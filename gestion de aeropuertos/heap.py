CAP_INICIAL = 10
REDIMENSION = 2

class Heap:
    def __init__(self, cmp):
        self.cantidad = 0
        self.datos = []
        self.cmp = cmp

    def encolar(self, dato):
        self.datos.append(dato)
        self.up_heap(len(self.datos)-1)
        self.cantidad += 1

    def desencolar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        dato = self.datos[0]
        self.cantidad -= 1
        self.datos[0] = self.datos[self.cantidad]
        self.down_heap(0)
        return dato

    def ver_max(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.datos[0]

    def cantidad(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0

    def up_heap(self, posicion):
        padre = self.padre(posicion)
        if padre < 0 or padre > self.cantidad - 1:
            return
        if self.cmp(self.datos[posicion], self.datos[padre]) > 0:
            self.datos[posicion], self.datos[padre] = self.datos[padre], self.datos[posicion]
            self.up_heap(padre)

    def down_heap(self, posicion):
        hijo_max = self.devolver_max(self.hijo_izq(posicion), self.hijo_der(posicion))
        if hijo_max < self.cantidad and self.cmp(self.datos[posicion], self.datos[hijo_max]) < 0:
            self.datos[posicion], self.datos[hijo_max] = self.datos[hijo_max], self.datos[posicion]
            self.down_heap(hijo_max)

    def heapify(self):
        primero_con_hijos = self.primero_con_hijos(self.cantidad)
        for i in range(primero_con_hijos, -1, -1):
            self.down_heap(i)

    def swap(self, pos1, pos2):
        self.datos[pos1], self.datos[pos2] = self.datos[pos2], self.datos[pos1]

    def devolver_max(self, hijo_izq, hijo_der):
        if hijo_der < self.cantidad:
            if hijo_izq < self.cantidad and self.cmp(self.datos[hijo_izq], self.datos[hijo_der]) > 0:
                return hijo_izq
        elif hijo_izq < self.cantidad:
            return hijo_izq
        return hijo_der

    def primero_con_hijos(self, i):
        return (i // 2) - 1

    def hijo_izq(self, i):
        return (2 * i) + 1

    def hijo_der(self, i):
        return (2 * i) + 2

    def padre(self, i):
        return (i - 1) // 2

def crear_heap_arr(arr, cmp):
    heap = Heap(cmp)
    heap.datos = arr.copy()
    heap.cantidad = len(arr)
    heap.heapify()
    return heap

def heap_sort(arr, cmp):
    heap = Heap(cmp)
    heap.datos = arr.copy()
    heap.cantidad = len(arr)
    heap.heapify()
    for i in range(len(arr) - 1, -1, -1):
        heap.swap(0, i)
        heap.cantidad -= 1
        heap.down_heap(0)
    return heap.datos
