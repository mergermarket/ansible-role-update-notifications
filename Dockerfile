FROM python:3.8.6

WORKDIR /opt

RUN pip install ansible ansible-lint && \
    printf '[defaults]\nroles_path=../' >ansible.cfg

COPY . .
