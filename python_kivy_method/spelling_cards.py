# coding:utf-8
#!/usr/bin/env python

# This file is used to generate different sounds or spelling cards
from PIL import Image, ImageFont, ImageDraw
from words_sounds import *
import sys, string

optionset = set(['hiragana', 'katakana', 'sounds'])

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def generate_cards(card_type):
    sounds = basic_sounds

    if card_type == "hiragana":
        words = basic_hiragana
        font = ImageFont.truetype("./KaoriGel.ttf",50)
    elif card_type == "katakana":
        words = basic_katakana
        font = ImageFont.truetype("./KaoriGel.ttf",50)
    elif card_type == "sounds":
        font = ImageFont.truetype("./SourceSansPro-Regular.otf",50)
        words = sounds

    for i in range(len(words)):
        img = Image.new("RGBA",(200,200),(255,255,255,0))
        img = add_corners(img, 40)
        draw = ImageDraw.Draw(img)
        draw.text((65,65), words[i],font=font,fill=(0,0,0))
        img.save(sounds[i]+"_"+card_type+".png","PNG")

if __name__ == "__main__":
    par1 = sys.argv[1]
    par1 = par1.lower()
    if par1 in optionset:
        generate_cards(par1)
