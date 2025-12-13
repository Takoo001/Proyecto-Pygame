import pygame as pg
import nivel_settings as ns

class Suelo(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sprite_suelo = pg.image.load("assets\sprites_suelo\suelo_cesped.png")
        self.lista_suelos = []

        for x in range(0, ns.ANCHO_NIVEL * 2, 64):
            self.lista_suelos.append(pg.Rect(x, ns.ALTO_NIVEL - 64, 64, 64))

    def dibujar_suelo(self, ventana):
        for suelo in self.lista_suelos:
            ventana.blit(self.sprite_suelo, suelo.topleft)
            #pg.draw.rect(ventana, (255, 0, 0), suelo, 1)