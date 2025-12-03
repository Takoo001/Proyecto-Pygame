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
        self.gravedad = 1
        self.contacto_suelo = False

        # Sprites
        self.flip = False
        self.quieto = pg.image.load("assets\sprites_lautaro\Lautaro_base64.png").convert_alpha()
        self.corriendo = pg.image.load("assets\sprites_lautaro\lautaro_corriendo.png").convert_alpha()
        self.imagen = self.quieto
        
        # Posición Hitbox
        self.x = x
        self.y = y
        self.rect = pg.Rect(self.x, self.y, 64, 64)
        self.hitbox = pg.Rect(self.x + 10, self.y + 10, 25, 35)
        
        # Frames de Sprites
        self.frame = 0
        self.frames_corriendo = []
        self.frame_tiempo = 0
        self.frame_milisegundos = 50

        for i in range(12):
            frame = self.corriendo.subsurface(i * 64, 0, 64, 64)
            self.frames_corriendo.append(frame)

        self.tiempo_de_inicio = pg.time.get_ticks() 

    def dibujar(self, ventana):
        imagen_flip = pg.transform.flip(self.imagen, flip_x= self.flip, flip_y= False)
        ventana.blit(imagen_flip, self.rect.topleft)
        #pg.draw.rect(ventana, (255, 0, 0), self.hitbox, 1)

    def movimiento(self, teclas):
        # Movimiento Jugador
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
        
        self.rect.x += mov_x * self.velocidad
        self.rect.y += mov_y * self.velocidad
        self.hitbox.center = self.rect.center

        # Cambiar sprite del Jugador en caso de movimiento o no
        if mov_x != 0 or mov_y != 0:
            self.animar_caminando()
        else:
            self.imagen = self.quieto
    
    def animar_caminando(self):
        tiempo_actual = pg.time.get_ticks()
        
        if tiempo_actual - self.tiempo_de_inicio > self.frame_milisegundos:  
            self.frame = (self.frame + 1) % len(self.frames_corriendo)
            self.imagen = self.frames_corriendo[self.frame]
            self.tiempo_de_inicio = tiempo_actual

    def obtener_posicion(self):
        return (self.hitbox.x, self.hitbox.y)
    
    def restablecer_posicion(self, y):
        self.rect.y = y
        self.hitbox.center = self.rect.center
        self.velocidad_y = 0
