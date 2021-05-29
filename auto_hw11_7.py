class Customer:
    def __init__(self, surname, id=1):
        self.__surname = surname
        self.__id = id

    def __add__(self, b):
        return self.id + b.id

    def __repr__(self):
        return f'Customer("{self.surname}", {self.id})'

    def __str__(self):
        return f'customer id = {self.id} and surname is {self.surname}'

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def set_surname(self, surname):
        if len(surname) > 0:
            self.__surname = surname

    @property
    def id(self):
        return self.__id

    @id.setter
    def set_id(self, id):
        if id > 0:
            self.__id = id

    def __eq__(self, other):
       return self.__id == other.__id and self.__surname == other.__surname 

    def __ne__(self, other):
       return self.__id != other.__id or self.__surname != other.__surname  

    def __gt__(self, other):
       return self.__id > other.__id 

    def __lt__(self, other):
       return self.__id < other.__id   

    def __ge__(self, other):
        return self.__gt__(other)  or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other)  or self.__eq__(other)
