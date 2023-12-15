import pygame


def draw_diamond(surface, color, x, y, size):
    pygame.draw.polygon(surface, color,
                        [[x + size / 2, y], [x + size, y + size / 2], [x + size / 2, y + size], [x, y + size / 2]])


try:
    n = int(input("Enter size: "))
except ValueError:
    print("Invalid input format")
    quit()

size = (300, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Orange Diamonds")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color("yellow"))
    draw_diamond(screen, pygame.Color("orange"), size[0] // 2 - n // 2, size[1] // 2 - n // 2, n)
    draw_diamond(screen, pygame.Color("orange"), size[0] // 2 + n // 2, size[1] // 2 - n // 2, n)
    draw_diamond(screen, pygame.Color("orange"), size[0] // 2 - n // 2, size[1] // 2 + n // 2, n)
    draw_diamond(screen, pygame.Color("orange"), size[0] // 2 + n // 2, size[1] // 2 + n // 2, n)

    pygame.display.update()

pygame.quit()