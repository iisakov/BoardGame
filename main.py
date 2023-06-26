#TODO Закончить разработку после достижения целей: 1) Отрисовки начальной карты с первым ходом игроков.

from config import n_type, m_field, patt, field_desc

from Components import BoardGameDeck, BoardGameMap
from Generators import VectorGenerator

from PIL import Image

list_i = []
bgd = BoardGameDeck(n_type, m_field, patt, field_desc)
bg = Image.new('RGB', (512, 512), (0, 0, 0))

bgm = BoardGameMap(bgd, 7)

print(VectorGenerator.gen((1, 2)))
