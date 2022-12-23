import csv
from pathlib import Path
from typing import Iterator


def read_csv(filename: str) -> Iterator[dict[str, str]]:
    with open(Path(__file__).parent.resolve() / "imports" / filename) as f:
        csv_file = csv.DictReader(f, delimiter=";")
        for row in csv_file:
            yield row
