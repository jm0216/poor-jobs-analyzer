import os

from utils import get_pyjob_codes, get_pyjob_content


JOBS_DIRECTORY = 'jobs/pyjobs'


if __name__ == '__main__':
    pyjob_codes = get_pyjob_codes()

    pyjob_url = 'http://www.pyjobs.com.br/job/{}/'
    for pyjob_code in pyjob_codes:
        content = get_pyjob_content(pyjob_code)

        filename = 'job{}.txt'.format(pyjob_code)
        full_filename = os.path.join(JOBS_DIRECTORY, filename)

        with open(full_filename, 'w') as pyjob_file:
            pyjob_file.write(content)
