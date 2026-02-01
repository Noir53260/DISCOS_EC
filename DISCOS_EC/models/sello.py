from models.base import BaseModel

class Sello(BaseModel):
    def __init__(self, nombre, id=None, activo=True):
        super().__init__(id)
        self._nombre = ""
        self._activo = True
        self.nombre = nombre
        self.activo = activo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        value = (value or "").strip()
        if len(value) < 2:
            raise ValueError("nombre de sello muy corto")
        self._nombre = value

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, value):
        self._activo = bool(value)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "activo": self.activo}
