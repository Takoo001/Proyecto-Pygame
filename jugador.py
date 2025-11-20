import pygame as pg

class Jugador(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.estadisticas = {
            "Vida": 100,
            "Daño": 20
        }
        self.quieto = pg.image.load("Lautaro.png")
        self.caminando = pg.image.load("Lautaro_caminando.png")
        self.x = x
        self.y = y
