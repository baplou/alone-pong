import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800,800))
        self.clock = pygame.time.Clock()

        self.bg = pygame.transform.scale(pygame.image.load("assets/background.png"),(800,800)).convert_alpha()
        self.duck = pygame.image.load("assets/duck.png").convert_alpha()
        self.bar = pygame.image.load("assets/bar.png").convert_alpha()

        self.mainloop()

    def endscreen(self):
        """end screen functionality"""
        pass

    def play(self):
        """game functionality"""
        pass

    def main(self):
        """handling game stages"""
        pass

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.bg,(0,0))
            self.main()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    g = Game()
