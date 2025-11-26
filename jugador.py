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
        self.velocidad = 2
        self.frame = 0  # Comienza con el primer frame
        self.frames_caminando = []  # Lista para almacenar los frames de la animación
        self.frame_tiempo = 0

        for i in range(4):
            frame = self.caminando.subsurface(i * 32, 0, 32, 32)
            self.frames_caminando.append(frame)

        self.imagen = self.quieto

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)

    def mover(self, teclas):
        mov_x = 0
        mov_y = 0

        if teclas[pg.K_a]:
            mov_x = -0.5
        if teclas[pg.K_d]:
            mov_x = 0.5
        if teclas[pg.K_w]:
            mov_y = -0.5
        if teclas[pg.K_s]:
            mov_y = 0.5
        
        self.rect.x += mov_x * self.velocidad
        self.rect.y += mov_y * self.velocidad

        if mov_x != 0 or mov_y != 0:
            self.animar_caminando()
        else:
            self.imagen = self.quieto

    def animar_caminando(self):
        self.frame_tiempo += 1
        
        if self.frame_tiempo >= 5:  
            self.frame_tiempo = 0
            self.frame = (self.frame + 1) % len(self.frames_caminando)
            self.imagen = self.frames_caminando[self.frame]

    def restablecer_posicion(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def obtener_posicion(self):
        return (self.rect.x, self.rect.y)
