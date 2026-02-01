from dao.base_dao import BaseDAO

class ReportesDAO(BaseDAO):
    def obtener_todos(self):
        return []

    def kpis(self):
        return self._run("""
            SELECT
              (SELECT COUNT(*) FROM disco) AS total_discos,
              (SELECT COUNT(*) FROM artista) AS total_artistas,
              (SELECT COALESCE(SUM(stock_total),0) FROM disco) AS unidades_totales,
              (SELECT COALESCE(AVG(precio),0) FROM disco) AS precio_promedio
        """, one=True)

    def stock_por_genero(self):
        return self._run("""
            SELECT g.nombre AS genero, COALESCE(SUM(d.stock_total),0) AS unidades
            FROM genero g
            LEFT JOIN disco d ON d.genero_id=g.id
            GROUP BY g.nombre
            ORDER BY unidades DESC, genero ASC
        """)

    def top_artistas_por_stock(self):
        return self._run("""
            SELECT a.nombre AS artista, COALESCE(SUM(d.stock_total),0) AS unidades
            FROM artista a
            LEFT JOIN disco d ON d.artista_id=a.id
            GROUP BY a.nombre
            ORDER BY unidades DESC, artista ASC
            LIMIT 7
        """)
