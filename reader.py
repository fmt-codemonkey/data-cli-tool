from pathlib import Path
from typing import Generator

def read_file(file_path: Path) -> Generator[dict, None, None]:
    if file_path.suffix == ".csv":
        # Read csv here
        pass
    elif file_path.suffix == ".json":
        # Read json file here
        pass
    else:
        raise ValueError(
            f"Unsupported file type '{file_path.suffix}'."
            f"Only .csv and .json are supported."
        )