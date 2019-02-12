from utils import csv_to_dict, evaluate_job, get_job_filenames, order_by_key

METRICS_FILENAME = 'metrics.csv'
JOBS_DIRECTORY = 'jobs'

if __name__ == '__main__':
    results = []
    metrics = csv_to_dict(METRICS_FILENAME)
    job_files = get_job_filenames(JOBS_DIRECTORY)

    for job_file in job_files:
        poor_level = evaluate_job(job_file, metrics)
        results.append({'job_file': job_file, 'poor_level': poor_level})

    results = order_by_key(results, 'poor_level')
    for result in results:
        print('Poor level: {} - Job file: {}'.format(
            result['poor_level'],
            result['job_file'],
        ))
