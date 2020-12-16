FROM balenalib/raspberry-pi:buster

WORKDIR /app
COPY . .

RUN apt-get update
RUN apt-get update && apt-get install build-essential -y

RUN apt-get install python3.7 -y &&\
    apt-get install python3-pip -

RUN apt-get install libhdf5-dev -y &&\
    apt-get install libblas-dev liblapack-dev libatlas-base-dev

RUN pip3 install setuptools &&\
    pip3 install timeflux &&\
    pip3 install timeflux_bitalino &&\
    pip3 install influxdb

CMD [ "timeflux", "-d", "examples/test_influx_bitalino.yaml" ]
