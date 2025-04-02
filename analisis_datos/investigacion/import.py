import pygame

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
screen = pygame.display.set_mode((800, 600))

# Definir el título de la ventana
pygame.display.set_caption("Mover rectángulo con teclas")

# Definir el color del rectángulo
color_rect = (255, 0, 0)  # Rojo

# Coordenadas iniciales del rectángulo
x, y = 350, 250
speed = 5  # Velocidad de movimiento

# Bucle principal
running = True
while running:
    # Comprobar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover el rectángulo
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Rellenar la pantalla con color de fondo
    screen.fill((255, 255, 255))  # Fondo blanco

    # Dibujar el rectángulo
    pygame.draw.rect(screen, color_rect, (x, y, 50, 50))

    # Actualizar la pantalla
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()