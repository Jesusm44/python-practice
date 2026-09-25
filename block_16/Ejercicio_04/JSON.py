import json
from pathlib import Path
from typing import Any

# We import the `Path` class from the `pathlib` module to work with file and directory paths in a more convenient and portable way.
DIR = Path(__file__).parent / "data"

# If the folder does not exist at this location, we create it, ensuring that it exists and that any necessary parent folders are created before the final folders.
DIR.mkdir(parents=True, exist_ok=True)

# We create the .txt file where the product files will go, placing it inside the folder we just created.
FILE: Path = DIR / "products.txt"

product:dict[str,Any] = {
    "code" : "A001",
    "name" : "Keyboard",
    "cent_price" : "2500",
    "stock" : 10,
}

# We open the file and use `json.dump()` to convert the Python data to JSON.
with open (
    FILE,
    "w",
    encoding= "utf-8"
) as archive:
    result = json.dump(product, archive)

print(result)
print(type(result))


# We open the file and use `json.loads()` to convert the JSON data into a Python dictionary.
with open(
    FILE,
    "r",
    encoding="utf-8"
) as archive:
    result:None = json.load(archive)

print(result)
print(type(result))