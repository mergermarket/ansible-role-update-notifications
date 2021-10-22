Update Notifications
=========

[![Deploy to Ansible Galaxy](https://github.com/mergermarket/ansible-role-update-notifications/actions/workflows/deploy.yml/badge.svg)](https://github.com/mergermarket/ansible-role-update-notifications/actions/workflows/deploy.yml)

Send an event to Datadog if there are updates available via `yum`.

Requirements
------------

yum

Role Variables
--------------

None. This role is intended for immutable infrastructure where the Ansible playbook is applied during the AMI bake (e.g. with Packer). It includes the file `/etc/cron.d/notify_updates` containing the following placeholders that should be replaced on instance creation (e.g. from UserData):

* `%JENKINS_JOB_NAME_TEMPLATE%` - the value is included in the `job` tag on the event, so that the AMI build job can be triggered.
* `%DATADOG_API_KEY_TEMPLATE%` - the API key for posting to Datadog.

Dependencies
------------

None

License
-------

https://opensource.org/licenses/MIT

Copyright 2018 Mergermarket Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author Information
------------------

Acuris Platform Team
