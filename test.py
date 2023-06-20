from PIL import Image
from PIL import ImageDraw
import math


def print_gex2(coord_x, coord_y, size, canvas):
    pdraw = ImageDraw.Draw(canvas)
    corners_coord = []

    for corner in range(6):
        angle_deg = 60 * corner + 30
        angle_rad = math.pi / 180 * angle_deg
        corner_coord = (coord_x + size * math.sin(angle_rad), coord_y + size * math.cos(angle_rad))
        corners_coord.append(corner_coord)

    pdraw.polygon(xy=corners_coord,
                  fill=(100, 0, 0, 127),
                  outline=(255, 255, 255, 255))


def print_field(coord_x, coord_y, size, position, canvas):
    pdraw = ImageDraw.Draw(canvas)
    corners_coord = [(coord_x, coord_y)]
    for corner in range(position, position+3):
        angle_deg = 60 * corner + 30
        angle_rad = math.pi / 180 * angle_deg
        corner_coord = (coord_x + size * math.sin(angle_rad), coord_y + size * math.cos(angle_rad))

        corners_coord.append(corner_coord)

    pdraw.polygon(xy=corners_coord,
                  fill=(0, 100, 0, 127),
                  outline=(255, 255, 255, 255))


size = 40
poly = Image.new('RGB', (512, 512), (0, 0, 0))
width = size * 2
height = math.sqrt(3) / 2 * width
center_x = 256
center_y = 256


print_gex2(center_x, center_y, size, poly)
print_gex2(center_x, center_y + height, size, poly)
print_gex2(center_x + (3/4*width), center_y + (height / 2), size, poly)
print_field(center_x, center_y, size, 6, poly)

poly.show()
