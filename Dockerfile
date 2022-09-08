FROM python:3.10.7

WORKDIR /opt

RUN pip install ansible ansible-lint && \
    printf '[defaults]\nroles_path=../' >ansible.cfg

COPY . .
