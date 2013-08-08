class YmapAdmin(object):
    def formfield_for_dbfield(self, db_field, **kwargs):
        from django_ymap.fields import YmapCoord
        from django_ymap.widgets import YmapCoordFieldWidget

        request = kwargs.pop("request", None)
        if isinstance(db_field, YmapCoord):
            kwargs['widget'] = YmapCoordFieldWidget

        return db_field.formfield(**kwargs)