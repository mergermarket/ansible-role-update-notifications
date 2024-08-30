#!/usr/bin/env python

import os
import sys
from datadog import initialize, api
import subprocess
import socket


def main(argv):
    options = {
        'api_key': os.getenv('DATADOG_API_TOKEN'),
    }
    updates = argv[0]
    ami_build_job_name = os.getenv('AMI_BUILD_JOB_NAME')

    cluster = os.getenv('CLUSTER')
    stateless = bool(int(os.getenv('STATELESS_INSTANCE', 1)))
    
    process = subprocess.Popen(['uname', '-m'], stdout=subprocess.PIPE)
    output, error = process.communicate()
    architecture = output.decode().strip()
    priv_ip = socket.gethostbyname(socket.gethostname())

    initialize(**options)

    title = "Software Update!"
    text = 'update-notifier (yum-cron) has flagged ' \
           'the following updates \n{}'.format(updates)
    tags = [
        'job:{}'.format(ami_build_job_name),
        'stateless:{}'.format(stateless),
        'cluster:{}'.format(cluster),
        'architecture:{}'.format(architecture),
        'priv_ip:{}'.format(priv_ip),
    ]

    api.Event.create(title=title, text=text, tags=tags)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
