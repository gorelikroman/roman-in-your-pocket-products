#!/usr/bin/env python3
"""Refresh the Reboost pack from the design handbook in beluga-ds.

The pack (plugins/roman-in-your-pocket-reboost/skills/product-layer/) is a portable summary of
beluga-ds docs/design-handbook/. source.json in that folder records the beluga-ds commit the
summary was taken from. This script compares it with a beluga-ds checkout and:

  --check      reports what changed in the handbook since the recorded commit; exits 1 when the
               pack is behind (usable in CI), 0 when it is current
  (default)    also refreshes the mechanical parts: design-decisions.md becomes the new
               09-decisions.md under its header comment, source.json and the commit named in
               product.md move to the new commit, the plugin version gets a minor bump.
               It then lists the chapters whose changes product.md has to absorb: that prose is
               a summary and is updated by a person or by the critic, never by this script.

    python3 scripts/sync_reboost.py --beluga ../beluga-ds --check
    python3 scripts/sync_reboost.py --beluga ../beluga-ds

The checkout must contain the recorded commit; in a shallow clone run
`git -C ../beluga-ds fetch --depth=500 origin` first. Standard library only.
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACK = os.path.join(ROOT, "plugins", "roman-in-your-pocket-reboost")
LAYER = os.path.join(PACK, "skills", "product-layer")
SOURCE = os.path.join(LAYER, "source.json")
HEADER = """<!-- Snapshot of beluga-ds docs/design-handbook/09-decisions.md at commit {commit}, taken
     {date} by scripts/sync_reboost.py. The canonical log lives in beluga-ds; edit it there and
     refresh this copy. Relative links below (05-design-rules.md, 13-…, 16-…, 17-…, 18-…,
     10-fix-backlog.md, 08-design-review/) point into beluga-ds/docs/design-handbook/. Node ids
     (1:877 …) are in the review collection file vdFkmYUE5h0ndTS9pfc2k8 unless another file is named. -->

"""


def git(repo, *args):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"git {' '.join(args)} failed in {repo}:\n{r.stderr.strip()}")
    return r.stdout


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    ap = argparse.ArgumentParser(description="Refresh the Reboost pack from beluga-ds.")
    ap.add_argument("--beluga", default=os.path.join(ROOT, "..", "beluga-ds"),
                    help="path to a beluga-ds checkout (default: ../beluga-ds next to this repository)")
    ap.add_argument("--rev", default="HEAD",
                    help="beluga-ds revision to sync to (default: HEAD; e.g. origin/main)")
    ap.add_argument("--check", action="store_true", help="report only; exit 1 when the pack is behind")
    args = ap.parse_args()

    src = json.loads(read(SOURCE))
    repo, book, log = os.path.abspath(args.beluga), src["handbook"], src["log"]
    if not os.path.isdir(os.path.join(repo, ".git")) and not os.path.isfile(os.path.join(repo, ".git")):
        sys.exit(f"{repo} is not a git checkout of beluga-ds; pass --beluga")
    old = src["commit"]
    if subprocess.run(["git", "-C", repo, "cat-file", "-e", f"{old}^{{commit}}"]).returncode:
        sys.exit(f"recorded commit {old} is not in {repo}; fetch more history "
                 f"(git -C {repo} fetch --depth=500 origin) and run again")
    new = git(repo, "rev-parse", "--short=8", args.rev).strip()

    changed = [l.split("\t") for l in git(repo, "diff", "--name-status", old, new, "--", book).splitlines() if l]
    docs = [(s[0], s[-1]) for s in changed if s[-1].endswith((".md", ".json"))]
    if not docs:
        print(f"Reboost pack is current: the handbook has not changed since {old} (beluga-ds {new}).")
        return 0

    last = git(repo, "log", "-1", "--format=%h %ad", "--date=short", new, "--", book).strip()
    print(f"Handbook changed since {old} — last change {last}; syncing to {new}.\n")
    kinds = {"A": "new", "M": "changed", "D": "removed"}
    for status, path in docs:
        print(f"  {kinds.get(status[0], status):8} {os.path.relpath(path, book)}")
    log_changed = any(path == log for _, path in docs)

    if args.check:
        print("\nThe pack is behind. Run without --check to refresh it.")
        return 1

    today = datetime.date.today().isoformat()
    # The header carries the commit, so the copy is rewritten even when the log itself did not change.
    write(os.path.join(LAYER, "design-decisions.md"),
          HEADER.format(commit=new, date=today) + git(repo, "show", f"{new}:{log}"))

    product_path = os.path.join(LAYER, "product.md")
    product = read(product_path)
    product = product.replace(f"beluga-ds@{old}", f"beluga-ds@{new}")
    product = product.replace(f"commit `{old}`", f"commit `{new}`")
    product = re.sub(r"Last updated: \d{4}-\d{2}-\d{2}", f"Last updated: {today}", product, count=1)
    write(product_path, product)

    src.update(commit=new, synced=today)
    write(SOURCE, json.dumps(src, indent=2) + "\n")

    plugin_path = os.path.join(PACK, ".claude-plugin", "plugin.json")
    plugin = json.loads(read(plugin_path))
    major, minor, _patch = (int(x) for x in plugin["version"].split("."))
    plugin["version"] = f"{major}.{minor + 1}.0"
    write(plugin_path, json.dumps(plugin, indent=2, ensure_ascii=False) + "\n")

    prose = [os.path.relpath(p, book) for s, p in docs if p != log]
    print(f"\nRefreshed: design-decisions.md{' (log changed)' if log_changed else ''}, source.json, "
          f"the commit in product.md, version {plugin['version']}.")
    if prose:
        print("\nproduct.md summarises these chapters; update its prose by hand or ask the critic "
              "(\"refresh the Reboost layer from these chapters\"):")
        for p in prose:
            print(f"  - {p}")
        print(f"  (diff: git -C {repo} diff {old} {new} -- {book}/<chapter>)")
    print("\nThen commit, push, and teammates run "
          "`claude plugin update roman-in-your-pocket-reboost@roman-in-your-pocket-products`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
