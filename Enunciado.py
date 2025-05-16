# Juego "Radar del Tesoro"
MapaTesoro = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]

def VerificarTesoro(mapa: list, x: int, y: int) -> int:
        """
        Verifica las coordenadas que ingresó el usuario para encontrar el tesoro dentro del mapa
        Si lo encontró, devuelve 0
        De lo contario, devuelve otro número

        Parámetros:
        mapa:list = Una lista que contiene dígitos binarios
        x: int = un entero que se usará como coordenada de fila
        x: int = un entero que se usará como coordenada de columna
        """
        if mapa[CoordenadaFila][CoordenadaColumna] == 1:
            Resultado = 0
        else:
            Manhattan = (x - 1) + (y - 3)
            Resultado = Manhattan
        if Resultado == 0:
            print("\n¡Encontraste el tesoro!\n")
        else:
            print(f"\nFallaste. El tesoro está a {Resultado} casilleros de distancia.\n" )
        return Resultado

while True:
    CoordenadaFila = int(input("Porfavor, ingrese la coordenada de una fila (desde 0 hasta 4)\n"))
    CoordenadaColumna = int(input("Porfavor, ingrese la coordenada de una columna (desde 0 hasta 4)\n"))
    if VerificarTesoro(MapaTesoro, CoordenadaFila, CoordenadaColumna) != 0:
        Continuar = input("No ha encontrado el tesoro. ¿Desea continuar jugando? (S/N)\n").upper()
        if Continuar not in ["S", "N"]:
            print("La opción ingresada es inválida. Vuelva a iniciar el programa.\n")
        elif Continuar == "N":
            print("Ha decidido dejar de jugar.\n")
            break
    else:
        break