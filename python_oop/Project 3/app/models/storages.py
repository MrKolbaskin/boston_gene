# storage module

from app.models.resources import Resource
from app.utils import validators


class Storage(Resource):
    def __init__(self, name, manufacturer, capacity, total, allocated=0):
        super().__init__(name, manufacturer, total, allocated)

        validators.validate_integer('capacity', capacity, min_value=0)
        self._capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    def __repr__(self):
        return f'{self.category}: {self.capacity} GB'


class HDD(Storage):
    def __init__(self, name, manufacturer, capacity, size, rpm, total, allocated=0):
        super().__init__(name, manufacturer, capacity, total, allocated)

        validators.validate_integer('size', size, min_value=0)
        self._size = size

        validators.validate_integer('rpm', rpm, min_value=0)
        self._rpm = rpm

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.size}, {self.rpm} rpm)'


class SSD(Storage):
    def __init__(self, name, manufacturer, capacity, interface, total, allocated=0):
        super().__init__(name, manufacturer, capacity, total, allocated)

        self._interface = interface

    @property
    def interface(self):
        return self._interface

    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.interface})'
