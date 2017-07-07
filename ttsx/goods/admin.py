from django.contrib import admin
from models import GoodType,GoodInfo
# Register your models here.
class GoodInfoAdmin(admin.ModelAdmin):
    list_display = ['id','gname','gprice','gclick','gunit','isDelete','gstock','gtype']

class GoodTypeAdmin(admin.ModelAdmin):
    list_display = ['id','tname','isDelete']

admin.site.register(GoodType,GoodTypeAdmin)
admin.site.register(GoodInfo,GoodInfoAdmin)