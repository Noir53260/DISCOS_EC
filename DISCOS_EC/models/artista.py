from models.base import BaseModel

class Artista(BaseModel):
    def __init__(self, nombre, provincia_origen="Desconocida", id=None, activo=True):
        super().__init__(id)
        self._nombre = ""
        self._provincia_origen = ""
        self._activo = True
        self.nombre = nombre
        self.provincia_origen = provincia_origen
        self.activo = activo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        value = (value or "").strip()
        if len(value) < 2:
            raise ValueError("nombre de artista muy corto")
        self._nombre = value

    @property
    def provincia_origen(self):
        return self._provincia_origen

    @provincia_origen.setter
    def provincia_origen(self, value):
        value = (value or "").strip()
        if len(value) < 2:
            raise ValueError("provincia inválida")
        self._provincia_origen = value

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, value):
        self._activo = bool(value)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "provincia_origen": self.provincia_origen, "activo": self.activo}
