
# Comentario de prueba subido a GitHub (actualizado)
# SI VES ESTO ES EL ARCHIVO CORRECTO ✅
#Hola mundo
#confirmar que funciona 
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request, redirect

from dao.genero_dao import GeneroDAO
from dao.artista_dao import ArtistaDAO
from dao.sello_dao import SelloDAO
from dao.disco_dao import DiscoDAO
from dao.sucursal_dao import SucursalDAO
from dao.movimiento_dao import MovimientoDAO
from dao.reportes_dao import ReportesDAO

from models.genero import Genero
from models.artista import Artista
from models.sello import Sello
from models.disco import Disco
from models.sucursal import Sucursal
from models.movimiento import Movimiento

from services.inventario_service import InventarioService
from models.grafo_rutas import GrafoNoDirigido

app = Flask(__name__)

genero_dao = GeneroDAO()
artista_dao = ArtistaDAO()
sello_dao = SelloDAO()
disco_dao = DiscoDAO()
sucursal_dao = SucursalDAO()
mov_dao = MovimientoDAO()
rep_dao = ReportesDAO()
inv_service = InventarioService()

@app.get("/")
def index():
    return render_template("index.html", title="Inicio")

def _bool_form(v):
    return str(v) in ("1", "true", "True", "on", "yes", "SI", "si")

# -----------------------------
# GENEROS
# -----------------------------
@app.get("/generos")
def generos_list():
    try:
        generos = genero_dao.obtener_todos()
        return render_template("generos/list.html", title="Géneros", generos=generos, ok=request.args.get("ok"))
    except Exception as e:
        return render_template("generos/list.html", title="Géneros", generos=[], error=str(e))

@app.get("/generos/nuevo")
def genero_nuevo_form():
    return render_template("generos/form.html", title="Nuevo Género", genero=None)

@app.post("/generos/nuevo")
def genero_nuevo_post():
    try:
        g = Genero(nombre=request.form.get("nombre", ""), activo=_bool_form(request.form.get("activo", "1")))
        new_id = genero_dao.crear(g)
        return redirect(f"/generos?ok=Creado ID {new_id}")
    except Exception as e:
        return render_template("generos/form.html", title="Nuevo Género", genero=None, error=str(e))

@app.get("/generos/<int:id_>/editar")
def genero_editar_form(id_):
    gen = genero_dao.buscar_por_id(id_)
    if not gen:
        return redirect("/generos?ok=No existe")
    return render_template("generos/form.html", title="Editar Género", genero=gen)

@app.post("/generos/<int:id_>/editar")
def genero_editar_post(id_):
    try:
        g = Genero(nombre=request.form.get("nombre", ""), activo=_bool_form(request.form.get("activo", "1")), id=id_)
        genero_dao.actualizar(id_, g)
        return redirect("/generos?ok=Actualizado")
    except Exception as e:
        gen = {"id": id_, "nombre": request.form.get("nombre", ""), "activo": _bool_form(request.form.get("activo", "1"))}
        return render_template("generos/form.html", title="Editar Género", genero=gen, error=str(e))

@app.post("/generos/<int:id_>/eliminar")
def genero_eliminar_post(id_):
    try:
        genero_dao.eliminar(id_)
        return redirect("/generos?ok=Eliminado")
    except Exception as e:
        return redirect(f"/generos?ok=No se pudo eliminar")

# -----------------------------
# ARTISTAS
# -----------------------------
@app.get("/artistas")
def artistas_list():
    try:
        artistas = artista_dao.obtener_todos()
        return render_template("artistas/list.html", title="Artistas", artistas=artistas, ok=request.args.get("ok"))
    except Exception as e:
        return render_template("artistas/list.html", title="Artistas", artistas=[], error=str(e))

@app.get("/artistas/nuevo")
def artista_nuevo_form():
    return render_template("artistas/form.html", title="Nuevo Artista", artista=None)

@app.post("/artistas/nuevo")
def artista_nuevo_post():
    try:
        a = Artista(
            nombre=request.form.get("nombre", ""),
            provincia_origen=request.form.get("provincia_origen", "Desconocida"),
            activo=_bool_form(request.form.get("activo", "1"))
        )
        new_id = artista_dao.crear(a)
        return redirect(f"/artistas?ok=Creado ID {new_id}")
    except Exception as e:
        return render_template("artistas/form.html", title="Nuevo Artista", artista=None, error=str(e))

@app.get("/artistas/<int:id_>/editar")
def artista_editar_form(id_):
    art = artista_dao.buscar_por_id(id_)
    if not art:
        return redirect("/artistas?ok=No existe")
    return render_template("artistas/form.html", title="Editar Artista", artista=art)

@app.post("/artistas/<int:id_>/editar")
def artista_editar_post(id_):
    try:
        a = Artista(
            nombre=request.form.get("nombre", ""),
            provincia_origen=request.form.get("provincia_origen", "Desconocida"),
            activo=_bool_form(request.form.get("activo", "1")),
            id=id_
        )
        artista_dao.actualizar(id_, a)
        return redirect("/artistas?ok=Actualizado")
    except Exception as e:
        art = {
            "id": id_,
            "nombre": request.form.get("nombre", ""),
            "provincia_origen": request.form.get("provincia_origen", "Desconocida"),
            "activo": _bool_form(request.form.get("activo", "1"))
        }
        return render_template("artistas/form.html", title="Editar Artista", artista=art, error=str(e))

@app.post("/artistas/<int:id_>/eliminar")
def artista_eliminar_post(id_):
    try:
        artista_dao.eliminar(id_)
        return redirect("/artistas?ok=Eliminado")
    except Exception as e:
        return redirect(f"/artistas?ok=No se pudo eliminar")

# -----------------------------
# SELLOS
# -----------------------------
@app.get("/sellos")
def sellos_list():
    try:
        sellos = sello_dao.obtener_todos()
        return render_template("sellos/list.html", title="Sellos", sellos=sellos, ok=request.args.get("ok"))
    except Exception as e:
        return render_template("sellos/list.html", title="Sellos", sellos=[], error=str(e))

@app.get("/sellos/nuevo")
def sello_nuevo_form():
    return render_template("sellos/form.html", title="Nuevo Sello", sello=None)

@app.post("/sellos/nuevo")
def sello_nuevo_post():
    try:
        s = Sello(nombre=request.form.get("nombre", ""), activo=_bool_form(request.form.get("activo", "1")))
        new_id = sello_dao.crear(s)
        return redirect(f"/sellos?ok=Creado ID {new_id}")
    except Exception as e:
        return render_template("sellos/form.html", title="Nuevo Sello", sello=None, error=str(e))

@app.get("/sellos/<int:id_>/editar")
def sello_editar_form(id_):
    sel = sello_dao.buscar_por_id(id_)
    if not sel:
        return redirect("/sellos?ok=No existe")
    return render_template("sellos/form.html", title="Editar Sello", sello=sel)

@app.post("/sellos/<int:id_>/editar")
def sello_editar_post(id_):
    try:
        s = Sello(nombre=request.form.get("nombre", ""), activo=_bool_form(request.form.get("activo", "1")), id=id_)
        sello_dao.actualizar(id_, s)
        return redirect("/sellos?ok=Actualizado")
    except Exception as e:
        sel = {"id": id_, "nombre": request.form.get("nombre", ""), "activo": _bool_form(request.form.get("activo", "1"))}
        return render_template("sellos/form.html", title="Editar Sello", sello=sel, error=str(e))

@app.post("/sellos/<int:id_>/eliminar")
def sello_eliminar_post(id_):
    try:
        sello_dao.eliminar(id_)
        return redirect("/sellos?ok=Eliminado")
    except Exception as e:
        return redirect(f"/sellos?ok=No se pudo eliminar")

# -----------------------------
# DISCOS
# -----------------------------
@app.get("/discos")
def discos_list():
    try:
        discos = disco_dao.obtener_todos()
        return render_template("discos/list.html", title="Discos", discos=discos, ok=request.args.get("ok"))
    except Exception as e:
        return render_template("discos/list.html", title="Discos", discos=[], error=str(e))

@app.get("/discos/nuevo")
def disco_nuevo_form():
    return render_template(
        "discos/form.html",
        title="Nuevo Disco",
        disco=None,
        artistas=artista_dao.obtener_todos(),
        generos=genero_dao.obtener_todos(),
        sellos=sello_dao.obtener_todos()
    )

@app.post("/discos/nuevo")
def disco_nuevo_post():
    try:
        d = Disco(
            titulo=request.form.get("titulo", ""),
            artista_id=request.form.get("artista_id", "0"),
            genero_id=request.form.get("genero_id", "0"),
            sello_id=request.form.get("sello_id", "0"),
            precio=request.form.get("precio", "0"),
            stock_total=request.form.get("stock_total", "0"),
            activo=_bool_form(request.form.get("activo", "1"))
        )
        new_id = disco_dao.crear(d)
        return redirect(f"/discos?ok=Creado ID {new_id}")
    except Exception as e:
        return render_template(
            "discos/form.html",
            title="Nuevo Disco",
            disco=None,
            artistas=artista_dao.obtener_todos(),
            generos=genero_dao.obtener_todos(),
            sellos=sello_dao.obtener_todos(),
            error=str(e)
        )

@app.get("/discos/<int:id_>/editar")
def disco_editar_form(id_):
    d = disco_dao.buscar_por_id(id_)
    if not d:
        return redirect("/discos?ok=No existe")
    return render_template(
        "discos/form.html",
        title="Editar Disco",
        disco=d,
        artistas=artista_dao.obtener_todos(),
        generos=genero_dao.obtener_todos(),
        sellos=sello_dao.obtener_todos()
    )

@app.post("/discos/<int:id_>/editar")
def disco_editar_post(id_):
    try:
        d = Disco(
            titulo=request.form.get("titulo", ""),
            artista_id=request.form.get("artista_id", "0"),
            genero_id=request.form.get("genero_id", "0"),
            sello_id=request.form.get("sello_id", "0"),
            precio=request.form.get("precio", "0"),
            stock_total=request.form.get("stock_total", "0"),
            activo=_bool_form(request.form.get("activo", "1")),
            id=id_
        )
        disco_dao.actualizar(id_, d)
        return redirect("/discos?ok=Actualizado")
    except Exception as e:
        disco_form = {
            "id": id_,
            "titulo": request.form.get("titulo", ""),
            "artista_id": int(request.form.get("artista_id", "0") or 0),
            "genero_id": int(request.form.get("genero_id", "0") or 0),
            "sello_id": int(request.form.get("sello_id", "0") or 0),
            "precio": request.form.get("precio", "0"),
            "stock_total": request.form.get("stock_total", "0"),
            "activo": _bool_form(request.form.get("activo", "1"))
        }
        return render_template(
            "discos/form.html",
            title="Editar Disco",
            disco=disco_form,
            artistas=artista_dao.obtener_todos(),
            generos=genero_dao.obtener_todos(),
            sellos=sello_dao.obtener_todos(),
            error=str(e)
        )

@app.post("/discos/<int:id_>/eliminar")
def disco_eliminar_post(id_):
    try:
        disco_dao.eliminar(id_)
        return redirect("/discos?ok=Eliminado")
    except Exception as e:
        return redirect(f"/discos?ok=No se pudo eliminar")

# -----------------------------
# SUCURSALES
# -----------------------------
@app.get("/sucursales")
def sucursales_list():
    try:
        sucursales = sucursal_dao.obtener_todos()
        return render_template("sucursales/list.html", title="Sucursales", sucursales=sucursales, ok=request.args.get("ok"))
    except Exception as e:
        return render_template("sucursales/list.html", title="Sucursales", sucursales=[], error=str(e))

@app.get("/sucursales/nuevo")
def sucursal_nuevo_form():
    return render_template("sucursales/form.html", title="Nueva Sucursal", sucursal=None)

@app.post("/sucursales/nuevo")
def sucursal_nuevo_post():
    try:
        s = Sucursal(nombre=request.form.get("nombre", ""), ciudad=request.form.get("ciudad", ""), activo=_bool_form(request.form.get("activo", "1")))
        new_id = sucursal_dao.crear(s)
        return redirect(f"/sucursales?ok=Creado ID {new_id}")
    except Exception as e:
        return render_template("sucursales/form.html", title="Nueva Sucursal", sucursal=None, error=str(e))

@app.get("/sucursales/<int:id_>/editar")
def sucursal_editar_form(id_):
    s = sucursal_dao.buscar_por_id(id_)
    if not s:
        return redirect("/sucursales?ok=No existe")
    return render_template("sucursales/form.html", title="Editar Sucursal", sucursal=s)

@app.post("/sucursales/<int:id_>/editar")
def sucursal_editar_post(id_):
    try:
        s = Sucursal(nombre=request.form.get("nombre", ""), ciudad=request.form.get("ciudad", ""), activo=_bool_form(request.form.get("activo", "1")), id=id_)
        sucursal_dao.actualizar(id_, s)
        return redirect("/sucursales?ok=Actualizado")
    except Exception as e:
        s_form = {"id": id_, "nombre": request.form.get("nombre", ""), "ciudad": request.form.get("ciudad", ""), "activo": _bool_form(request.form.get("activo", "1"))}
        return render_template("sucursales/form.html", title="Editar Sucursal", sucursal=s_form, error=str(e))

@app.post("/sucursales/<int:id_>/eliminar")
def sucursal_eliminar_post(id_):
    try:
        sucursal_dao.eliminar(id_)
        return redirect("/sucursales?ok=Eliminado")
    except Exception as e:
        return redirect(f"/sucursales?ok=No se pudo eliminar")

# -----------------------------
# MOVIMIENTOS + SERVICE
# -----------------------------
@app.get("/movimientos")
def movimientos_list():
    try:
        movimientos = mov_dao.obtener_todos()
        return render_template("movimientos/list.html", title="Movimientos", movimientos=movimientos, ok=request.args.get("ok"))
    except Exception as e:
        return render_template("movimientos/list.html", title="Movimientos", movimientos=[], error=str(e))

@app.get("/movimientos/nuevo")
def movimiento_nuevo_form():
    return render_template(
        "movimientos/form.html",
        title="Nuevo Movimiento",
        mov=None,
        discos=disco_dao.obtener_todos(),
        sucursales=sucursal_dao.obtener_todos()
    )

@app.post("/movimientos/nuevo")
def movimiento_nuevo_post():
    try:
        mov = Movimiento(
            tipo=request.form.get("tipo", ""),
            disco_id=request.form.get("disco_id", "0"),
            cantidad=request.form.get("cantidad", "0"),
            sucursal_origen_id=request.form.get("sucursal_origen_id"),
            sucursal_destino_id=request.form.get("sucursal_destino_id"),
            detalle=request.form.get("detalle", "")
        )
        new_id = inv_service.registrar_movimiento(mov)
        return redirect(f"/movimientos?ok=Registrado ID {new_id}")
    except Exception as e:
        return render_template(
            "movimientos/form.html",
            title="Nuevo Movimiento",
            mov=None,
            discos=disco_dao.obtener_todos(),
            sucursales=sucursal_dao.obtener_todos(),
            error=str(e)
        )

# -----------------------------
# REPORTES
# -----------------------------
@app.get("/reportes")
def reportes_dashboard():
    try:
        kpis = rep_dao.kpis()
        por_genero = rep_dao.stock_por_genero()
        top_artistas = rep_dao.top_artistas_por_stock()
        return render_template("reportes/dashboard.html", title="Reportes", kpis=kpis, por_genero=por_genero, top_artistas=top_artistas)
    except Exception as e:
        return render_template("reportes/dashboard.html", title="Reportes", kpis=None, por_genero=[], top_artistas=[], error=str(e))

# -----------------------------
# RUTAS (GRAFO)
# -----------------------------
def _grafo_demo():
    g = GrafoNoDirigido()
    g.agregar_arista("Quito", "Cuenca", 7)
    g.agregar_arista("Quito", "Loja", 10)
    g.agregar_arista("Guayaquil", "Cuenca", 4)
    g.agregar_arista("Cuenca", "Loja", 3)
    g.agregar_arista("Guayaquil", "Quito", 8)
    return g

@app.get("/rutas")
def rutas_view():
    g = _grafo_demo()
    origen = request.args.get("origen", "Quito")
    destino = request.args.get("destino", "Loja")

    bfs = g.bfs(origen)
    dist, camino = g.dijkstra(origen, destino)
    dist_txt = "No disponible" if dist == float("inf") else str(dist)

    return render_template(
        "rutas/grafo.html",
        title="Rutas",
        nodos=g.nodos(),
        origen=origen,
        destino=destino,
        bfs=bfs,
        dist=dist_txt,
        camino=camino
    )

if __name__ == "__main__":
    app.run(debug=True)

