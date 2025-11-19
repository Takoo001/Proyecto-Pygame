import pygame as pg

class Jugador:
    def __init__(self, posicion):
        self.vida = 100
        self.daño = 20
        self.posicion = posicion
        self.estado = "quieto"
        self.animaciones = {
            "quieto": self.cargar_sprite("Lautaro.png", 32, 32),
            "caminar": self.cargar_sprite("Lautaro_caminar.png", 32, 32)
        }
        self.frame = 0
        self.frame_timer = 0
        self.frame_velociad = 0.15

    def cargar_sprite(self, sprite, ancho, alto):
        imagen = pg.image.load(sprite).convert_alpha()
        frames = []
        ancho, alto = imagen.get_size
        #for i in range(imagen.get_)
