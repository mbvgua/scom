#!/usr/bin/env python3
"""
compile src/static/scss/*.scss into src/static/css/*.css.

libsass is used rather than dart-sass because it is a pure wheel with no
platform binary, which keeps "pip install -r requirements.txt" sufficient on
every machine.

the compiled CSS is committed to the repository on purpose, so a fresh clone
runs without needing this script at all.

its best run as a module with:
    $ python -m scripts.styling                     # compile once
    $ python -m scripts.styling --watch             # recompile on change
"""

import argparse
import sys
import time
from pathlib import Path

try:
    import sass
except ImportError:  # pragma: no cover - developer convenience only
    print(
        "libsass is not installed. Run:\n" "    pip install libsass\n",
        file=sys.stderr,
    )
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parent.parent
SCSS_DIR = ROOT / "static" / "scss"
CSS_DIR = ROOT / "static" / "css"


def compile_all(watch: bool = False) -> int:
    """compile every .scss file. returns a process exit code."""

    SCSS_DIR.mkdir(parents=True, exist_ok=True)
    CSS_DIR.mkdir(parents=True, exist_ok=True)

    sources = sorted(SCSS_DIR.rglob("*.scss"))
    if not sources:
        print(f"no .scss files found in {SCSS_DIR}", file=sys.stderr)
        return 1

    failed = False

    for source in sources:
        # main.scss compiles to main.css; a partial (leading underscore) is
        # imported by another file and is not emitted on its own
        if source.name.startswith("_"):
            continue

        relative = source.relative_to(SCSS_DIR)
        target = (CSS_DIR / relative).with_suffix(".css")

        try:
            css = sass.compile(
                filename=str(source),
                output_style="compressed",
            )
        except sass.CompileError as exc:
            print(f"[FAIL] {relative}\n{exc}", file=sys.stderr)
            failed = True
            continue

        target.write_text(css, encoding="utf-8")
        print(f"[ok]   {relative} -> {target.relative_to(ROOT)} ({len(css):,} bytes)")

    if watch and not failed:
        print("\nwatching for changes, ctrl-c to stop")
        _watch(sources)
    elif failed:
        return 1

    return 0


def _watch(sources: list[Path]) -> None:
    """
    poll mtimes rather than depend on a file-watching package, which keeps the
    dependency list to libsass alone.
    """

    stamps = {p: p.stat().st_mtime for p in sources}

    try:
        while True:
            time.sleep(1)
            changed = [
                p for p in sources if p.exists() and stamps.get(p) != p.stat().st_mtime
            ]
            if changed:
                for path in changed:
                    stamps[path] = path.stat().st_mtime
                print(f"\nchange detected in {', '.join(p.name for p in changed)}")
                compile_all()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="compile the SCSS stylesheets")
    parser.add_argument(
        "--watch", action="store_true", help="recompile whenever a file changes"
    )
    args = parser.parse_args()

    raise SystemExit(compile_all(watch=args.watch))
