from pathlib import Path
import json


DIR = Path(__file__).parent
new_folder = DIR / "data"
file_path = new_folder / "products.json"

new_folder.mkdir(exist_ok=True)


def save_inventory(inventory):
    with file_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(inventory,file,ensure_ascii=False, indent= 4)

def load_inventory():
    with file_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        inventory = json.load(file)
    return inventory


