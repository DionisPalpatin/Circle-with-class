import pygame as pg


class Circle():
    def __init__(self, center_X, center_Y, rad, colour, direction):
        self.X = center_X
        self.Y = center_Y
        self.rad = rad
        self.colour = colour
        self.direction = direction


    def move_by_itself(self):
        if not (self.rad - 1 < self.X < size - self.rad + 1):
            self.direction *= -1
        self.X += self.direction


    def move(self):
        if keys[pg.K_RIGHT]:
            self.X += 1
        elif keys[pg.K_LEFT]:
            self.X -= 1
        else:
            self.move_by_itself()


circle = Circle(100, 100, 35, (0, 0, 0), 1)
size = 500    


pg.init()
window = pg.display.set_mode((size, size), pg.SHOWN)
pg.draw.circle(window, circle.colour, (circle.X, circle.Y), circle.rad)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


    keys = pg.key.get_pressed()
    circle.move()


    window.fill((255, 255, 255))
    pg.draw.circle(window, circle.colour, (circle.X, circle.Y), circle.rad)


    pg.display.update()
    pg.time.delay(10)