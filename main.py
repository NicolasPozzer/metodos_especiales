#Los metodos especiales o "Dunder Method" arrancan con des __ y terminan con __ ej. __init__

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #Metodo especial como el ToString en java.
    def __str__(self):
        return f'Persona(nombre={self.nombre},edad={self.edad})'

    """def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'"""


persona = Persona("Nicolas",24)
repre = repr(persona)


#Con solo llamar al objeto ya nos devuelve el objeto con sus datos,
# si no tuvieramos el __str__ nos devolveria la posicion en memoria.
print(persona)
