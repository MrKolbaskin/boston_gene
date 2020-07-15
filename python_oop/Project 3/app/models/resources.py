# resource module

from app.utils import validators


class Resource:

    def __init__(self, name, manufacturer, total, allocated=0):
        validators.validate_str('name', name)
        self._name = name

        validators.validate_str('manufacturer', manufacturer)
        self._manufacturer = manufacturer

        validators.validate_integer('total', total, min_value=0)
        self._total = total

        validators.validate_integer('allocated', allocated, min_value=0, max_value=total)
        self._allocated = allocated

        self._count_available = None

    def __str__(self):
        return f'This is resource - {self.name}'

    def __repr__(self):
        return (f'{self.name} ({self.category} - {self.manufacturer}) : '
                f'total={self.total}, allocated={self.allocated}'
                )

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    @property
    def available(self):
        if self._count_available is None:
            self._count_available = self.total - self.allocated
        return self._count_available

    def claim(self, count_claim):
        validators.validate_integer('count_claim', count_claim, min_value=1, max_value=self.available)
        self._count_available = None
        self._allocated += count_claim

    def freeup(self, count_freeup):
        validators.validate_integer('count_freeup', count_freeup, min_value=1, max_value=self.allocated)
        self._count_available = None
        self._allocated -= count_freeup

    def died(self, count_died):
        validators.validate_integer('count_died', count_died, min_value=1, max_value=self.allocated)
        self._count_available = None
        self._total -= count_died
        self._allocated -= count_died

    def purchased(self, count_purchased):
        validators.validate_integer('count_freeup', count_purchased, min_value=1)
        self._count_available = None
        self._total += count_purchased

    @property
    def category(self):
        return self.__class__.__name__.lower()
