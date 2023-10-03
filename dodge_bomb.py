import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1100, 600

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    # 爆弾Surfaceを作成
    bomb_radius = 10
    bomb_color = (255, 0, 0)
    bomb_img = pg.Surface((2 * bomb_radius, 2 * bomb_radius), pg.SRCALPHA)
    pg.draw.circle(bomb_img, bomb_color, (bomb_radius, bomb_radius), bomb_radius)
    bomb_img.set_colorkey((0, 0, 0))

    clock = pg.time.Clock()
    tmr = 0

    bomb_x = random.randint(0, WIDTH - 2 * bomb_radius)
    bomb_y = random.randint(0, HEIGHT - 2 * bomb_radius)
    vx, vy = 5, 5

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])

        # 爆弾を表示
        screen.blit(bomb_img, (bomb_x, bomb_y))

        # 爆弾を移動
        bomb_x += vx
        bomb_y += vy

        # 画面端で跳ね返る
        if bomb_x <= 0 or bomb_x >= WIDTH - 2 * bomb_radius:
            vx *= -1
        if bomb_y <= 0 or bomb_y >= HEIGHT - 2 * bomb_radius:
            vy *= -1

        pg.display.update()
        tmr += 1
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

