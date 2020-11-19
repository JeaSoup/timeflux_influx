FROM python:3.7

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8086

# CMD tail -f /dev/null
CMD [ "timeflux", "-d", "timeflux_influx/examples/basic.yaml" ]
