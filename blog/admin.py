from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ( 'name','title','created_at')
    list_editable=('title',)



# Register your models here.
admin.site.register(Post, PostAdmin),





