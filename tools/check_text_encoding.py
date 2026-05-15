#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

SKIP_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",
    ".ico",
    ".wav",
    ".mp3",
    ".ogg",
    ".zip",
    ".pack",
    ".idx",
    ".rev",
}

TEXT_EXTENSIONS = {
    "",
    ".md",
    ".py",
    ".yaml",
    ".yml",
    ".json",
    ".txt",
    ".ps1",
    ".cmd",
    ".bat",
    ".gitignore",
    ".gitattributes",
    ".editorconfig",
}

MOJIBAKE_MARKERS = tuple(
    chr(codepoint)
    for codepoint in (
        0x951B,
        0x7ECB,
        0x74BA,
        0x93B4,
        0x705E,
        0x95AB,
        0x5987,
        0x9FA5,
        0xFFFD,
    )
)


def should_scan(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    if path.suffix.lower() in SKIP_EXTENSIONS:
        return False
    return path.suffix.lower() in TEXT_EXTENSIONS


def scan_file(path: Path) -> list[str]:
    errors = []
    data = path.read_bytes()
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        return [f"{path}: 非 UTF-8 文本: {exc}"]

    for marker in MOJIBAKE_MARKERS:
        if marker in text:
            errors.append(f"{path}: 疑似乱码标记 `{marker}`")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="检查文本文件是否为 UTF-8，且未混入常见中文乱码。")
    parser.add_argument("--root", default=".", help="扫描根目录")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors = []
    scanned = 0

    for path in sorted(root.rglob("*")):
        if not path.is_file() or not should_scan(path.relative_to(root)):
            continue
        scanned += 1
        errors.extend(scan_file(path))

    if errors:
        print("text-encoding: FAIL")
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print("text-encoding: PASS")
    print(f"INFO  scanned files: {scanned}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
