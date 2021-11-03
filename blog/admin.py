from django.contrib import admin
from . models import Category , Post , Comment , Like
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','is_published','posted')
    list_filter = ('is_published','posted')
    list_editable = ('is_published',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','created','is_resolved')
    list_filter = ('is_resolved','created')
    list_editable = ('is_resolved',)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('particular_post','name','likes')
    list_filter = ( )
    list_editable = ()


admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Like,LikeAdmin)