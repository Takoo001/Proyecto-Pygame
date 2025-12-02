import pygame

pygame.init()

# Pantalla
pantalla_info = pygame.display.Info()
ANCHO = pantalla_info.current_w
ALTO = pantalla_info.current_h
PANTALLA = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)

# Colores
BLANCO = (255, 255, 255)
NARANJO = (255, 140, 0)

# Configuración global
BRILLO = 100
VOLUMEN = 100

# Rutas de assets
RUTA_LOGO = "assets/images/logo_juego.png"
RUTA_PJ_CAMINANDO = "assets/sprites_lautaro/Lautaro_base64.png"
RUTA_FONDO_MENU = "assets/images/fondo_bosque.png"
RUTA_PANEL_MENU = "assets/images/fondo_menu.png"
RUTA_BOTON = "assets/images/boton_fondo.png"
RUTA_SPRITE_LAUTARO = "assets/images/pj.png"
RUTA_MUSICA_MENU = "assets/musica/musica_menu.ogg"

# Fuentes
pygame.font.init()
FUENTE_GENERAL = pygame.font.Font(None, 60)
FUENTE_TITULO = pygame.font.Font(None, 120)

# Reloj global
RELOJ = pygame.time.Clock()
