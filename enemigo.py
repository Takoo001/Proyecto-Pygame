import pygame as pg
import nivel_settings as ns
from entidad import Entidad

class Enemigo(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tipo_entidad = 2
        # Estadisticas
        self.estadisticas["Vida"] = 50
        self.estadisticas["Daño"] = 10
        self.estadisticas["Velocidad"] = 2

        # Cooldown Ataque
        self.cooldown = 3000
        self.inicio_ataque = 1000 # Iniciar el ataque 1 segundo después de detectar el área de ataque con el jugador

        # Posición Hitbox
        self.hitbox = pg.Rect(self.x, self.y, 64, 64)
        self.ataque_hitbox = pg.Rect(self.rect.centerx + 15, self.rect.centery, 64, 64)

        # Frames de Sprites Corriendo
        self.frame_milisegundos = 100

        # Frames de Sprite Atacando
        self.frame_milisegundos_ataque = 10

        self.tiempo_de_inicio = pg.time.get_ticks()

        if len(self.frames_ataque) > 0:
            self.imagen_ataque = self.frames_ataque[0]

    def movimiento(self, jugador):
        tiempo_actual = pg.time.get_ticks()

        if self.hitbox.centerx > jugador.hitbox.centerx + 60:
            self.rect.x -= 1 * self.estadisticas["Velocidad"]
            self.direccion = "IZQUIERDA"
            self.flip = True

            if self.ataque_hitbox.colliderect(jugador.hitbox):
                if tiempo_actual - self.ultimo_ataque > self.cooldown and tiempo_actual - self.inicio_ataque:
                    if not self.atacando:
                        self.atacando = True
                        self.ultimo_ataque = tiempo_actual
                        self.inicio_ataque = tiempo_actual

        if self.hitbox.centerx < jugador.hitbox.centerx - 60:
            self.rect.x += 1 * self.estadisticas["Velocidad"]
            self.direccion = "DERECHA"
            self.flip = False

            if self.ataque_hitbox.colliderect(jugador.hitbox):
                if tiempo_actual - self.ultimo_ataque > self.cooldown and tiempo_actual - self.inicio_ataque:
                    if not self.atacando:
                        self.atacando = True
                        self.ultimo_ataque = tiempo_actual
                        self.inicio_ataque = tiempo_actual

        self.hitbox.center = self.rect.center

        if self.direccion == "DERECHA":
            self.ataque_hitbox = pg.Rect(self.rect.centerx + 15, self.rect.centery - 32, 64, 64)
        if self.direccion == "IZQUIERDA":
            self.ataque_hitbox = pg.Rect(self.rect.centerx - 79, self.rect.centery - 32, 64, 64)

        if self.atacando:
            self.animar_ataque()

    def dibujar(self, ventana):
        if self.atacando:
            ataque = pg.transform.flip(self.imagen_ataque, flip_x= self.flip, flip_y= False)
            ventana.blit(ataque, self.ataque_hitbox.topleft)
            pg.draw.rect(ventana, (255, 0, 0), self.ataque_hitbox, 2)

        imagen_flip = pg.transform.flip(self.imagen, flip_x= self.flip, flip_y= False)
        ventana.blit(imagen_flip, self.rect.topleft)
        pg.draw.rect(ventana, (255, 0, 0), self.hitbox, 1)
    
class EnemigoPequeno(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)

        # Sprites
        self.sprite_quieto = pg.image.load("assets\sprites_enemigos\enemigo_prueba.png").convert_alpha()
        self.imagen = self.sprite_quieto