class MenuItem:

    def __init__(self, name, cost=0, qty=0):
        self._name = name
        self._cost = cost
        self._qty = qty

    @property
    def name(self):
        print("im in the getter")
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __str__(self):
        return self._name, self._cost, self._qty

    def __repr__(self):
        return f'{self._name}: {self._cost},{self._qty}'





