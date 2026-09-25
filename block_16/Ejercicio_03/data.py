# We import the `Path` class from the `pathlib` module to work with file and directory paths in a more convenient and portable way.
from pathlib import Path

# We create a variable with the file path and another variable containing the file and the path.
DIR: Path = Path(__file__).parent / "data"
FILE: Path = DIR / "products.txt"

# We use `with` and `open` to open the file so that it closes automatically when no longer in use, specifying read mode and UTF-8 encoding.
with open(
    FILE,
    "r",
    encoding= "utf-8"
)as archive:
    for product in archive:
        print(product.strip())


