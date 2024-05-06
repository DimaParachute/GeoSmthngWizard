FROM python:3.9

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y --no-install-recommends binutils libproj-dev gdal-bin libgdal-dev python3-gdal

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=app/

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.6.1 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

COPY ./app ./
