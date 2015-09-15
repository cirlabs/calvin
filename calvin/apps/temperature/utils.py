import os
import random
import glob
import re
import fnmatch
import uuid

from PIL import Image, ImageFont, ImageDraw
# from __future__ import print_function

from django.conf import settings


def get_random_photo(dir_path):
    files = [f for f in os.listdir(dir_path) if re.match(r'\S+\.jpg', f.lower())]
    return os.path.join(dir_path, random.choice(files))


def build_image(message):
    media_dir = os.path.join(settings.BASE_DIR, 'media')

    random_image = get_random_photo(media_dir)

    im = Image.open(random_image)

    font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'fonts', 'home_sweet_home.ttf'), im.size[0]/10)
    font_color = (255, 255, 255)

    draw = ImageDraw.Draw(im)

    text_x, text_y = font.getsize(message)
    x = (im.size[0] - text_x)/2
    y = (im.size[1] - text_y)/2
    draw.text((x, y), message, font=font, fill=font_color)

    hed_message = 'HARPER SEZ'
    hed_x, hed_y = font.getsize(hed_message)
    hed_x = (im.size[0] - hed_x)/2
    hed_y = 10

    draw.text((hed_x, hed_y), hed_message, font=font, fill=font_color)

    my_uuid = uuid.uuid1()
    export_path = os.path.join(media_dir, 'finished_photos', '%s.jpg' % my_uuid)
    im.save(export_path)

    return {'image_path': export_path, 'uuid': my_uuid}
