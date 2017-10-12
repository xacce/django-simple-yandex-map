from django.apps.config import AppConfig


class SimpleYandexMap(AppConfig):
    name = "django_ymap"
    def ready(self):
        try:
            from model_mommy.generators import add
        except ImportError:
            pass
        else:
            from random import randint
            from django_ymap.fields import YmapCoord
            add(YmapCoord,lambda: '{},{}'.format(randint(-50,50),randint(-50,50)))

