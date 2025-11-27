import pygame as pg

class Jugador(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Estadisticas/ajustes
        self.estadisticas = {
            "Vida": 100,
            "Daño": 20
        }
        self.velocidad = 2

        # Sprites
        self.flip = False
        self.quieto = pg.image.load("assets\images_lautaro\Lautaro_base64.png").convert_alpha()
        self.caminando = pg.image.load("assets\images_lautaro\Lautaro_caminar.png").convert_alpha()
        self.imagen = self.quieto
        
        # Posición Hitbox
        self.x = x
        self.y = y
        self.rect = pg.Rect(self.x, self.y, 64, 64)
        self.hitbox = pg.Rect(self.rect.x + 10, self.rect.y + 10, 30, 40)
        
        # Frames de Sprites
        self.frame = 0
        self.frames_caminando = []
        self.frame_tiempo = 0

        for i in range(4):
            frame = self.caminando.subsurface(i * 32, 0, 32, 32)
            self.frames_caminando.append(frame)

    def dibujar(self, ventana):
        imagen_flip = pg.transform.flip(self.imagen, flip_x= self.flip, flip_y= False)
        ventana.blit(imagen_flip, self.rect.topleft)
        pg.draw.rect(ventana, (255, 0, 0), self.hitbox, 2)

    def mover(self, teclas):
        mov_x = 0
        mov_y = 0

        if teclas[pg.K_a]:
            mov_x = -1
            self.flip = True
        if teclas[pg.K_d]:
            mov_x = 1
            self.flip = False
        if teclas[pg.K_w]:
            mov_y = -1
        if teclas[pg.K_s]:
            mov_y = 1
        
        self.rect.x += mov_x * self.velocidad
        self.rect.y += mov_y * self.velocidad
        self.hitbox.center = self.rect.center

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
        self.hitbox.center = self.rect.center

    def obtener_posicion(self):
        return (self.rect.x, self.rect.y)
