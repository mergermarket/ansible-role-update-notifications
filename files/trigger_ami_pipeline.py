#!/usr/bin/env python

import sys
from os import environ
from jenkins import Jenkins


def main(argv):
    jenkins_master = environ['JENKINS_MASTER']
    jenkins_user = environ['JENKINS_USER']
    jenkins_password = environ['JENKINS_PASSWORD']
    client = Jenkins(
        jenkins_master,
        jenkins_user,
        jenkins_password
    )

    ami_id = argv[1]

    jobs = client.get_jobs(folder_depth=4)

    for job in jobs:
        if 'ami' in job['fullname']:
            job_info = client.get_job_info(job['fullname'])
            if job_info['lastSuccessfulBuild']:
                log = client.get_build_console_output(job['fullname'], job_info['lastSuccessfulBuild']['number'])
                if ami_id in log:
                    print(f"Building {job['fullname']} pipeline on {jenkins_master}")
                    client.build_job(job['fullname'])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))