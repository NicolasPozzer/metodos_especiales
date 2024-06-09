class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza},Velocidad: {self.velocidad})"

    #Funcion para fusionar los personajes
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza)/2) **2 #sumamos las fuerzas, la dividimos x2 y las elevamos
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad)/2) **2
        return  Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

goku = Personaje("Goku",100,100)
vegeta = Personaje("Vegeta",99,99)
gogeta = goku + vegeta #Fucionamos los objetos personajes

print(gogeta)