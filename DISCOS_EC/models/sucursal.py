from models.base import BaseModel

class Disco(BaseModel):
    def __init__(self, titulo, artista_id, genero_id, sello_id, precio, stock_total=0, id=None, activo=True):
        super().__init__(id)
        self._titulo = ""
        self._artista_id = 0
        self._genero_id = 0
        self._sello_id = 0
        self._precio = 0.0
        self._stock_total = 0
        self._activo = True

        self.titulo = titulo
        self.artista_id = artista_id
        self.genero_id = genero_id
        self.sello_id = sello_id
        self.precio = precio
        self.stock_total = stock_total
        self.activo = activo

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        value = (value or "").strip()
        if len(value) < 2:
            raise ValueError("título muy corto")
        self._titulo = value

    @property
    def artista_id(self):
        return self._artista_id

    @artista_id.setter
    def artista_id(self, value):
        value = int(value)
        if value <= 0:
            raise ValueError("artista inválido")
        self._artista_id = value

    @property
    def genero_id(self):
        return self._genero_id

    @genero_id.setter
    def genero_id(self, value):
        value = int(value)
        if value <= 0:
            raise ValueError("género inválido")
        self._genero_id = value

    @property
    def sello_id(self):
        return self._sello_id

    @sello_id.setter
    def sello_id(self, value):
        value = int(value)
        if value <= 0:
            raise ValueError("sello inválido")
        self._sello_id = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        value = float(value)
        if value < 0:
            raise ValueError("precio inválido")
        self._precio = value

    @property
    def stock_total(self):
        return self._stock_total

    @stock_total.setter
    def stock_total(self, value):
        value = int(value)
        if value < 0:
            raise ValueError("stock inválido")
        self._stock_total = value

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, value):
        self._activo = bool(value)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "artista_id": self.artista_id,
            "genero_id": self.genero_id,
            "sello_id": self.sello_id,
            "precio": self.precio,
            "stock_total": self.stock_total,
            "activo": self.activo
        }

from models.base import BaseModel

class Sucursal(BaseModel):
    def __init__(self, nombre, ciudad, id=None, activo=True):
        super().__init__(id)
        self._nombre = ""
        self._ciudad = ""
        self._activo = True
        self.nombre = nombre
        self.ciudad = ciudad
        self.activo = activo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        value = (value or "").strip()
        if len(value) < 2:
            raise ValueError("nombre inválido")
        self._nombre = value

    @property
    def ciudad(self):
        return self._ciudad

    @ciudad.setter
    def ciudad(self, value):
        value = (value or "").strip()
        if len(value) < 2:
            raise ValueError("ciudad inválida")
        self._ciudad = value

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, value):
        self._activo = bool(value)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "ciudad": self.ciudad,
            "activo": self.activo
        }
