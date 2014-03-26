from django.forms.widgets import TextInput


class YmapCoordFieldWidget(TextInput):
    attrs = None

    def __init__(self, attrs=None):

        default = {'class': 'ymap_field', 'style': 'display:none'}
        if attrs:
            default.update(attrs)
        super(YmapCoordFieldWidget, self).__init__(default)

    class Media:
        js = ('http://api-maps.yandex.ru/2.0/?load=package.full&lang=ru-RU', 'django_ymap/init.js')