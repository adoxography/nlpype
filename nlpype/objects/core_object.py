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

