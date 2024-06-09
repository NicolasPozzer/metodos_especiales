#Los metodos especiales o "Dunder Method" arrancan con des __ y terminan con __ ej. __init__

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #Metodo especial como el ToString en java.
    def __str__(self):
        return f'Persona(nombre={self.nombre},edad={self.edad})'

    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'


    #Metodo de suma de valores de un objeto
    def __add__(self, other):
        nuevo_valor = self.edad + other.edad
        return Persona(self.nombre+other.nombre, nuevo_valor)


#Tests

persona = Persona("Nicolas",24)
persona2 = Persona("Pepito",44)

#Con solo llamar al objeto ya nos devuelve el objeto con sus datos,
# si no tuvieramos el __str__ nos devolveria la posicion en memoria.
print(persona)

#Esta linea de abajo suma las edades de las personas
resultado = persona + persona2

print(resultado)# Devolveria --> Persona(nombre=NicolasPepito,edad=68)
print(resultado.edad)# Devuelve solamente la edad de las personas sumadas


