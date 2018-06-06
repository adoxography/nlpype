import re
from abc import ABCMeta


class CoreObject(metaclass=ABCMeta):
    def __init__(self, base):
        self._base = base

    def __getattr__(self, attr):
        return getattr(self._base, attr)

    def __repr__(self):
        return self._base.toString()

    def _get_base(self, obj):
        if isinstance(obj, CoreNLPObject):
            return obj._base
        return obj


def cache(func):
    def wrapper(self, *args, **kwargs):
        key = '_' + func.__name__
        if hasattr(self, key):
            return getattr(self, key)
        value = func(self, *args, **kwargs)
        setattr(self, key, value)
        return value
    return wrapper

