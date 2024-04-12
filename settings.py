import pygame as pg
vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32)
BG_COLOR = (100,22,100)

PIECE_COLORS = [
    "orange",
    "blue",
    "yellow",
    "red",
    "purple",
]

ANI_INTERVAL = 200 # animation time interval
FAST_ANI_INTERVAL = 15

TILE_SIZE = 32
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE
WIN_W , WIN_H = FIELD_W*1.7 , FIELD_H*1.0
WIN = WIN_W*TILE_SIZE , WIN_H*TILE_SIZE

INIT_POS_OFFSET = vec(FIELD_W//2-1,0)
PREV_POS_OFFSET = vec(WIN_W*0.8 , WIN_H*0.5)

SCORE_SHEET = {
    0:0,
    1:40,
    2:100,
    3:300,
    4:1200,
}

MOV_DIREC = {
    "left": vec(-1,0),
    "right": vec(1,0),
    "down": vec(0,1),
}

TETROS = {
    'T':[(0,0),(-1,0),(1,0),(0,-1)],
    'O':[(0,0),(0,-1),(1,0),(1,-1)],
    'J':[(0,0),(-1,0),(0,-1),(0,-2)],
    'L':[(0,0),(1,0),(0,-1),(0,-2)],
    'I':[(0,0),(0,1),(0,-1),(0,-2)],
    'S':[(0,0),(-1,0),(0,-1),(1,-1)],
    'Z':[(0,0),(1,0),(0,-1),(-1,-1)],
}