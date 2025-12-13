import pygame as pg
import nivel_settings as ns

class Jugador(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Estadisticas/ajustes
        self.estadisticas = {
            "Vida": 100,
            "Daño": 20
        }
        self.velocidad = 5
        self.velocidad_y = 0

        # Parametros para Ataque
        self.atacando = False
        self.atacando_timer = 0
        self.direccion = "DERECHA"

        # Lógica de cooldown de ataque
        self.cooldown = 1000
        self.ultimo_ataque = 0

        # Sprites
        self.flip = False
        self.quieto = pg.image.load("assets\sprites_lautaro\Lautaro_base64.png").convert_alpha()
        self.corriendo = pg.image.load("assets\sprites_lautaro\lautaro_corriendo.png").convert_alpha()
        self.imagen = self.quieto
        self.sprite_ataque = pg.image.load("assets\\sprites_lautaro\\ataque_prueba.png").convert_alpha()
        self.imagen_ataque = None

        # Posición Hitbox
        self.x = x
        self.y = y
        self.rect = pg.Rect(self.x, self.y, 64, 64)
        self.hitbox = pg.Rect(self.x, self.y, 25, 35)
        self.ataque_hitbox = pg.Rect(self.rect.centerx + 15, self.rect.centery - 48, 64, 64)

        # Frames de Sprites caminando
        self.frame_corriendo = 0
        self.frames_corriendo = []
        self.frame_tiempo_corriendo = 0
        self.frame_milisegundos = 100

        # Frames de Sprite atacando
        self.frame_ataque = 0
        self.frames_ataque = []
        self.frame_tiempo_ataque = 0
        self.frame_milisegundos_ataque = 10
        self.tiempo_de_inicio_ataque = pg.time.get_ticks()

        self.tiempo_de_inicio = pg.time.get_ticks()
        

        # Bucle para recortar el sprite por el total de frames:

        # Personaje Corriendo
        for i in range(12):
            frame = self.corriendo.subsurface(i * 64, 0, 64, 64)
            self.frames_corriendo.append(frame)

        # Ataque
        for a in range(7):
            frame = self.sprite_ataque.subsurface(a * 64, 0, 64, 64)
            self.frames_ataque.append(frame)

        if len(self.frames_ataque) > 0:
            self.imagen_ataque = self.frames_ataque[0]

    def dibujar(self, ventana):
        if self.atacando:
            ataque = pg.transform.flip(self.imagen_ataque, flip_x= self.flip, flip_y= False)
            ventana.blit(ataque, self.ataque_hitbox.topleft)
            pg.draw.rect(ventana, (255, 0, 0), self.ataque_hitbox, 2)

        imagen_flip = pg.transform.flip(self.imagen, flip_x= self.flip, flip_y= False)
        ventana.blit(imagen_flip, self.rect.topleft)
        pg.draw.rect(ventana, (255, 0, 0), self.hitbox, 1)

    def movimiento(self, teclas):
        # Movimiento Jugador
        mov_x = 0
        mov_y = 0

        if teclas[pg.K_a]:
            mov_x = -1
            self.direccion = "IZQUIERDA"
            self.flip = True

        if teclas[pg.K_d]:
            mov_x = 1
            self.direccion = "DERECHA"
            self.flip = False

        if teclas[pg.K_w]:
            mov_y = -1
        if teclas[pg.K_s]:
            mov_y = 1
        
        tiempo_actual = pg.time.get_ticks()

        # Ataque
        if teclas[pg.K_SPACE] and tiempo_actual - self.ultimo_ataque > self.cooldown:
            if not self.atacando:
                self.atacando = True
                self.ultimo_ataque = tiempo_actual
                self.tiempo_de_inicio_ataque = tiempo_actual
                self.animar_ataque()

        # Movimiento
        self.rect.x += mov_x * self.velocidad
        self.rect.y += mov_y * self.velocidad
        self.hitbox.center = self.rect.center

        # Cambiar sprite del Jugador en caso de movimiento o no
        if mov_x != 0:
            self.animar_corriendo()
        else:
            self.imagen = self.quieto

        if self.direccion == "DERECHA":
            self.ataque_hitbox = pg.Rect(self.rect.centerx + 15, self.rect.centery - 48, 64, 64)
        if self.direccion == "IZQUIERDA":
            self.ataque_hitbox = pg.Rect(self.rect.centerx - 79, self.rect.centery - 48, 64, 64)

        if self.atacando:
            self.animar_ataque()

    def animar_corriendo(self):
        tiempo_actual = pg.time.get_ticks()
        
        if tiempo_actual - self.tiempo_de_inicio > self.frame_milisegundos:  
            self.frame_corriendo = (self.frame_corriendo + 1) % len(self.frames_corriendo)
            self.imagen = self.frames_corriendo[self.frame_corriendo]
            self.tiempo_de_inicio = tiempo_actual

    def animar_ataque(self):
        tiempo_actual = pg.time.get_ticks()

        if tiempo_actual - self.tiempo_de_inicio_ataque > self.frame_milisegundos_ataque:  
            self.frame_ataque += 1
            if self.frame_ataque >= len(self.frames_ataque):
                self.atacando = False
                self.frame_ataque = 0

            if self.frame_ataque < len(self.frames_ataque):
                self.imagen_ataque = self.frames_ataque[self.frame_ataque]

            self.tiempo_de_inicio_ataque = tiempo_actual

    def obtener_posicion(self):
        return (self.hitbox.x, self.hitbox.y)
    
    def restablecer_posicion(self, y):
        self.rect.y = y
        self.hitbox.center = self.rect.center
        self.velocidad_y = 0
