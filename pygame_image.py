import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    bf_img = pg.transform.flip(bg_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    kcl = [(-1,-1),(-1,1),(-2,0),(1,0),(-1,0)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -tmr
        key_lst = pg.key.get_pressed()
        kc = 4
        if key_lst[pg.K_UP]:
            kc = 0
        if key_lst[pg.K_DOWN]:
            kc = 1
        if key_lst[pg.K_LEFT]:
            kc = 2
        if key_lst[pg.K_RIGHT]:
            kc = 3
        kk_rct.move_ip(kcl[kc])
        screen.blit(bg_img, [x, 0])
        screen.blit(bf_img, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        if x == -3199:
            tmr = 0
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()