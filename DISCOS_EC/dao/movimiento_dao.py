from dao.base_dao import BaseDAO

class MovimientoDAO(BaseDAO):
    def obtener_todos(self):
        return self._run("""
            SELECT m.id, m.tipo, m.fecha, m.cantidad, m.detalle,
                   d.titulo AS disco,
                   so.nombre AS origen,
                   sd.nombre AS destino,
                   m.disco_id, m.sucursal_origen_id, m.sucursal_destino_id
            FROM movimiento m
            JOIN disco d ON d.id=m.disco_id
            LEFT JOIN sucursal so ON so.id=m.sucursal_origen_id
            LEFT JOIN sucursal sd ON sd.id=m.sucursal_destino_id
            ORDER BY m.fecha DESC, m.id DESC
        """)

    def crear(self, mov):
        row = self._run("""
            INSERT INTO movimiento (tipo, disco_id, cantidad, sucursal_origen_id, sucursal_destino_id, detalle)
            VALUES (%s,%s,%s,%s,%s,%s)
            RETURNING id
        """, (mov.tipo, mov.disco_id, mov.cantidad, mov.sucursal_origen_id, mov.sucursal_destino_id, mov.detalle), one=True)
        return row["id"] if row else None
