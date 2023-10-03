import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1600, 900
BOMB_RADIUS = 10
BOMB_COLOR = (255, 0, 0)  # 赤色


def is_inside_screen(rect):
    return (0 <= rect.left and rect.right <= WIDTH, 0 <= rect.top and rect.bottom <= HEIGHT)

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect(topleft=(900, 400))
    clock = pg.time.Clock()
    tmr = 0

    KEY_MOVEMENTS = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, 5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (5, 0)
    }

    kk_images = {
        (0, -5): pg.transform.flip(pg.transform.rotozoom(kk_img, 90, 1.0), True,True ),  # 下向き
        (0, 5): pg.transform.rotozoom(kk_img, 45, 1.0),   # 上向き
        (-5, 0): pg.transform.rotozoom(kk_img, 0, 1.0),  # 右向き
        (5, 0): pg.transform.flip(pg.transform.rotozoom(kk_img, 0, 1.0), True, False),  # 左向き
        (-5, -5): pg.transform.rotozoom(kk_img, -45, 1.0),  # 右下斜め
        (5, -5): pg.transform.flip(pg.transform.rotozoom(kk_img, -45, 1.0), True, False), # 左下斜め
        (-5, 5): pg.transform.rotozoom(kk_img, 45, 1.0), # 右上斜め
        (5, 5): pg.transform.flip(pg.transform.rotozoom(kk_img, 45, 1.0), True, False), # 左上斜め
    }


    # 爆弾Surfaceの作成
    bomb_surface = pg.Surface((20, 20))
    bomb_surface.fill((0, 0, 0))  # 黒で塗りつぶす
    pg.draw.circle(bomb_surface, BOMB_COLOR, (10, 10), 10)  # 赤い円を描画
    bomb_surface.set_colorkey((0, 0, 0))  # 黒を透明にする

    # 爆弾Rectのランダムな位置を設定
    bomb_rect = bomb_surface.get_rect()
    bomb_rect.topleft = (random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20))

    # 爆弾の移動方向を設定（初期値はTrue）
    bomb_dir_x = True
    bomb_dir_y = True

    # 爆弾の速度を設定
    vx = 5
    vy = 5

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_lst = pg.key.get_pressed()
        dx, dy = 0, 0
        for key, (vx_key, vy_key) in KEY_MOVEMENTS.items():
            if key_lst[key]:
                dx += vx_key
                dy += vy_key
        kk_rect.move_ip(dx, dy)
        inside_x, inside_y = is_inside_screen(kk_rect)
        if not inside_x:
            kk_rect.move_ip(-dx, 0)
        if not inside_y:
            kk_rect.move_ip(0, -dy)

        # 爆弾の移動
        bomb_rect.move_ip(vx, vy)
        inside_x, inside_y = is_inside_screen(bomb_rect)
        if not inside_x:
            vx = -vx  # 速度の符号を反転
        if not inside_y:
            vy = -vy  # 速度の符号を反転

        # こうかとんと爆弾が衝突したかどうかを判定
        if kk_rect.colliderect(bomb_rect):
            return  # 衝突した場合、main関数からreturnする

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_images.get((dx, dy), kk_img), kk_rect.topleft)
        screen.blit(bomb_surface, bomb_rect.topleft)  # 爆弾の表示
        pg.display.update()
        tmr += 1
        clock.tick(50)  # FPSを50に変更

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()