class Birthday(Field):
    def __init__(self, value=None):
        super().__init__(value)

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = Birthday(birthday) if birthday else None

    def days_to_birthday(self):
        if self.birthday:

            pass
        return None
class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        # Реалізація перевірки на коректність номера телефону
        if not self.is_valid_phone(new_value):
            raise ValueError("Некоректний номер телефону")
        self._value = new_value

    def is_valid_phone(self, phone):
        # Реалізація перевірки на коректність номера телефону
        pass

class Birthday(Field):
    def __init__(self, value=None):
        super().__init__(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        # Реалізація перевірки на коректність дня народження
        if not self.is_valid_birthday(new_value):
            raise ValueError("Некоректна дата народження")
        self._value = new_value

    def is_valid_birthday(self, birthday):
        # Реалізація перевірки на коректність дня народження
        pass
class AddressBook:
    def __init__(self, records=None):
        self.records = records or []

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self, n=5):
        if self.current_index < len(self.records):
            result = self.records[self.current_index:self.current_index + n]
            self.current_index += n
            return result
        else:
            raise StopIteration
