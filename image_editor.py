from PIL import Image, ImageFilter
from pathlib import Path
import argparse

# ──────────────────────────────────────────────────────────────────────────────
#                                  CONFIG
# ──────────────────────────────────────────────────────────────────────────────

FILTERS = {
    'BLUR':         ImageFilter.BLUR,
    'CONTOUR':      ImageFilter.CONTOUR,
    'DETAIL':       ImageFilter.DETAIL,
    'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
    'SHARPEN':      ImageFilter.SHARPEN,
    'SMOOTH':       ImageFilter.SMOOTH,
}

SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp'}

# ──────────────────────────────────────────────────────────────────────────────
#                             CORE FUNCTION
# ──────────────────────────────────────────────────────────────────────────────

def apply_filters(image_path: Path, filter_types: list[str]) -> dict:
    """Apply one or more filters to a single image and save the result."""

    filter_types = [f.upper() for f in filter_types]

    # Validate filters
    for f in filter_types:
        if f not in FILTERS:
            raise ValueError(
                f"Unsupported filter: '{f}'\n"
                f"Supported filters: {', '.join(FILTERS.keys())}"
            )

    # Validate image path
    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Validate image format
    if image_path.suffix.lower() not in SUPPORTED_FORMATS:
        raise ValueError(
            f"Unsupported format: '{image_path.suffix}'\n"
            f"Supported formats: {', '.join(SUPPORTED_FORMATS)}"
        )

    # Open, convert, and apply filters
    with Image.open(image_path) as img:
        img = img.convert('RGB')

        for f in filter_types:
            img = img.filter(FILTERS[f])

        # Build output path: photo.jpg → photo_BLUR_SHARPEN.jpg
        output_path = image_path.parent / (
            f"{image_path.stem}_{'_'.join(filter_types)}{image_path.suffix}"
        )

        img.save(output_path)

    return {
        "input":   str(image_path),
        "output":  str(output_path),
        "filters": filter_types,
        "status":  "success",
    }

# ──────────────────────────────────────────────────────────────────────────────
#                           DIRECTORY FUNCTION
# ──────────────────────────────────────────────────────────────────────────────

def process_directory(directory_path: Path, filters: list[str]):
    """Apply filters to every supported image in a folder."""

    if not directory_path.is_dir():
        raise NotADirectoryError(f"Not a valid directory: {directory_path}")

    results = []

    for image_file in directory_path.iterdir():
        if image_file.suffix.lower() in SUPPORTED_FORMATS:
            try:
                result = apply_filters(image_file, filters)
                results.append(result)
                print(f"✅ {result['input']} → {result['output']}")
            except Exception as e:
                print(f"❌ Skipped {image_file.name}: {e}")

    print(f"\n📁 Done. {len(results)} image(s) processed in: {directory_path}")

# ──────────────────────────────────────────────────────────────────────────────
#                                CLI ENTRY POINT
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Apply filters to images using Pillow.",
        epilog=f"Available filters: {', '.join(FILTERS.keys())}"
    )
    parser.add_argument("--image_path",     type=Path, help="Path to a single image")
    parser.add_argument("--directory_path", type=Path, help="Path to a folder of images")
    parser.add_argument("--filters", nargs='+', required=True,
                        help="Filters to apply e.g. BLUR SHARPEN")

    args = parser.parse_args()

    try:
        if args.image_path and args.directory_path:
            raise ValueError("Use --image_path or --directory_path, not both.")
        elif args.image_path:
            result = apply_filters(args.image_path, args.filters)
            print(f"✅ Saved: {result['output']}")
        elif args.directory_path:
            process_directory(args.directory_path, args.filters)
        else:
            parser.print_help()

    except Exception as e:
        print(f"❌ Error: {e}")
