import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "database" / "students.json"


def load_data():
    if JSON_PATH.exists():
        with open(JSON_PATH, "r") as file:
            return json.load(file)
    else:
        return []


Student_data = load_data()


def save_data():
    JSON_PATH.parent.mkdir(exist_ok=True)

    with open(JSON_PATH, "w") as file:
        json.dump(Student_data, file)
