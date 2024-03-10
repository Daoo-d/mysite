from django.contrib import admin
from .models import Post,Author

class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    

# Register your models here.
admin.site.register(Post,AdminPost)
admin.site.register(Author)
