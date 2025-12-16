import pygame as pg
import nivel_settings as ns

class Suelo(pg.sprite.Sprite):
    def __init__(self, largo_suelos):
        super().__init__()

        self.largo_suelos = largo_suelos
        self.sprite_suelo = pg.image.load("assets\sprites_suelo\suelo_cesped.png")
        self.lista_suelos = []

        for x in range(0, ns.ANCHO_NIVEL * largo_suelos, 64):
            self.lista_suelos.append(pg.Rect(x, ns.ALTO_NIVEL - 64, 64, 64))
    def dibujar_suelo(self, ventana, mundo_x):

        for suelo in self.lista_suelos:
            ventana.blit(self.sprite_suelo, (suelo.topleft[0] + mundo_x, suelo.topleft[1]))
            #pg.draw.rect(ventana, (255, 0, 0), suelo, 1)