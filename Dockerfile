FROM python:3.9

ADD main.py .

RUN pip install datetime flask flask_restful

CMD ["python", "./main.py"]
