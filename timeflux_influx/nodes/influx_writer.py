"""influx write node"""

from timeflux.core.node import Node
from influxdb import DataFrameClient, InfluxDBClient


class InfluxWriter(Node):

    """Writes ``data`` to given Influx database.

    Attributes:
        i (Port): Default input, expects DataFrame.
        o (Port): Default output, provides DataFrame.
    """

    def __init__(self, database, measurement, port=8086, host='localhost'):
        """
        Args:
            host (string)
            port (int)
        """
        self._port = port
        self._host = host
        self._database = database
        self._measurement = measurement
        self._client = DataFrameClient(host=self._host, port=self._port, database= self._database)
        if self._client:
            self.logger.debug('Connection established - Host: ' + self._host + ' port: ' + str(self._port) + ' database ' + self._database)
        else:
            self.logger.debug('Something went wrong.')

    def update(self):
        self.logger.debug('Writing to database..')
        if self.i.ready():
            self._client.write_points(self.i.data, self._measurement, batch_size=1000)
