import pygame as pg
import nivel_settings as ns
from entidad import Entidad

class Jugador(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y)

        # Sprites
        self.sprite_girando = pg.image.load("assets\sprites_lautaro\giro_aire.png").convert_alpha()
        self.sprite_dash = pg.image.load("assets\sprites_lautaro\dash.png").convert_alpha()

        # Recorte sprites por sus frames
        self.frames_corriendo = self.recortar_frames(self.sprite_corriendo, 12, 64, 64)
        self.frames_ataque = self.recortar_frames(self.sprite_ataque, 7, 64, 64)
        self.frames_girando = self.recortar_frames(self.sprite_girando, 4, 64, 64)
        self.frames_dasheando = self.recortar_frames(self.sprite_dash, 8, 64, 64)

        # Frames de Sprites Corriendo
        self.frame_milisegundos_corriendo = 50

        # Frames de Sprite Atacando
        self.frame_milisegundos_ataque = 10

        # Frames de Sprites Girando
        self.frame_girando = 0
        self.frame_tiempo_girando = 0
        self.frame_milisegundos_girando = 50

        # Frames Dasheando
        self.frame_dasheando = 0
        self.tiempo_de_inicio_dash= 0
        self.frame_milisegundos_dasheando = 10

        # Saber si se encuentra dasheando o no
        self.dasheando = False
        self.ultimo_dash = 0
        self.tiempo_de_inicio_dash = 0
        self.cooldown_dash = 1000
        self.duracion_dash = 200
        self.distancia_dash = 30
       
        self.tiempo_de_inicio = pg.time.get_ticks()
        
        if len(self.frames_ataque) > 0:
            self.imagen_ataque = self.frames_ataque[0]

    def movimiento(self, teclas):
        # Movimiento Jugador
        mov_x = 0
        mov_y = 0
        tiempo_actual = pg.time.get_ticks()

        if teclas[pg.K_a]:
            mov_x = -1
            self.direccion = "IZQUIERDA"
            self.flip = True

        if teclas[pg.K_d]:
            mov_x = 1
            self.direccion = "DERECHA"
            self.flip = False

        if teclas[pg.K_w] and not self.en_el_aire:
            self.velocidad_y = self.velocidad_salto
            self.en_el_aire = True

        if teclas[pg.K_LSHIFT] and tiempo_actual - self.ultimo_dash > self.cooldown_dash:
            if not self.dasheando:
                self.dasheando = True
                self.ultimo_dash = tiempo_actual
                self.tiempo_de_inicio_dash = tiempo_actual

        if self.dasheando:
            tiempo_dash = tiempo_actual - self.tiempo_de_inicio_dash
            porcentaje_dash = min(tiempo_dash / self.distancia_dash, 1)

            distancia_recorrida = self.distancia_dash * porcentaje_dash

            if self.direccion == "DERECHA":
                self.rect.x += distancia_recorrida
            if self.direccion == "IZQUIERDA":
                self.rect.x -= distancia_recorrida
            
            if tiempo_dash >= self.duracion_dash:
                self.dasheando = False

        if self.en_el_aire:
            self.velocidad_y += self.gravedad
        
        mov_y = self.velocidad_y

        # Ataque
        if teclas[pg.K_SPACE] and tiempo_actual - self.ultimo_ataque > self.cooldown:
            if not self.en_el_aire:
                if not self.atacando:
                    self.atacando = True
                    self.ultimo_ataque = tiempo_actual
                    self.tiempo_de_inicio_ataque = tiempo_actual

        # Movimiento
        self.rect.x += mov_x * self.estadisticas["Velocidad"]

        self.rect.y += mov_y
        self.hitbox.center = self.rect.center

        # Cambiar sprite del Jugador en caso de movimiento o no
        if not self.dasheando:    
            if self.en_el_aire:
                self.animar_giro()
            else:
                if mov_x != 0:
                    self.animar_corriendo()
                else:
                    self.imagen = self.sprite_quieto
        else:
            self.animar_dash()

        if self.direccion == "DERECHA":
            self.ataque_hitbox = pg.Rect(self.rect.centerx + 15, self.rect.centery - 48, 64, 64)
        if self.direccion == "IZQUIERDA":
            self.ataque_hitbox = pg.Rect(self.rect.centerx - 79, self.rect.centery - 48, 64, 64)

        if self.atacando:
            self.animar_ataque()
    
    def animar_giro(self):
        tiempo_actual = pg.time.get_ticks()
        
        if tiempo_actual - self.tiempo_de_inicio > self.frame_milisegundos_girando:  
            self.frame_girando = (self.frame_girando + 1) % len(self.frames_girando)
            self.imagen = self.frames_girando[self.frame_girando]
            self.tiempo_de_inicio = tiempo_actual
    
    def animar_dash(self):
        tiempo_actual = pg.time.get_ticks()
        
        if tiempo_actual - self.tiempo_de_inicio > self.frame_milisegundos_dasheando:  
            self.frame_dasheando = (self.frame_dasheando + 1) % len(self.frames_dasheando)
            self.imagen = self.frames_dasheando[self.frame_dasheando]
            self.tiempo_de_inicio = tiempo_actual