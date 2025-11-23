import pygame as pg

from jugador import Jugador

pg.init()

background = (30, 30, 30)

ventana = pg.display.set_mode((640, 480))
pg.display.set_caption("Movimiento de rectángulos y colisión")

# Creando Objetos
jugador = Jugador(100, 100)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False
    ventana.fill(background)

    teclas = pg.key.get_pressed()

    # Almacena la posición inicial de los rectángulos

    posición_ant_jugador = jugador.obtener_posicion()

    # Mover Rectángulos
    jugador.mover(teclas)

    '''if rectangulo_pequeno.rect.colliderect(rectangulo_grande.rect):
        # Si existe colosión, se reestablece la posición anterior
        rectangulo_pequeno.restablecer_posicion(*posición_anterior_pequeño)
        rectangulo_grande.restablecer_posicion(*posición_anterior_grande)

    else:
        #Restablecer color
        rectangulo_pequeno.cambiar_color((63, 232, 234))
        rectangulo_grande.cambiar_color((63, 234, 76))'''

    ventana.fill(background)    
    jugador.dibujar(ventana)

    pg.display.update()

pg.quit