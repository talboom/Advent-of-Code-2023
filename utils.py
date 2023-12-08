from typing import List


def read_input(file_path: str) -> list[str]:
    input_path = f"inputs/{file_path}"
    with open(input_path, 'r') as f:
        lines = [line.rstrip() for line in f]
    return lines