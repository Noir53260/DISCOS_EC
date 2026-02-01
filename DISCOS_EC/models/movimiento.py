from models.base import BaseModel

class Movimiento(BaseModel):
    def __init__(self, tipo, disco_id, cantidad, sucursal_origen_id=None, sucursal_destino_id=None, detalle="", id=None):
        super().__init__(id)
        self._tipo = ""
        self._disco_id = 0
        self._cantidad = 0
        self._sucursal_origen_id = sucursal_origen_id
        self._sucursal_destino_id = sucursal_destino_id
        self._detalle = ""

        self.tipo = tipo
        self.disco_id = disco_id
        self.cantidad = cantidad
        self.sucursal_origen_id = sucursal_origen_id
        self.sucursal_destino_id = sucursal_destino_id
        self.detalle = detalle

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        value = (value or "").strip().upper()
        if value not in ("ENTRADA", "SALIDA", "TRASLADO"):
            raise ValueError("tipo inválido")
        self._tipo = value

    @property
    def disco_id(self):
        return self._disco_id

    @disco_id.setter
    def disco_id(self, value):
        value = int(value)
        if value <= 0:
            raise ValueError("disco inválido")
        self._disco_id = value

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value):
        value = int(value)
        if value <= 0:
            raise ValueError("cantidad inválida")
        self._cantidad = value

    @property
    def sucursal_origen_id(self):
        return self._sucursal_origen_id

    @sucursal_origen_id.setter
    def sucursal_origen_id(self, value):
        self._sucursal_origen_id = None if value in (None, "", "0") else int(value)

    @property
    def sucursal_destino_id(self):
        return self._sucursal_destino_id

    @sucursal_destino_id.setter
    def sucursal_destino_id(self, value):
        self._sucursal_destino_id = None if value in (None, "", "0") else int(value)

    @property
    def detalle(self):
        return self._detalle

    @detalle.setter
    def detalle(self, value):
        self._detalle = (value or "").strip()

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "disco_id": self.disco_id,
            "cantidad": self.cantidad,
            "sucursal_origen_id": self.sucursal_origen_id,
            "sucursal_destino_id": self.sucursal_destino_id,
            "detalle": self.detalle
        }
