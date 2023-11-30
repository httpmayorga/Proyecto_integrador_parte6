import os
import readchar
import random
import time

class Juego:
    def __init__(self, filename):
        self.PARED = "#"
        self.CAMINO = "."
        self.JUGADOR = "P"
        self.px = 0
        self.py = 0
        self.laberinto, self.ancho, self.alto, self.px, self.py = self.cargar_laberinto(filename)
        self.META = (self.ancho , self.alto)

    def cargar_laberinto(self, filename):
        with open(filename, "r") as f:
            px, py, ancho, alto = map(int, f.readline().strip().split())
            laberinto = list(map(list, map(str.strip, f.readlines())))

        return laberinto, ancho, alto, px, py

    def imprimir_laberinto(self):
        for fila in self.laberinto:
            print(" ".join(fila))
    
    def obtener_posicion_meta(self):
        return self.META
    
    def obtener_datos_mapa(self):
        datos_mapa = ""
        for fila in self.laberinto:
            datos_mapa += "".join(fila) + "\n"

        return datos_mapa.strip()
    
    def obtener_dimensiones(self):
        return self.ancho, self.alto
                  
    def colocar_jugador(self, x, y, dx, dy):
        ancho_laberinto = self.ancho + 1
        alto_laberinto = self.alto + 1
        
        if x + dx < 0 or x + dx >= ancho_laberinto or y + dy < 0 or y + dy >= alto_laberinto:
            return
        
        if (x + dx, y + dy) == self.obtener_posicion_meta():
            print("Felicidades, ganaste")
            exit()
        
        if self.laberinto[y + dy][x + dx] == self.CAMINO:
            self.laberinto[y][x] = self.CAMINO
            self.laberinto[y + dy][x + dx] = self.JUGADOR
            self.px = x + dx
            self.py = y + dy
        
    def ejecutar(self):
    
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            self.imprimir_laberinto()
          
            tecla = readchar.readkey()

            if tecla == "q":
                break
            elif tecla.lower() == "a" or tecla == readchar.key.LEFT:
                self.colocar_jugador(self.px, self.py, -1, 0)
            elif tecla.lower() == "s" or tecla == readchar.key.DOWN:
                self.colocar_jugador(self.px, self.py, 0, 1)
            elif tecla.lower() == "d" or tecla == readchar.key.RIGHT:
                self.colocar_jugador(self.px, self.py, 1, 0)
            elif tecla.lower() == "w" or tecla == readchar.key.UP:
                self.colocar_jugador(self.px, self.py, 0, -1)

class JuegoArchivos(Juego):
    def __init__(self, nombres_archivos):
        nombre_archivo_seleccionado = random.choice(nombres_archivos)
        super().__init__(nombre_archivo_seleccionado)
        
def principal():
    juego = JuegoArchivos(["map1.txt", "map2.txt"])
    juego.ejecutar()

if __name__ == "__main__":
    principal()
