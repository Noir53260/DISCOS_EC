from collections import deque
import math

class GrafoNoDirigido:
    def __init__(self):
        self._ady = {}

    def agregar_nodo(self, nodo):
        if nodo not in self._ady:
            self._ady[nodo] = {}

    def agregar_arista(self, a, b, peso=1):
        self.agregar_nodo(a)
        self.agregar_nodo(b)
        peso = float(peso)
        self._ady[a][b] = peso
        self._ady[b][a] = peso

    def nodos(self):
        return list(self._ady.keys())

    def bfs(self, inicio):
        if inicio not in self._ady:
            return []
        visitado = set([inicio])
        cola = deque([inicio])
        orden = []
        while cola:
            u = cola.popleft()
            orden.append(u)
            for v in self._ady[u].keys():
                if v not in visitado:
                    visitado.add(v)
                    cola.append(v)
        return orden

    def dijkstra(self, inicio, fin):
        if inicio not in self._ady or fin not in self._ady:
            return (math.inf, [])

        dist = {n: math.inf for n in self._ady}
        prev = {n: None for n in self._ady}
        dist[inicio] = 0

        pendientes = set(self._ady.keys())

        while pendientes:
            u = min(pendientes, key=lambda n: dist[n])
            pendientes.remove(u)

            if dist[u] == math.inf:
                break
            if u == fin:
                break

            for v, w in self._ady[u].items():
                if v in pendientes:
                    alt = dist[u] + w
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u

        camino = []
        actual = fin
        pila = []
        while actual is not None:
            pila.append(actual)
            actual = prev[actual]
        while pila:
            camino.append(pila.pop())

        if camino and camino[0] == inicio and camino[-1] == fin:
            return (dist[fin], camino)

        return (math.inf, [])
