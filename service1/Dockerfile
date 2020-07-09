FROM python:latest

RUN apt update
RUN apt install python3-pip -y

COPY . .

RUN pip3 install -r requirements.txt

CMD ["env"]
EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/python3", "app.py"]

