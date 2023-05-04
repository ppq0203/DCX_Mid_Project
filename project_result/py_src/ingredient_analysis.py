
from function.ingredient_kind import get_kind
from function.length_ocr import length_from_image
from function.ea_weight_length_function import calc_quantity, calc_weight


def img_anl(img_url):
    name = get_kind(img_url)
    length = length_from_image(img_url)
    quantity = calc_quantity(length, name)
    weight = calc_weight(quantity, name)
    return name, length, quantity, weight


img_url = "../img/test_img/po1.jpg"
print(img_anl(img_url))
