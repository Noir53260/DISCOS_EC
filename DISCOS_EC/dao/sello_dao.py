from dao.base_dao import BaseDAO

class SelloDAO(BaseDAO):

    def obtener_todos(self):
        return self._run(
            "SELECT id, nombre, activo FROM sello ORDER BY nombre"
        )

    def buscar_por_id(self, id_):
        return self._run(
            "SELECT id, nombre, activo FROM sello WHERE id=%s",
            (id_,),
            one=True
        )

    def crear(self, sello):
        row = self._run(
            "INSERT INTO sello (nombre, activo) VALUES (%s,%s) RETURNING id",
            (sello.nombre, sello.activo),
            one=True,
            commit=True
        )
        return row["id"] if row else None

    def actualizar(self, id_, sello):
        self._run(
            "UPDATE sello SET nombre=%s, activo=%s WHERE id=%s",
            (sello.nombre, sello.activo, id_),
            commit=True
        )

    def eliminar(self, id_):
        self._run(
            "DELETE FROM sello WHERE id=%s",
            (id_,),
            commit=True
        )