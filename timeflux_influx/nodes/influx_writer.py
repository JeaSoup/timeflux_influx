"""influx write node"""

from timeflux.core.node import Node
from influxdb import DataFrameClient, InfluxDBClient
from dotenv import load_dotenv
import os
load_dotenv()


class InfluxWriter(Node):

    """Writes ``data`` to given Influx database.

    Attributes:
        i (Port): Default input, expects DataFrame.
        o (Port): Default output, provides DataFrame.
    """

    def __init__(self, database, measurement, port=8086):
   
        self._port = port
        self._database = database
        self._measurement = measurement
        self._username = os.getenv("DB_USER")
        self._password = os.getenv("DB_PASSWORD")
        self._host = os.getenv("DB_HOST")

        self._client = DataFrameClient(host=self._host, port=self._port, database= self._database, username=self._username, password=self._password)
        try:
            self._client
        except:
            raise Exception("Could not connect to host, please review your client information.")
        else:
             self.logger.debug('Connection established to host!')

    def update(self):
        self.logger.debug('Writing to database..')
        if self.i.ready():
            self._client.write_points(self.i.data, self._measurement, batch_size=1000)
