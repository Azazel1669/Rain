import pygame


def draw(screen):
    screen.fill("yellow")
    if n % 2 == 0:
        n1 = n // 2
    else:
        n1 = n // 2 + 1
    len = 300 // n1

    for i in range(1, len, 2):
        for j in range(1, len, 2):
            pygame.draw.polygon(screen, 'orange', [[n1 * (j - 1), n1 * i], [n1 * j, n1 * (i - 1)], [n1 * (j + 1), n1 * i], [n1 * j, n1 * (i + 1)]])


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Ромбики")
    size = width, height = 300, 300
    try:
        n = int(input())
    except ValueError:
        print("Неправильный формат ввода")
        pygame.quit()
    else:
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
