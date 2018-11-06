FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

ADD src/requirements.txt /src/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD ./src/ /src/

EXPOSE 8040