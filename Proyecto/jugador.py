import pygame as pg

class Jugador:
    def __init__(self, posicion):
        self.vida = 100
        self.daño = 20
        self.posicion = posicion
        self.estado = "quieto"
        self.animaciones = {
            "quieto": self.cargar_sprite("Lautaro.png", 32, 32),
            "caminar": self.cargar_sprite("Lautaro_caminar.png", 32, 32)
        }
        self.frame = 0
        self.frame_timer = 0
        self.frame_velociad = 0.15

    def cargar_sprite(self, sprite, ancho_frame, alto_frame):
        imagen = pg.image.load(sprite).convert_alpha()
        frames = []

        ancho_hoja, alto_hoja = imagen.get_size()

        for i in range(0, ancho_hoja, ancho_frame):
            frame = imagen.subsurface((i, 0, ancho_frame, alto_frame))
            frames.append(frame)

        return frames

    def actualizar(self, dt):
        self.frame_timer += dt
        if self.frame_timer >= self.frame_velociad:
            self.frame_timer = 0
            self.frame += 1
            if self.frame >= len(self.animaciones[self.estado]):
                self.frame = 0