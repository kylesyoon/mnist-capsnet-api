FROM python:3.6.5
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

WORKDIR /code/mnist
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
