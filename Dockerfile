FROM python
RUN apt-get install netcat net-tools
WORKDIR /opt/simple-web-server
COPY . .
EXPOSE 8080

CMD ["python3", "server.py"]
