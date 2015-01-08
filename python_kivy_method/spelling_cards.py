# coding:utf-8

# This file is used to generate images cards
from PIL import Image, ImageFont, ImageDraw

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

# main_sound = []

# extra_sound1 = []

# extra_sound2 = []

# words = main_sound+extra_sound1+extra_sound2

words = [u"あ",u"い",u"う",u"え",u"お",
        u"か", u"き", u"く", u"け", u"こ",
        u"さ", u"し", u"す", u"せ", u"そ",
        u"た", u"ち", u"つ", u"て", u"と",
        u"な", u"に", u"ぬ", u"ね", u"の",
        u"は", u"ひ", u"ふ", u"へ", u"ほ",
        u"ま", u"み", u"む", u"め", u"も",
        u"や", u"ゆ", u"よ",
        u"ら", u"り", u"る", u"れ", u"ろ",
        u"わ", u"を", u"ん"]

#extra_hiragana = [u"きゃ",　u"きゅ",　u"きょ",
#                  u"しゃ",  u"しゅ",　u"しょ"]





main_sound = ["a", "i", "u", "e", "o",
              "ka", "ki", "ku", "ke", "ko",
              "sa", "shi", "su", "se", "so",
              "ta", "chi", "tsu", "te", "to",
              "na", "ni", "nu", "ne", "no",
              "ha", "hi", "fu", "he", "ho",
              "ma", "mi", "mu", "me", "mo",
              "ya","yu","yo",
              "ra", "ri", "ru", "re", "ro",
              "wa", "o", "n"]

extra_sound1 = ["kya", "kyu", "kyo",
                "sha", "shu", "sho",
                "cha", "chu", "cho",
                "nya", "nyu", "nyo",
                "hya", "hyu", "hyo",
                "mya", "myu", "myo",
                "rya", "ryu", "ryo",
                "gya", "gyu", "gyo",
                "ja",  "ju",  "jo",
                "bya", "byu", "byo",
                "pya", "pyu", "pyo"]

extra_sound2 = ["ga", "gi", "gu", "ge", "go",
                "za", "ji", "zu", "ze", "zo",
                "da", "ji", "zu", "de", "do",
                "ba", "bi", "bu", "be", "bo",
                "pa", "pi", "pu", "pe", "po"]


sounds = main_sound#+extra_sound1+extra_sound2

font = ImageFont.truetype("./KaoriGel.ttf",50)

#draw.text((200,200), "Te")#,font=font)
for i in range(len(words)):
    img = Image.new("RGBA",(200,200),(255,255,255,0))
    img = add_corners(img, 40)
    draw = ImageDraw.Draw(img)
    draw.text((65,65), words[i],font=font,fill=(0,0,0))
    img.save(sounds[i]+"_Hiragana.png","PNG")
