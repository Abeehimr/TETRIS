from settings import *
import random

class Block(pg.sprite.Sprite):
    def __init__(self,tetromino,pos) -> None:
        self.tetromino = tetromino
        if not tetromino.current:
            self.pos = vec(pos) + PREV_POS_OFFSET
        else:
            self.pos = vec(pos) + INIT_POS_OFFSET
        
        super().__init__(tetromino.tetris.sp_group)
        self.image = pg.Surface([TILE_SIZE,TILE_SIZE])
        pg.draw.rect(self.image,FIELD_COLOR,(1,1,TILE_SIZE-2,TILE_SIZE-2))
        pg.draw.rect(self.image,tetromino.color,(1,1,TILE_SIZE-2,TILE_SIZE-2),border_radius=8)
        self.rect = self.image.get_rect()
        
        self.live = True

    def make_current(self,pos):
        self.pos = vec(pos) + INIT_POS_OFFSET

    def is_alive(self):
        if not self.live:
            self.kill()

    def set_rect_pos(self) -> None:
        self.rect.topleft = self.pos*TILE_SIZE

    def update(self):
        self.is_alive()
        self.set_rect_pos()

    def rotate(self,pivot):
        a = self.pos - pivot
        return a.rotate(90) + pivot


    def is_collide(self,new_pos):
        x,y =  map(int,new_pos)
        if 0 <= x < FIELD_W and y < FIELD_H and (y < 0 or not self.tetromino.tetris.board[y][x]):
            return False
        else:
            return True

class Tetromino():
    def __init__(self,Tetris,current=False) -> None:
        self.tetris = Tetris
        self.current = current
        self.shape = random.choice(list(TETROS.keys()))
        self.color = random.choice(PIECE_COLORS)
        self.blocks = [Block(self,pos) for pos in TETROS[self.shape]]
        self.landed = False

    def make_current(self):
        self.current = True
        for i, block in enumerate(self.blocks):
            block.make_current(TETROS[self.shape][i])

    def is_collide(self,offset):
        return any(block.is_collide(block.pos + offset) for block in self.blocks)

    def move(self,direc):
        offset = MOV_DIREC[direc]

        if not self.is_collide(offset):
            for block in self.blocks:
                block.pos += offset
        elif direc == "down":
            self.landed = True

    def rotate(self):
        pivot = self.blocks[0].pos
        new_pos = [block.rotate(pivot) for block in self.blocks]
        if not any(block.is_collide(new_pos[i]) for i,block in enumerate(self.blocks)):
            for i , block in enumerate(self.blocks):
                block.pos = new_pos[i]

    def update(self):
        self.move(direc="down")