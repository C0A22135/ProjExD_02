import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1200, 600
BOMB_RADIUS = 10
BOMB_COLOR = (255, 0, 0)  # 赤色
vx = 5
vy = 5
KEY_MOVEMENTS = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, 5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (5, 0)
}

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect(topleft=(900, 400))
    clock = pg.time.Clock()
    tmr = 0

    # 爆弾Surfaceの作成
    bomb_surface = pg.Surface((BOMB_RADIUS * 2, BOMB_RADIUS * 2))
    bomb_surface.fill((0, 0, 0))
    pg.draw.circle(bomb_surface, BOMB_COLOR, (BOMB_RADIUS, BOMB_RADIUS), BOMB_RADIUS)
    bomb_surface.set_colorkey((0, 0, 0))
    bomb_rect = bomb_surface.get_rect()
    bomb_rect.x = random.randint(0, WIDTH - BOMB_RADIUS * 2)
    bomb_rect.y = random.randint(0, HEIGHT - BOMB_RADIUS * 2)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_lst = pg.key.get_pressed()
        dx, dy = 0, 0
        for key, (vx, vy) in KEY_MOVEMENTS.items():
            if key_lst[key]:
                dx += vx
                dy += vy
        kk_rect.move_ip(dx, dy)

        bomb_rect.move_ip(vx, vy)  # 爆弾の位置を移動

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect.topleft)
        screen.blit(bomb_surface, bomb_rect.topleft)  # 爆弾の表示
        pg.display.update()
        tmr += 1
        clock.tick(50)  # FPSを50に変更

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

