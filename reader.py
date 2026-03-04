from pathlib import Path
from typing import Generator, Union

import csv
import json


def convert_value(value: str) -> Union[int, float, bool, str]:
    # Integer value
    try:
        return int(value)
    except ValueError:
        pass
    
    # Float value
    try:
        return float(value)
    except ValueError:
        pass

    # Boolean value
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    
    # String value
    return value


def read_file(file_path: Path) -> Generator[dict, None, None]:
    if file_path.suffix == ".csv":
        with open(file_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                converted_row = {key: convert_value(value) for key, value in row.items()}
                yield converted_row

    elif file_path.suffix == ".json":
        with open(file_path) as file:
            data = json.load(file)
            for row in data: 
                converted_row = {key: convert_value(value) for key, value in row.items()}
                yield converted_row
    else:
        raise ValueError(
            f"Unsupported file type '{file_path.suffix}'."
            f"Only .csv and .json are supported."
        )


if __name__ =="__main__":
    print("\n--- CSV TEST ---")
    for row in read_file(Path("data/employees.csv")):
        print(row)

    print("\n--- JSON TEST ---")
    for row in read_file(Path("data/employees.json")):
        print(row)