django-simple-yandex-map
========================

Простая интеграция Яндекс карт в панель администратора django

![alt=""](http://ubuntuone.com/4UYu7wU8lZhE5Z0P7FdEO3)
### Установка
===
Скопировать папку django_ymap в корневую директорию вашего django проекта.
Добавить ```django_ymap``` в ```INSTALLED_APPS``` (файл ```settings.py```)

```
INSTALLED_APPS = (
    ...
    'django_ymap',
    ... 
)

```

===

### Использование
Добавьте в вашу модель поле ```django_ymap.fields.YmapCoord```

```
from django.db import models

from django_ymap.fields import YmapCoord


class Record(models.Model):
    title = models.CharField(max_length=200)
    address = YmapCoord(max_length=200, start_query=u'Россия', size_width=500, size_height=500)
    alternative_address = YmapCoord(max_length=200, start_query=u'Австралия', size_width=500, size_height=500)
```

У поля YmapCoord есть 3 параметра ```start_query``` - что будет показываться на карте при создании нового объекта,```size_width``` - ширина карты,```size_height``` - высота карты. 

Для отображения Яндекс карты в панели администратора нужно унаследоваться от ```django_ymap.admin.YmapAdmin```

```
from django.contrib import admin
from django_test.models import Record
from django_ymap.admin import YmapAdmin


class RecordAdmin(YmapAdmin, admin.ModelAdmin):
    pass


admin.site.register(Record, RecordAdmin)
```
Где ```Record``` ваша модель.

===
Возможно, для корректой работы вам потребуется выполнить ```collectstatic```.
