# -*- coding: utf-8 -*-
import re


def _invert_dict(inp):
    d = {}
    for (k, vs) in inp.iteritems():
        for v in vs:
            d[v] = k
    return d


_clean_chars = {
    '': ['\r', '\t', '\n'],
    '-': [u'\u2010', u'\u2011', u'\u2012', u'\u2013', u'\u2014', u'\u2015'],
    ' ': [u'\u2016', u'\u2017', u'\00a0'],
    "'": [u'\u2018', u'\u2019', u'\u201A', u'\u201B'],
    '"': [u'\u201C', u'\u201D', u'\u201E', u'\u201F']
}

_dirty_chars = _invert_dict(_clean_chars)
_regex = re.compile("(%s)" % "|".join(map(re.escape, _dirty_chars.keys())),
                    re.UNICODE)


def _multiple_replace(text):
    # For each match, look-up corresponding value in dictionary
    return _regex.sub(lambda mo: _dirty_chars[mo.string[mo.start():mo.end()]],
                      text)


def clean_str(s):
    return _multiple_replace(s).strip().encode('utf-8')


def clean_str_list(str_list):
    return filter(lambda x: len(x) > 0, map(clean_str, str_list))


def list_to_clean_str(str_list):
    return ' '.join(clean_str_list(str_list))
