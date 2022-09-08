FROM pypy:3.9-slim-buster

COPY ./app/requirements.txt /opt/app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/app/requirements.txt

ARG USERNAME="fastapi"
ARG GROUPNAME="fastapi"
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME

COPY --chown=$USERNAME:$GROUPNAME ./app /opt/app

ENV PYTHONPATH "${PYTHONPATH}:/opt/app"

WORKDIR /opt/app

RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER $USERNAME


