import json
from config import DATA_FILE

def save_patient(patients):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(patients, file)

def load_patients():
    try:
        with open(DATA_FILE, "r") as file:
            list_patients = json.load(file)
            if isinstance (list_patients, list):
                return list_patients
            raise TypeError("The json is not a list")
    except FileNotFoundError:
        return []
    
