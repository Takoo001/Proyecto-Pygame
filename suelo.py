import pygame as pg
import nivel_settings as ns

class Suelo(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.suelo = pg.image.load("assets\sprites_suelo\suelo_cesped.png").convert_alpha()
        
        # Posición Hitbox
        self.x = x
        self.y = y
        self.rect = pg.Rect(self.x, self.y, 64, 64)

    def dibujar(self, ventana):
        ventana.blit(self.suelo, (self.x, self.y))
        pg.draw.rect(ventana, (255, 0, 0), self.rect, 1)

    def dibujar_suelo(self, suelo, ventana):
        for sprite in range(0, ns.ANCHO_NIVEL, 64):
            self.x = sprite
            # self.rect.x es solo para cambiar también el eje x del dibujo de la "hitbox" roja de los sprites
            self.rect.x = sprite
            suelo.dibujar(ventana)

    def obtener_posicion(self):
        return (self.rect.x, self.rect.y)
