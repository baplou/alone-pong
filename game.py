import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Solo Pong")
        pygame.display.set_icon(pygame.image.load("assets/favicon.png"))
        self.clock = pygame.time.Clock()

        self.bg = pygame.transform.scale(pygame.image.load("assets/background.png"),(800,800)).convert_alpha()
        self.duck = pygame.transform.scale(pygame.image.load("assets/duck.png"), (40,40)).convert_alpha()
        self.bar = pygame.transform.scale(pygame.image.load("assets/bar.png"), (200,200)).convert_alpha()

        self.bar_x = 600
        self.bar_y = 300
        self.bar_mask = pygame.mask.from_surface(self.bar)
        self.bar_direction = "up" 
        self.bar_direction_counter = 0
        self.bar_direction_list = ["up", "sideways"]

        self.duck_x = 400
        self.duck_y = 400
        self.duck_vel = 2
        self.duck_mask = pygame.mask.from_surface(self.duck)
        self.duck_direction = "sideways"

        self.counter = 0
        self.counter2 = 0
        self.rotate_counter = 0
        self.rotate_main = 90

        self.game_active = True
        self.score = 0
        
        self.mainloop()

    def collide(self, x1, x2, y1, y2, mask1, mask2):
        offsetx = x2 - x1
        offsety = y2 - y1
        return mask1.overlap(mask2, (offsetx, offsety)) != None

    def endscreen(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.bar = pygame.transform.scale(pygame.image.load("assets/bar.png"), (200,200)).convert_alpha()
            self.bar_x = 600
            self.bar_y = 300
            self.bar_mask = pygame.mask.from_surface(self.bar)
            self.bar_direction = "up" 
            self.duck_direction = "sideways"
            self.bar_direction_counter = 0
            self.duck_x = 400
            self.duck_y = 400
            self.duck_vel = 2
            self.score = 0
            self.game_active = True
        dead_font = pygame.font.SysFont("comicsans", 70)
        dead_label = dead_font.render("You lost with a score of: " + str(self.score), 1, (255,255,255))
        restart_font = pygame.font.SysFont("comicsans", 70)
        restart_label = restart_font.render("To restart press 'r'", 1, (255,255,255))
        self.screen.blit(dead_label, (800/2 - dead_label.get_width()/2, 800/2 - dead_label.get_height()/2))
        self.screen.blit(restart_label, (800/2 - restart_label.get_width()/2, (800/2 - restart_label.get_height()/2) + 100))

    def play(self):
        keys = pygame.key.get_pressed()
        self.counter += 1
        self.counter2 += 1
        if keys[pygame.K_UP]:
            self.bar_y -= 5
        if keys[pygame.K_DOWN]:
            self.bar_y += 5
        if keys[pygame.K_LEFT]:
            self.bar_x -= 5
        if keys[pygame.K_RIGHT]:
            self.bar_x += 5
        if keys[pygame.K_s] and self.counter >= 20:
            self.bar_direction_counter += 1
            self.rotate_counter += 1
            if self.bar_direction_counter > 1:
                self.bar_direction_counter = 0
            if self.rotate_counter >= 2:
                self.rotate_counter = 0
                self.rotate_main = 270
            else:
                self.rotate_main = 90
            self.bar_direction = self.bar_direction_list[self.bar_direction_counter] 
            self.bar = pygame.transform.rotate(self.bar, self.rotate_main)
            self.bar_mask = pygame.mask.from_surface(self.bar)
            self.counter = 0

        if self.collide(self.bar_x, self.duck_x, self.bar_y, self.duck_y, self.bar_mask, self.duck_mask) and self.counter2 >= 60:
            self.counter2 = 0
            if self.duck_vel < 0:
                constant = -2
            else:
                constant = 2
            if self.bar_direction == "up":
                self.duck_direction = "sideways"
                if self.bar_x >= self.duck_x - 8:
                    self.duck_vel = -2
                elif self.bar_x <= self.duck_x:
                    self.duck_vel = 2
            elif self.bar_direction == "sideways":
                self.duck_direction = "up"
                if self.bar_y + 100 >= self.duck_y:
                    self.duck_vel = -2
                elif self.bar_y <= self.duck_y:
                    self.duck_vel = 2
            if self.duck_vel != constant:
                self.score += 1

        if self.duck_direction == "sideways":
            self.duck_x += self.duck_vel
        elif self.duck_direction == "up":
            self.duck_y += self.duck_vel

        self.main_font = pygame.font.SysFont("comicsans", 50)
        self.score_label = self.main_font.render(f"Score: {str(self.score)}", 1, (255,255,255))

        self.screen.blit(self.duck,(self.duck_x,self.duck_y))
        self.screen.blit(self.bar,(self.bar_x,self.bar_y))
        self.screen.blit(self.score_label,(800 - self.score_label.get_width() - 10, 10))

        if self.duck_x >= 800 or self.duck_x <= 0 or self.duck_y >= 800 or self.duck_y <= 0:
            self.game_active = False
 
    def main(self):
        if self.game_active:
            self.play()
        else:
            self.endscreen()

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
