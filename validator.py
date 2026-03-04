from pathlib import Path


def validate_file_exists(file_path: Path) -> None:
    if not file_path.exists():
        raise ValueError(f"{file_path} doesn't exist. Please try again.")

def validate_file_not_empty(file_path: Path) -> None:
    if file_path.stat().st_size == 0:
        raise ValueError(f"{file_path} is empty. Please try again.")

def validate_filter_column(column: str, headers: list) -> None:
    if column not in headers:
        raise ValueError(f"Invalid column: {column}. Existing filter columns are: {', '.join(headers)}")

def validate_filter_operator(operator: str) -> None:
    valid_operators = [">", "<", ">=", "<=", "==", "!="]
    if operator not in valid_operators:
        raise ValueError(f"Invalid operator: {operator}. Valid operator are: {', '.join(valid_operators)}")

def validate_filter_type(column: str, operator: str, sample_row: dict) -> None:
    column_value = sample_row[column]
    numeric_operator = [">", "<", ">=", "<="]
    
    if isinstance(column_value, str) and operator in numeric_operator:
        raise ValueError(
            f"Cannot use '{operator}' on colum '{column}' "
            f"because it contains text values like '{column_value}'. "
            f"Use == or != for text column"
        )

def validate_groupby_column(column: str, headers: list) -> None:
    if column not in headers:
        raise ValueError(f"Invalid column: {column}. Existing groupby columns are: {', '.join(headers)}")

def validate_all(file_path: Path, headers: list, sample_row: dict, filter_column: str | None = None, filter_operator: str | None = None, filter_value: str | None = None, groupby_column: str | None = None) -> None:
    # Always check 
    validate_file_exists(file_path)
    validate_file_not_empty(file_path)

    # Only if filter was provided
    if filter_column is not None and filter_operator is not None and filter_value is not None:
        validate_filter_column(filter_column, headers)
        validate_filter_operator(filter_operator)
        validate_filter_type(filter_column, filter_operator, filter_value, sample_row)

