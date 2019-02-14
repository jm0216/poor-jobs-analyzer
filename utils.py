import csv
import os
import re
from operator import itemgetter


def csv_to_list(filename: str) -> list:
    """Receive an csv filename and returns rows of file with an list"""
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        csv_data = [line for line in reader]
    return csv_data


def get_files_in_directory(directory: str) -> list:
    """Receive an directory and returns an list of filenames in directory"""
    full_filenames = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            filename = os.path.join(root, file)
            full_filenames.append(filename)

    return full_filenames


def evaluate_job_file(filename: str, metrics: list) -> int:
    """
    Receive an filename and metrics (list of dicts containing metrics)
    and return an poor level
    """
    poor_level = 0

    with open(filename) as file:
        content = file.read()

    for metric in metrics:
        lower_term = metric['Terms'].lower()
        pattern = r'\b{}\b'.format(lower_term)
        lower_content = content.lower()

        if re.search(pattern, lower_content):
            poor_level += int(metric['Poor level'])

    return poor_level


def order_by_key(results_list: list, order_key: str) -> list:
    """Receive an list of dicts and return ordered list by order_key"""
    reordered_results = sorted(results_list, key=itemgetter(order_key))
    return reordered_results
