# start by pulling the python image
#FROM python:3.8-alpine
FROM python:3.8-slim
WORKDIR /app
# copy the requirements file into the image
#COPY ./requirements.txt /app/requirements.txt
#COPY ./employees.py /app/employees.py
#RUN mkdir /app
#RUN cd /app
RUN apt install git
RUN git clone https://github.com/edk2010/final-project.git
#RUN cd final-project/employees
WORKDIR /app/final-project/employees
# install the dependencies and packages in the requirements file
RUN pip install --no-cache-dir -r requirements.txt


# switch working directory


#EXPOSE 5000


# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["employees.py" ]