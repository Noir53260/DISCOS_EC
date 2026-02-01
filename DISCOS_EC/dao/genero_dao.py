from dao.base_dao import BaseDAO

class GeneroDAO(BaseDAO):

    def obtener_todos(self):
        return self._run(
            "SELECT id, nombre, activo FROM genero ORDER BY nombre"
        )

    def buscar_por_id(self, id_):
        return self._run(
            "SELECT id, nombre, activo FROM genero WHERE id=%s",
            (id_,),
            one=True
        )

    def crear(self, genero):
        row = self._run(
            "INSERT INTO genero (nombre, activo) VALUES (%s,%s) RETURNING id",
            (genero.nombre, genero.activo),
            one=True,
            commit=True
        )
        return row["id"] if row else None

    def actualizar(self, id_, genero):
        self._run(
            "UPDATE genero SET nombre=%s, activo=%s WHERE id=%s",
            (genero.nombre, genero.activo, id_),
            commit=True
        )

    def eliminar(self, id_):
        self._run(
            "DELETE FROM genero WHERE id=%s",
            (id_,),
            commit=True
        )