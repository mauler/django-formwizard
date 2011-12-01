#!/usr/bin/env python
#-*- coding:utf-8 -*-

try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4


class lazy_property(property):
    """
    A property that works with subclasses by wrapping the decorated
    functions of the base class.
    """
    def __new__(cls, fget=None, fset=None, fdel=None, doc=None):
        if fget is not None:
            @wraps(fget)
            def fget(instance, instance_type=None, name=fget.__name__):
                return getattr(instance, name)()
        if fset is not None:
            @wraps(fset)
            def fset(instance, value, name=fset.__name__):
                return getattr(instance, name)(value)
        if fdel is not None:
            @wraps(fdel)
            def fdel(instance, name=fdel.__name__):
                return getattr(instance, name)()
        return property(fget, fset, fdel, doc)

