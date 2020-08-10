from django.contrib import admin

# Register your models here.
from .models import TheftData, Cur1, Cur2, Source, \
Cur1DataModel, Cur2DataModel, SourceDataModel

admin.site.register(TheftData)
admin.site.register(Cur1)
admin.site.register(Cur2)
admin.site.register(Source)
admin.site.register(Cur1DataModel)
admin.site.register(Cur2DataModel)
admin.site.register(SourceDataModel)