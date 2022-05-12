# Template from jacobtomlinson/python-container-action
FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

RUN apt update && apt install -y curl
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null
RUN apt update && apt install -y gh

RUN pip install PyYAML

ENTRYPOINT ["python3", "main.py"]
