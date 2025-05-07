import pygame as pg

class FontSprite(pg.sprite.Sprite):
    def __init__(self, x, y, text, font_name, font_size, placement="center", color="#000000"):
        super().__init__()
        
        font = pg.font.SysFont(font_name, font_size)
        self.image = font.render(text, False, color)
        self.rect = self.image.get_rect(midleft = (x, y))

        if placement == "midleft":
            self.rect = self.image.get_rect(midleft = (x, y))
        elif placement == "center":
            self.rect = self.image.get_rect(center = (x, y))
        elif placement == "midbottom":
            self.rect = self.image.get_rect(midbottom = (x, y))
        elif placement == "midtop":
            self.rect = self.image.get_rect(midtop = (x, y))
        elif placement == "midright":
            self.rect = self.image.get_rect(midright = (x, y))