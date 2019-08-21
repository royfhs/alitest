FROM python:2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD python manager.py runserver -h 0.0.0.0

EXPOSE 5000
