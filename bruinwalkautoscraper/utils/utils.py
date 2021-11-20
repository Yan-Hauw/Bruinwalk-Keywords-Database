# standard lib modules
import re


def string_to_number(string):
    return re.sub(r"[^0-9]", "", string)
