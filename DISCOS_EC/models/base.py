from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self, id=None):
        self._id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is not None and int(value) <= 0:
            raise ValueError("id inválido")
        self._id = value

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError
