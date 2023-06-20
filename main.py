#TODO Добавить sqlite для сбора статистики

from datetime import datetime
from time import sleep

from config import n_type, m_field, patt, field_desc

from BoardGameDeck import BoardGameDeck
from BoardGameMap import BoardGameMap
from BoardGameGex import BoardGameGex
from BoardGameField import BoardGameField
from Printer import Printer

from PIL import Image
from PIL import ImageDraw


list_i = []
bgd = BoardGameDeck(n_type, m_field, patt, field_desc)
bg = Image.new('RGB', (512, 512), (0, 0, 0))
for i in range(1000):
    bgm = BoardGameMap(bgd, 7)
    Printer.img_print_map(bgm, bg)
    bg.save(f'pic/map_{i}_{datetime.now()}.jpg')
    print(f'{i}_{datetime.now()}', bgm.get_stat())