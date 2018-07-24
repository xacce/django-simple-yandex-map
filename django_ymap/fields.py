#* coding: utf-8
from django.db import models


class YmapCoord(models.CharField):
    def __init__(self, start_query=u'Россия', size_width=500, size_height=500, **kwargs):
        self.start_query, self.size_width, self.size_height = start_query, size_width, size_height
        super(YmapCoord, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        if 'widget' in kwargs:
            kwargs['widget'] = kwargs['widget'](attrs={
                "data-start_query": self.start_query,
                "data-size_width": self.size_width,
                "data-size_height": self.size_height,
            })
        return super(YmapCoord, self).formfield(**kwargs)

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        # We'll just introspect the _actual_ field.
        try:
            from south.modelsinspector import introspector
            field_class = self.__class__.__module__ + "." + self.__class__.__name__
            args, kwargs = introspector(self)
            # That's our definition!
            kwargs.update({
                'start_query': repr(self.start_query),
                'size_width': repr(self.size_width),
                'size_height': repr(self.size_height),
            })
            return ('django_ymap.fields.YmapCoord', args, kwargs)
        except ImportError:
            pass


    def deconstruct(self):
        name, path, args, kwargs = super(YmapCoord, self).deconstruct()
        if "start_query" in kwargs:
            del kwargs["start_query"]
        if 'size_width' in kwargs:
            del kwargs["size_width"]
        if 'size_height' in kwargs:
            del kwargs["size_height"]
        return name, path, args, kwargs

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^django_ymap\.fields\.YmapCoord"])
except ImportError:
    pass