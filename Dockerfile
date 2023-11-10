FROM python:3.10

WORKDIR /LMS

RUN pip install --upgrade pip

COPY requirements.txt /LMS

RUN pip install -r requirements.txt

COPY . .

