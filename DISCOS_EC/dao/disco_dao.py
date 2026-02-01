from dao.base_dao import BaseDAO

class DiscoDAO(BaseDAO):

    def obtener_todos(self):
        return self._run("""
            SELECT d.id, d.titulo, d.precio, d.stock_total, d.activo,
                   a.nombre AS artista,
                   g.nombre AS genero,
                   s.nombre AS sello,
                   d.artista_id, d.genero_id, d.sello_id
            FROM disco d
            JOIN artista a ON a.id=d.artista_id
            JOIN genero g ON g.id=d.genero_id
            JOIN sello s ON s.id=d.sello_id
            ORDER BY d.titulo
        """)

    def buscar_por_id(self, id_):
        return self._run(
            "SELECT * FROM disco WHERE id=%s",
            (id_,),
            one=True
        )

    def crear(self, disco):
        row = self._run("""
            INSERT INTO disco (titulo, artista_id, genero_id, sello_id, precio, stock_total, activo)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
            RETURNING id
        """, (
            disco.titulo,
            disco.artista_id,
            disco.genero_id,
            disco.sello_id,
            disco.precio,
            disco.stock_total,
            disco.activo
        ), one=True, commit=True)
        return row["id"] if row else None

    def actualizar(self, id_, disco):
        self._run("""
            UPDATE disco
            SET titulo=%s,
                artista_id=%s,
                genero_id=%s,
                sello_id=%s,
                precio=%s,
                stock_total=%s,
                activo=%s
            WHERE id=%s
        """, (
            disco.titulo,
            disco.artista_id,
            disco.genero_id,
            disco.sello_id,
            disco.precio,
            disco.stock_total,
            disco.activo,
            id_
        ), commit=True)

    def eliminar(self, id_):
        self._run(
            "DELETE FROM disco WHERE id=%s",
            (id_,),
            commit=True
        )