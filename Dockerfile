FROM python:3.10

RUN mkdir /bewise_test

WORKDIR /bewise_test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /bewise_test/
COPY . /bewise_test/src/
COPY . /bewise_test/docker/

RUN chmod +x docker/*.sh
ENTRYPOINT ["sh","./docker/bd.sh"]

