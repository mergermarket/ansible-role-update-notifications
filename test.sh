#!/bin/bash

set -euo pipefail

IMAGE_ID="$(basename $(pwd))"

docker image build -t "${IMAGE_ID}" .

docker container run --rm --name "${IMAGE_ID}" \
    $(tty -s && echo -t) \
    "${IMAGE_ID}" \
    ansible-playbook tests/test.yml -i tests/inventory --syntax-check

docker container run --rm --name "${IMAGE_ID}" \
    $(tty -s && echo -t) \
    "${IMAGE_ID}" \
    ansible-lint .

docker container run --rm -i -v "$(pwd)":"$(pwd)" -w "$(pwd)" \
    koalaman/shellcheck \
    ./files/notify_updates
