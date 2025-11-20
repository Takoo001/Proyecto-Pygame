import pygame
import sys
import time
from menu import menu

pygame.init()

pantalla_info = pygame.display.Info()
ANCHO = pantalla_info.current_w
ALTO = pantalla_info.current_h
pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)


# Cargando imagenes
logo = pygame.image.load("assets/images/logo_juego.png").convert_alpha()
pj_caminando = pygame.image.load("assets/images/pj_caminando.png").convert_alpha()

# Colores
BLANCO = (255,255,255)
NARANJO = (255,140,0)

fuente_carga = pygame.font.Font(None, 70)
reloj = pygame.time.Clock()



def animacion_inicio():
    # Tamaño del logo
    escala = 0.1  
    escala_final = 1.0

    # Posición inicial y final
    x_logo = ANCHO // 2
    y_logo = ALTO // 2
    y_logo_final = ALTO * 0.13

    puntos = 0
    tiempo_puntos = 0

    # Tiempo de animacion del logo
    while escala < escala_final or y_logo > y_logo_final:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pantalla.fill((0, 0, 0))

        if escala < escala_final:
            escala += 0.02

        logo_escalado = pygame.transform.scale(
            logo,
            (int(logo.get_width() * escala), int(logo.get_height() * escala))
        )
        rect_logo = logo_escalado.get_rect(center=(x_logo, y_logo))

        pantalla.blit(logo_escalado, rect_logo)

        # Mover logo hacia arriba
        if escala >= escala_final and y_logo > y_logo_final:
            y_logo -= 10

        tiempo_puntos += 1
        if tiempo_puntos > 30:
            puntos = (puntos + 1) % 4
            tiempo_puntos = 0

        texto = "Cargando" + "." * puntos
        render_carga = fuente_carga.render(texto, True, BLANCO)
        pantalla.blit(render_carga, (ANCHO * 0.70, ALTO * 0.85))

        pj_escalado = pygame.transform.scale(pj_caminando, (120, 120))
        pantalla.blit(pj_escalado, (ANCHO * 0.15, ALTO * 0.78))

        pygame.display.flip()
        reloj.tick(60)

    time.sleep(0.8)

if __name__ == "__main__":
    animacion_inicio()
    menu()
