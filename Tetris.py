from settings import *
from tretomino import Tetromino
import pygame.freetype  as ft

class Text():
    def __init__(self,app) -> None:
        self.app = app
        self.font = ft.Font(None)

    def draw(self):
        self.font.render_to(self.app.screen , 
                            (WIN_W*0.65*TILE_SIZE, WIN_H*0.02*TILE_SIZE),
                            "TETRIS",fgcolor="white",size=TILE_SIZE*1.5,bgcolor=BG_COLOR)
        self.font.render_to(self.app.screen , 
                            (WIN_W*0.65*TILE_SIZE, WIN_H*0.33*TILE_SIZE),
                            "NEXT",fgcolor="white",size=TILE_SIZE*1.5,bgcolor=BG_COLOR)
        self.font.render_to(self.app.screen , 
                            (WIN_W*0.65*TILE_SIZE, WIN_H*0.63*TILE_SIZE),
                            "SCORE",fgcolor="white",size=TILE_SIZE*1.5,bgcolor=BG_COLOR)
        self.font.render_to(self.app.screen , 
                            (WIN_W*0.65*TILE_SIZE, WIN_H*0.72*TILE_SIZE),
                            f"{self.app.tetris.score}",fgcolor="white",size=TILE_SIZE*1.5,bgcolor=BG_COLOR)
        
class Tetris():
    def __init__(self,app) -> None:
        self.app = app
        self.sp_group = pg.sprite.Group()
        self.tetromino = Tetromino(self,current=True)
        self.prev = Tetromino(self)
        self.board = [[0]*FIELD_W for _ in range(FIELD_H)]
        self.mov_fast = False

        self.score = 0
        self.full_lines = 0

    def update_score(self):
        self.score += SCORE_SHEET[self.full_lines]
        self.full_lines = 0

    def is_line_done(self):
        row = FIELD_H-1
        for y in range(FIELD_H-1,-1,-1):
            for x in range(FIELD_W):
                self.board[row][x] = self.board[y][x]
                if self.board[row][x]:
                    self.board[row][x].pos = vec(x,y)

            if sum(map(bool,self.board[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.board[row][x].live = False
                    self.board[row][x] = 0

                self.full_lines += 1

    def save_tetro(self):
        for block in self.tetromino.blocks:
            x,y = map(int,block.pos)
            self.board[y][x] = block

    def control(self,key):
        if key == pg.K_LEFT:
            self.tetromino.move("left")
        elif key == pg.K_RIGHT:
            self.tetromino.move("right")
        elif key == pg.K_UP:
            self.tetromino.rotate()
        elif key == pg.K_DOWN:
            self.mov_fast = True

    def draw_grid(self):
        for y in range(FIELD_H):
            for x in range(FIELD_W):
                pg.draw.rect(self.app.screen,"black",(x*TILE_SIZE,y*TILE_SIZE,TILE_SIZE,TILE_SIZE),1)

    def is_tetro_landed(self):
        if self.tetromino.landed:
            if self.tetromino.blocks[0].pos[1] <= 0:
                pg.time.wait(300)
                self.__init__(self.app)
            else:
                self.mov_fast = False
                self.save_tetro()
                self.tetromino = self.prev
                self.tetromino.make_current()
                self.prev = Tetromino(self)

    def update(self):
        trigger = [self.app.ani_trigger,self.app.fast_ani_trigger][self.mov_fast]
        if trigger:
            self.is_line_done()
            self.tetromino.update()
            self.is_tetro_landed()
            self.update_score()
        self.sp_group.update()

    def draw(self):
        self.draw_grid()
        self.sp_group.draw(self.app.screen)