import random 

class Grafo:
    def __init__(self, dirigido):
        self.vertices = {}
        self.dirigido = dirigido
    
    def agregar_vertice(self, v):
        self.vertices[v] = {}
    
    def agregar_arista(self, v, w, peso):
        if v in self.vertices and w in self.vertices:
            self.vertices[v][w] = peso
            if not self.dirigido:
                self.vertices[w][v] = peso
    
    def borrar_vertice(self, v):
        if v in self.vertices:
            del self.vertices[v]
            for _, adyacentes in self.vertices.items():
                if v in adyacentes:
                    adyacentes.pop(v, None)

    def borrar_arista(self, v, w):
        if v in self.vertices and w in self.vertices:
            self.vertices[v].pop(w, None)
            if not self.dirigido:
                self.vertices[w].pop(v, None)
    
    def estan_unidos(self, v, w):
        return w in self.vertices.get(v, {})
    
    def obtener_vertices(self):
        return list(self.vertices.keys())
    
    def obtener_aristas(self): 
        aristas = []
        for v in self.vertices:
            for w in self.adyacentes(v):   
                aristas.append((v, w, self.peso_arista(v, w)))
        return aristas
    
    def vertice_aleatorio(self):
        return random.choice(self.obtener_vertices())

    def adyacentes(self, v):
        return self.vertices.get(v, {})
    
    def peso_arista(self, v, w):
        return self.vertices.get(v, {}).get(w, None)

