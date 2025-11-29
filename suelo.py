import pygame as pg
import nivel_settings as ns

class Suelo(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.suelo = 1 #pg.image.load("assets\sprites_suelo\...").convert_alpha()
        
        # Posición Hitbox
        self.x = x
        self.y = y
        self.rect = pg.Rect(self.x, self.y, 64, 64)

    def dibujar(self, ventana):
        pg.draw.rect(ventana, (255, 0, 0), self.rect, 1)

    def obtener_posicion(self):
        return (self.rect.x, self.rect.y)
