# cpu module

from app.models.resources import Resource
from app.utils import validators


class CPU(Resource):
    def __init__(self, name, manufacturer, cores, socket, power_watts, total, allocated=0):
        super().__init__(name, manufacturer, total, allocated)

        validators.validate_integer('cores', cores, min_value=1)
        self._cores = cores

        self._socket = socket

        validators.validate_integer('power_watts', power_watts, min_value=1)
        self._power_watts = power_watts

    def __str__(self):
        return super().__str__() + '\nType: CPU'

    def __repr__(self):
        return f'{self.category}: {self.name} ({self.socket} - x{self.cores})'

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts
