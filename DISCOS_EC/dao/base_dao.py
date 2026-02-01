from db.conexion import get_conexion

class BaseDAO:

    def _run(self, sql, params=None, one=False, commit=False):
        con = get_conexion()
        cur = con.cursor()
        try:
            cur.execute(sql, params or ())
            result = None

            if one:
                result = cur.fetchone()
            elif not commit:
                result = cur.fetchall()

            if commit:
                con.commit()

            return result
        finally:
            cur.close()
            con.close()