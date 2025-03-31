class vuelo:
    def __init__(self, tiempo, precio, cant_vuelos):
        self.tiempo = int(tiempo)
        self.precio = int(precio)
        self.cant_vuelos = int(cant_vuelos)

    def ver_tiempo(self):
        return self.tiempo
    
    def ver_precio(self):
        return self.precio

    def ver_cant_vuelos(self):
        return self.cant_vuelos
    
class aeropuerto: 
    def __init__(self, ciudad, codigo, latitud, longitud):
        self.ciudad = ciudad
        self.codigo = codigo
        self.latitud = latitud
        self.longitud =  longitud

    def ver_ciudad(self):
        return self.ciudad

    def ver_codigo(self):
        return self.codigo
    
    def ver_latitud(self):
        return self.latitud
    
    def ver_longitud(self):
        return self.longitud
        
        