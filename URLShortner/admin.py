from django.contrib import admin
from URLShortner.models import OriginalURL, URLid

class OriginalURLAdmin(admin.ModelAdmin):
    list_display = ('original_url',)

class URLidAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'url_id',)


admin.site.register(OriginalURL, OriginalURLAdmin)
admin.site.register(URLid, URLidAdmin)

