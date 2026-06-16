from __future__ import annotations

import argparse
from pathlib import Path

from playwright.sync_api import sync_playwright


def render(html_path: Path, output_dir: Path, width: int = 1280, height: int = 720) -> None:
    html_path = html_path.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=2)
        page.goto(html_path.as_uri(), wait_until="networkidle")
        slides = page.locator(".slide")
        count = slides.count()
        if count == 0:
            raise RuntimeError("No .slide elements found in HTML.")
        for index in range(count):
            slides.nth(index).screenshot(path=str(output_dir / f"slide_{index + 1:02d}.png"))
        browser.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Render HTML .slide elements to PNG screenshots.")
    parser.add_argument("html", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    args = parser.parse_args()
    render(args.html, args.output_dir, args.width, args.height)


if __name__ == "__main__":
    main()
