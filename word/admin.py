from email._header_value_parser import Word
from django.contrib import admin


from .models import Post, Comment, Item

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Item)