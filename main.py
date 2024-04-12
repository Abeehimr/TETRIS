from settings import *
import sys
from Tetris import Tetris,Text

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(WIN)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)
        self.text = Text(self)

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.ani_trigger = False
        self.fast_ani_trigger = False
        pg.time.set_timer(self.user_event,ANI_INTERVAL)
        pg.time.set_timer(self.fast_user_event,FAST_ANI_INTERVAL)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)
        
    def draw(self):
        self.screen.fill(color=BG_COLOR)
        pg.draw.rect(self.screen, FIELD_COLOR,(0,0,*FIELD_RES))
        self.tetris.draw()
        self.text.draw()
        pg.display.flip()

    def check_events(self):
        self.ani_trigger = False
        self.fast_ani_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(event.key)
            elif event.type == self.user_event:
                self.ani_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_ani_trigger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()