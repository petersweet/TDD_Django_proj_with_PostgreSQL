from django.contrib import admin
from .models import Author
from .models import Publisher
from .models import Article
# Register your models here.

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Article)

