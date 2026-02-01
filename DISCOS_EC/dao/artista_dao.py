from dao.base_dao import BaseDAO

class ArtistaDAO(BaseDAO):

    def obtener_todos(self):
        return self._run(
            "SELECT id, nombre, provincia_origen, activo FROM artista ORDER BY nombre"
        )

    def buscar_por_id(self, id_):
        return self._run(
            "SELECT id, nombre, provincia_origen, activo FROM artista WHERE id=%s",
            (id_,),
            one=True
        )

    def crear(self, artista):
        row = self._run(
            "INSERT INTO artista (nombre, provincia_origen, activo) VALUES (%s,%s,%s) RETURNING id",
            (artista.nombre, artista.provincia_origen, artista.activo),
            one=True,
            commit=True
        )
        return row["id"] if row else None

    def actualizar(self, id_, artista):
        self._run(
            "UPDATE artista SET nombre=%s, provincia_origen=%s, activo=%s WHERE id=%s",
            (artista.nombre, artista.provincia_origen, artista.activo, id_),
            commit=True
        )

    def eliminar(self, id_):
        self._run(
            "DELETE FROM artista WHERE id=%s",
            (id_,),
            commit=True
        )