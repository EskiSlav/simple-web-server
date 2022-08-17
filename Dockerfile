FROM python

WORKDIR /opt/simple-web-server
COPY . .
EXPOSE 8080

CMD ["python", "server.py"]