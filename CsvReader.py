import csv
from io import StringIO

import requests

from DataReader import DataReader


class CsvReader(DataReader):
	def read_data(self, path):
		"""Читання даних з CSV файлу за URL."""
		response = requests.get(path)
		response_text = StringIO(response.content.decode('utf-8-sig'))
		reader = csv.DictReader(response_text, delimiter=',')
		return list(reader)
