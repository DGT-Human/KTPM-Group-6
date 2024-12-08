import json
from pathlib import Path


class TestData:
    @staticmethod
    def load_data(file_path):
        base_path = Path(__file__).resolve().parent  # Thư mục của file Python hiện tại
        full_path = base_path / file_path
        with open(full_path, 'r', encoding='utf-8') as file:
            return json.load(file)

