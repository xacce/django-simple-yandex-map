class YmapAdmin(object):
    def formfield_for_dbfield(self, db_field, **kwargs):
        from django_ymap.fields import YmapCoord
        from django_ymap.widgets import YmapCoordFieldWidget

        if isinstance(db_field, YmapCoord):
            kwargs['widget'] = YmapCoordFieldWidget

        field = super(YmapAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        return field