from pathlib import Path
import json

product = {
    "codigo": "A001",
    "nombre": "Teclado",
    "precio_cent": 2500,
    "stock": 10,
}

file_path = Path(__file__).parent / "data" / "data.json"

def save_product():
    with file_path.open(
        "w",
        encoding="utf-8"
) as archive:
        json.dump(product, archive, ensure_ascii=False, indent = 4)

def load_product():
    with file_path.open(
        "r",
        encoding ="utf-8",
    ) as archive:
        product = json.load(archive)
        return product

save_product()
print(load_product())