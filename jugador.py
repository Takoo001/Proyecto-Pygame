import pygame as pg

class Jugador(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.estadisticas = {
            "Vida": 100,
            "Daño": 20
        }
        self.quieto = pg.image.load("assets\images_lautaro\Lautaro_base.png").convert_alpha()
        self.caminando = pg.image.load("assets\images_lautaro\Lautaro_caminar.png").convert_alpha()
        self.x = x
        self.y = y
        self.rect = pg.Rect(0, 0, 32, 32)
        self.rect.center = (x, y)
        self.velocidad = 1

    def dibujar(self, ventana):
        pg.draw.rect(ventana, (0, 225, 0), self.rect)

    def mover(self, teclas):
        mov_x = 0
        mov_y = 0

        if teclas[pg.K_a]:
            mov_x = -1
        if teclas[pg.K_d]:
            mov_x = 1
        if teclas[pg.K_w]:
            mov_y = -1
        if teclas[pg.K_s]:
            mov_y = 1
        
        self.rect.x += mov_x * self.velocidad
        self.rect.y += mov_y * self.velocidad

    def restablecer_posicion(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def obtener_posicion(self):
        return (self.rect.x, self.rect.y)
