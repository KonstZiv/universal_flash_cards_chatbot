FROM python:3.10-slim-buster AS system

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PYTHONPYCACHEPREFIX=/.pycache

# Let all *.pyc files stay within the container, for Python >= 3.8
RUN mkdir -p $PYTHONPYCACHEPREFIX

# Use non-interactive frontend for debconf
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install system requirements
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential curl gettext libpq-dev zlib1g-dev libjpeg62-turbo-dev && \
    rm -rf /var/lib/apt/lists/*

ARG USER_ID=1000
RUN useradd --create-home --user-group -u $USER_ID user

USER $USER_ID
WORKDIR /home/user

RUN pip install -U pip 'setuptools<58' wheel

RUN curl -sSL https://install.python-poetry.org | python3 -

# Create a virtual env in home directory.
ENV VIRTUAL_ENV=/home/user/.venv
ENV PATH="${VIRTUAL_ENV}/bin:/home/user/.local/bin:${PATH}"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true


FROM system AS poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT=false

VOLUME /src
WORKDIR /src


FROM system AS dev

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

# Set the default directory where CMD will execute
WORKDIR /app

CMD bash
