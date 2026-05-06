# 🖼️ Image Filter Tool

A command-line Python tool that applies filters to images — one at a time or an entire folder in one go.

Built with Pillow. Handles single images and batch folder processing with clean error reporting.

---

## Features

- Apply one or multiple filters in sequence
- Process a single image or a full folder
- Supports JPG, PNG, JPEG, BMP, GIF, WEBP
- Auto-generates output filenames (e.g. photo_BLUR_SHARPEN.jpg)
- Input validation with clear error messages
- RGB conversion built-in (no crashes on transparent PNGs)

---

## Available Filters

| Filter       | Effect                              |
|--------------|-------------------------------------|
| BLUR         | Softens the image                   |
| CONTOUR      | Draws edges like a sketch           |
| DETAIL       | Enhances fine details               |
| EDGE_ENHANCE | Makes edges more visible            |
| SHARPEN      | Increases clarity                   |
| SMOOTH       | Reduces noise, gentle softening     |

---

## Installation

```bash
pip install pillow
```

---

## Usage

**Single image:**
```bash
python image_filter.py --image_path photo.jpg --filters BLUR SHARPEN
```

**Entire folder:**
```bash
python image_filter.py --directory_path ./images --filters CONTOUR
```

---

## Output

The filtered image is saved in the same folder as the original.
Filename example: `photo_BLUR_SHARPEN.jpg`

---

## Tech Stack

- Python 3.10+
- Pillow (PIL)
- argparse
- pathlib

---

## Author

**Umar Shahzad**
Data Analyst | Python Automation
🔗 [GitHub](https://github.com/umar-data-analyst) · [LinkedIn](https://www.linkedin.com/in/umar-data-analyst/) · [Upwork](https://www.upwork.com/freelancers/umarshahzad30)
