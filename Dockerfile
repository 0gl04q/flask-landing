FROM python:3.12-slim-bookworm

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt -y update && \
    apt install -y python3-dev libpq-dev python3-dev

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /src

CMD ["gunicorn", "-b", "0.0.0.0:8000", "src.app:app"]