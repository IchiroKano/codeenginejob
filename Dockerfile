FROM python:3
USER root
WORKDIR /usr
COPY . .
RUN pip install cloudant
CMD [ "python", "./cloudant-db-add-rand.py" ]
