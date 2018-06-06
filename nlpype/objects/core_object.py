import re
from abc import ABCMeta


class CoreObject(metaclass=ABCMeta):
    """
    Base class for all CoreNLP wrappers. Passes unmatched attributes on to the
    underlying Java object, and translates Python __str__ and __repr__ calls
    into Java toString() calls.
    """
    def __init__(self, base, pipeline):
        """
        Initializes the wrapper

        :param base: The underlying Java object
        :param pipeline: The pipeline that was originally used to parse this object
        """
        self._base = base
        self._pipeline = pipeline

    def __getattr__(self, attr):
        """
        Forwards any unknown attributes on to the base object

        Refer to the CoreNLP JavaDocs for the API.

        :param attr: The attribute call that couldn't find a match
        """
        return getattr(self._base, attr)

    def __repr__(self):
        """
        Translates Python's str() and repr() into Java's .toString()
        """
        return self._base.toString()

    def _get_base(self, obj):
        """
        Helper method for finding the underlying Java object of an object that
        could be either a wrapper or a Java object
        
        :param obj: The object to unwrap
        :return: The underlying Java object of obj
        """
        if isinstance(obj, CoreObject):
            return obj._base
        return obj


def cache(func):
    """
    Used as a decorator to cache the output of function calls on the object
    that was called

    :param func: A function to decorate
    :return: A decorated function that stores the output of the inner
             function if there is no cached value, and returns the cached value
             if there is
    """
    def wrapper(self, *args, **kwargs):
        key = '_' + func.__name__
        if hasattr(self, key):
            return getattr(self, key)
        value = func(self, *args, **kwargs)
        setattr(self, key, value)
        return value
    return wrapper

