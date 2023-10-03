import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1200, 600

delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, 5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (5, 0),
}

def check_bound(obj_rct: pg.Rect):
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")

    kk_img_normal = pg.image.load("ex02/fig/3.png")
    kk_img_flying = pg.image.load("ex02/fig/3_flying.png")
    kk_rct = kk_img_normal.get_rect()
    kk_rct.center = (900, 400)
    kk_animation_cycle = 10
    kk_animation_counter = 0

    bd_img = pg.Surface((20, 20))
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()
    bd_rct.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    vx, vy = +5, +5

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key, mv in delta.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1]) 

        bd_rct.move_ip(vx, vy)
        yoko, tate = check_bound(bd_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1

        screen.blit(bg_img, [0, 0])

        # 1. 飛ぶ方向に従ってこうかとん画像を切り替える
        kk_animation_counter += 1
        if kk_animation_counter % kk_animation_cycle == 0:
            kk_img = kk_img_flying if kk_img == kk_img_normal else kk_img_normal
            kk_animation_counter = 0

        # 2. 時間とともに爆弾が加速する or 大きくなる
        vx += 0.1
        vy += 0.1

        # 3. 着弾するとこうかとん画像が切り替わる（ゲームオーバー前に）
        if kk_rct.colliderect(bd_rct):
            print("ゲームオーバー")
            return

        # 4. 爆弾がこうかとんに近づくように移動する
        if bd_rct.x < kk_rct.x:
            bd_rct.x += 1
        elif bd_rct.x > kk_rct.x:
            bd_rct.x -= 1
        if bd_rct.y < kk_rct.y:
            bd_rct.y += 1
        elif bd_rct.y > kk_rct.y:
            bd_rct.y -= 1

        screen.blit(kk_img, kk_rct)
        screen.blit(bd_img, bd_rct)
        pg.display.update()

        tmr += 1
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

