FROM python

ENV APP_DIR=/usr/src/app

RUN mkdir $APP_DIR
WORKDIR $APP_DIR

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

RUN python manage.py collectstatic

EXPOSE 8000

CMD gunicorn task_tracker_backend.wsgi --bind 0.0.0.0:8000
