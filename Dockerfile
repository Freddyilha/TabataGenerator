FROM python:3.9

WORKDIR /usr/src/app

RUN apt update \
    && apt install -y --no-install-recommends \
        postgresql-client \
    && apt install -y vim \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 7676

RUN adduser --disabled-password --gecos "" docker

RUN chown -R docker:docker /usr/src/app

RUN chmod 755 /usr/src/app

USER docker

CMD ["python", "manage.py", "runserver", "0.0.0.0:7676"]
