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

bgm = BoardGameMap(bgd, 7)
Printer.img_print_map(bgm, bg)
bgm.get_map()[1].set_center((-43.3013+150, 25.0+150))
bgm.get_map()[1].set_step_angel(2)
Printer.img_print_gex(bgm.get_map()[1], bg)
Printer.show_board(bg)

for i in bgm.get_map():
    print(i.get_center())
