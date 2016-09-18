FROM python:3.5
RUN mkdir /app
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
