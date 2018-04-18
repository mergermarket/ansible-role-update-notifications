#!/usr/bin/env python

import os
import sys
from datadog import initialize, api


def main(argv):
    options = {
        'api_key': os.getenv('DATADOG_API_TOKEN'),
    }
    updates = argv[0]
    updates_key = argv[1]
    jenkins_job_name = os.getenv('JENKINS_JOB_NAME')

    initialize(**options)

    title = "Software Update!"
    text = 'update-notifier (yum-cron) has flagged the following updates {}'.format(updates)
    tags = ['jenkins_job_name:{}'.format(jenkins_job_name)]

    api.Event.create(title=title, text=text, tags=tags, source_type_name='Amazon EC2', aggregation_key=updates_key)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))