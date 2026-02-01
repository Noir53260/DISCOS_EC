from dao.disco_dao import DiscoDAO
from dao.movimiento_dao import MovimientoDAO

class InventarioService:
    def __init__(self):
        self._disco_dao = DiscoDAO()
        self._mov_dao = MovimientoDAO()

    def registrar_movimiento(self, mov):
        if mov.tipo == "ENTRADA":
            if mov.sucursal_destino_id is None:
                raise ValueError("ENTRADA necesita sucursal destino")
            self._disco_dao.ajustar_stock(mov.disco_id, mov.cantidad)

        elif mov.tipo == "SALIDA":
            if mov.sucursal_origen_id is None:
                raise ValueError("SALIDA necesita sucursal origen")
            self._disco_dao.ajustar_stock(mov.disco_id, -mov.cantidad)

        elif mov.tipo == "TRASLADO":
            if mov.sucursal_origen_id is None or mov.sucursal_destino_id is None:
                raise ValueError("TRASLADO necesita origen y destino")
            self._disco_dao.ajustar_stock(mov.disco_id, 0)

        return self._mov_dao.crear(mov)
