# -*- coding: utf-8 -*-
import re


def clean_str(s):
    return re.sub(r'\r|\t|\n', '', s).strip().encode('utf-8')


def clean_str_list(str_list):
    return filter(lambda x: len(x) > 0, map(clean_str, str_list))


def list_to_clean_str(str_list):
    return ' '.join(clean_str_list(str_list))
