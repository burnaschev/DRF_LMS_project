FROM python:3

WORKDIR /LMS

RUN pip install --upgrade pip

COPY requirements.txt /LMS

RUN pip install -r requirements.txt /LMS

COPY . .

