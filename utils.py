import csv
import os
import re
from operator import itemgetter


def csv_to_dict(filename):
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        csv_data = [line for line in reader]
    return csv_data


def get_job_filenames(directory):
    full_filenames = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            filename = os.path.join(root, file)
            full_filenames.append(filename)

    return full_filenames


def evaluate_job_file(filename, metrics):

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


def order_by_key(results_list, order_key):
    reordered_results = sorted(results_list, key=itemgetter(order_key))
    return reordered_results
