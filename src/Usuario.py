class Usuario:
    def __init__(self, nombre: str, peso: float):
        self.__nombre = nombre
        self.__peso = peso

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def peso(self) -> float:
        return self.__peso

    def actualizar_peso(self, nuevo_peso: float) -> None:
        # Aca la corrección, self.__peso = nuevo_peso y no restar 1kg
        self.__peso = nuevo_peso 

    def mostrar_informacion(self) -> None:
        print(f"Usuario: {self.__nombre}, Peso Actual: {self.__peso} kg")


"""# Ejemplo de uso
if __name__ == "__main__":
    # Crear un usuario
    usuario1 = Usuario("María", 65.3)
    
    # Mostrar información inicial
    usuario1.mostrar_informacion()  # Usuario: María, Peso Actual: 65.3 kg
    
    # Actualizar peso (con el error)
    usuario1.actualizar_peso(64.0)
    usuario1.mostrar_informacion()  # Usuario: María, Peso Actual: 64.3 kg (debería ser 64.0)
    
    # Crear otro usuario
    usuario2 = Usuario("Carlos", 80.5)
    usuario2.mostrar_informacion()  # Usuario: Carlos, Peso Actual: 80.5 kg
    
    # Intentar actualizar peso
    usuario2.actualizar_peso(78.0)
    usuario2.mostrar_informacion()  # Usuario: Carlos, Peso Actual: 79.5 kg (debería ser 78.0)
Características importantes:"""