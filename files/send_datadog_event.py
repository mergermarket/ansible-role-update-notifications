#!/usr/bin/env python

import os
import sys
from datadog import initialize, api


def main(argv):
    options = {
        'api_key': os.getenv('DATADOG_API_TOKEN'),
    }
    updates = argv[0]
    jenkins_job_name = os.getenv('JENKINS_JOB_NAME')

    stateless = bool(int(os.getenv('STATELESS_INSTANCE', 1)))

    initialize(**options)

    title = "Software Update!"
    text = 'update-notifier (yum-cron) has flagged ' \
           'the following updates \n{}'.format(updates)
    tags = [
        'job:{}'.format(jenkins_job_name),
        'stateless:{}'.format(stateless),
    ]

    api.Event.create(title=title, text=text, tags=tags)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
