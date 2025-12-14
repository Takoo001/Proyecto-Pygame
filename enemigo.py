import pygame as pg
import nivel_settings as ns
from entidad import Entidad

class Enemigo(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y)

        # Estadisticas
        self.estadisticas["Vida"] = 50
        self.estadisticas["Daño"] = 10
        self.estadisticas["Velocidad"] = 3

        # Cooldown Ataque
        self.cooldown = 5000

        # Posición Hitbox
        self.hitbox = pg.Rect(self.x, self.y, 25, 35)
        self.ataque_hitbox = pg.Rect(self.rect.centerx + 15, self.rect.centery - 48, 64, 64)

        # Frames de Sprites Corriendo
        self.frame_milisegundos = 100

        # Frames de Sprite Atacando
        self.frame_milisegundos_ataque = 10

        self.tiempo_de_inicio = pg.time.get_ticks()
        
        if len(self.frames_ataque) > 0:
            self.imagen_ataque = self.frames_ataque[0]

    # Bucle para recortar el sprite por el total de frames:

    def movimiento(self, teclas):
        super().movimiento()

    def dibujar(self, ventana):
        if self.atacando:
            ataque = pg.transform.flip(self.imagen_ataque, flip_x= self.flip, flip_y= False)
            ventana.blit(ataque, self.ataque_hitbox.topleft)
            pg.draw.rect(ventana, (255, 0, 0), self.ataque_hitbox, 2)

        imagen_flip = pg.transform.flip(self.imagen, flip_x= self.flip, flip_y= False)
        ventana.blit(imagen_flip, self.rect.topleft)
        pg.draw.rect(ventana, (255, 0, 0), self.hitbox, 1)

class EnemigoPequeño(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)

        # Sprites
        self.quieto = pg.image.load("assets\sprites_lautaro\Lautaro_base64.png").convert_alpha()
        self.corriendo = pg.image.load("assets\sprites_lautaro\lautaro_corriendo.png").convert_alpha()
        self.imagen = self.quieto
        self.sprite_ataque = pg.image.load("assets\\sprites_lautaro\\ataque_prueba.png").convert_alpha()
        self.imagen_ataque = None
