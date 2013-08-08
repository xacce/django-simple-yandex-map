from django.db import models
from django.forms.fields import CharField
from django_ymap.widgets import YmapCoordFieldWidget


class YmapCoord(models.CharField):
    def __init__(self, start_query, size_width=500, size_height=500, **kwargs):
        self.start_query, self.size_width, self.size_height = start_query, size_width, size_height
        super(YmapCoord, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        # defaults = {'form_class': YmapCoordFormField}
        # defaults.update(kwargs)
        kwargs['widget'] = kwargs['widget'](attrs={
            "data-start_query": self.start_query,
            "data-size_width": self.size_width,
            "data-size_height": self.size_height,
        })
        return super(YmapCoord, self).formfield(**kwargs)