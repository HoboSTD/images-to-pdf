# Images to PDF

A program that converts given images into a single PDF file. The images have their EXIF rotation
applied and each take up a full page.

## Requirements

[FPDF](https://pyfpdf.readthedocs.io/en/latest/) and
[Pillow](https://pillow.readthedocs.io/en/stable/) are required for this to work.

## Usage

```
$ python3 main.py name
image path
image path
image path
...
```

Which produces the file `name.pdf` that has these images.
