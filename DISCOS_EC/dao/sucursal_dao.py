from dao.base_dao import BaseDAO

class SucursalDAO(BaseDAO):

    def obtener_todos(self):
        return self._run(
            "SELECT id, nombre, ciudad, activo FROM sucursal ORDER BY nombre"
        )

    def buscar_por_id(self, id_):
        return self._run(
            "SELECT id, nombre, ciudad, activo FROM sucursal WHERE id=%s",
            (id_,),
            one=True
        )

    def crear(self, sucursal):
        row = self._run(
            "INSERT INTO sucursal (nombre, ciudad, activo) VALUES (%s,%s,%s) RETURNING id",
            (sucursal.nombre, sucursal.ciudad, sucursal.activo),
            one=True,
            commit=True
        )
        return row["id"] if row else None

    def actualizar(self, id_, sucursal):
        self._run(
            "UPDATE sucursal SET nombre=%s, ciudad=%s, activo=%s WHERE id=%s",
            (sucursal.nombre, sucursal.ciudad, sucursal.activo, id_),
            commit=True
        )

    def eliminar(self, id_):
        self._run(
            "DELETE FROM sucursal WHERE id=%s",
            (id_,),
            commit=True
        )