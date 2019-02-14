import os

from carpet import get_pyjob_codes, get_pyjob_content

JOBS_DIRECTORY = 'jobs/pyjobs'

if __name__ == '__main__':

    pyjob_codes = []
    for page in range(1, 7):
        pyjob_codes += get_pyjob_codes(page=page)

    for pyjob_code in pyjob_codes:
        print('Downloading pyjob {}'.format(pyjob_code))
        content = get_pyjob_content(pyjob_code)

        filename = 'job{}.txt'.format(pyjob_code)
        full_filename = os.path.join(JOBS_DIRECTORY, filename)

        with open(full_filename, 'w') as pyjob_file:
            pyjob_file.write(content)
