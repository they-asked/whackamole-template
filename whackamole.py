import pygame, random

def main():
    try:
        pygame.init()
        pygame.display.set_caption("only 0.1% of people can catch the mole!!!!1!!")
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x_mole, y_mole = (0, 0)
        while running:
            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_click, y_click = event.pos
                    if x_click // 32 == x_mole and y_click // 32 == y_mole:
                        x_mole, y_mole = (random.randrange(0, 20), random.randrange(0, 16))
            #Drawing The Board
            screen.fill("light green")
            for i in range(0, 21):
                pygame.draw.line(screen, "dark green", (32 * i, 0), (32 * i, 512))
            for i in range(0, 17):
                pygame.draw.line(screen, "dark green", (0, 32 * i), (640, 32 * i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(32*x_mole + 3, 32*y_mole + 3)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
