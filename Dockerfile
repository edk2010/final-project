#FROM python:3.8-alpine
FROM python:3.10-slim
WORKDIR /app


COPY ./lambda.py /app
COPY ./unitest.py /app
COPY ./requirements.txt /app
RUN apt-get -y update
RUN pip install --upgrade pip

# install the dependencies and packages in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

CMD ["tail", "-f", "/dev/null"]
#CMD ["python","employees.py" ]

