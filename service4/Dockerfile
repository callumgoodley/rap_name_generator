FROM python:latest

RUN apt update
RUN apt install python3-pip -y 

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5003
CMD ["env"]
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]

