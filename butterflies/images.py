from params import root_dir
import Image
from pytesseract import image_to_string


def get_catalog_file(num=2):
    file = "%s/data/butterflies_%s.jpg" % (root_dir, num)
    return file


def get_image_as_string(num=2):
    file = get_catalog_file(num=num)
    print "file: %s" % file
    return image_to_string(Image.open(file))
