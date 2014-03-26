from django.db import models


class YmapCoord(models.CharField):
    def __init__(self, start_query, size_width=500, size_height=500, **kwargs):
        self.start_query, self.size_width, self.size_height = start_query, size_width, size_height
        super(YmapCoord, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        if kwargs.has_key('widget'):
            kwargs['widget'] = kwargs['widget'](attrs={
                "data-start_query": self.start_query,
                "data-size_width": self.size_width,
                "data-size_height": self.size_height,
            })
        return super(YmapCoord, self).formfield(**kwargs)