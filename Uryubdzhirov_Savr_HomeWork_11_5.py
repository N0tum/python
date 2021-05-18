class WarehouseError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Warehouse:
    def __init__(self):
        self.__storage = []

    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise WarehouseError(f"{item} undefined")

        self.__storage.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise WarehouseError(f"{type(item)} undefined")

        item: OfficeEquipment = self.__storage[idx]

        if item.department:
            raise WarehouseError(f"{item} already in {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storage[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storage[key]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"number of devices: {len(self.__storage)}"


class OfficeEquipment:
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('printer', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('xerox', *args)




