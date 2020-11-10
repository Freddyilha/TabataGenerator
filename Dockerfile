FROM python:3.9

WORKDIR /usr/src/app

RUN apt update \
    && apt install -y --no-install-recommends \
        postgresql-client \
    && apt install -y vim \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN django-admin startproject TabataGenerator

COPY . .

EXPOSE 7676

CMD ["python", "TabataGenerator/manage.py", "runserver", "0.0.0.0:7676"]
