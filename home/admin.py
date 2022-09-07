from django.contrib import admin

from home.models import Media, Skill, Education, userprofile, Portfolio, Category, About, Experience, Images, Message


# Register your models here.
class ImageInline(admin.TabularInline):
    model=Images
    extra = 2
    fields = ('image',)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['title', 'symbol', 'link', 'status']
    list_filter = ['status']
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'Percentage','color', 'status']
    list_filter = ['status']
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject', 'status']
    readonly_fields  = ['name','email','subject','message']
    list_filter = ['status']
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title', 'instName', 'start','end','status']
    list_filter = ['status']
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','image_tag', 'status']
    list_filter = ['status']
    inlines = [ImageInline,]
admin.site.register(Experience)
admin.site.register(Message,MessageAdmin)
admin.site.register(About)
admin.site.register(Category)
admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(userprofile)
admin.site.register(Media, MediaAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Education,EducationAdmin)
