FROM python:3.11.1-alpine3.17

RUN apk add --no-cache bash

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "/usr/src/app/docker_entrypoint.sh" ]
