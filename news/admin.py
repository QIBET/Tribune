from django.contrib import admin
from .models import Article,tags, Editor

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
admin.site.register(Editor)
