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
