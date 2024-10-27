FROM python:3.12.2-slim

WORKDIR /server

COPY ./pyproject.toml /server/
COPY ./poetry.lock /server/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./ /server
