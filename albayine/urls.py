from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from home import views as homeViews
from django.contrib import admin
admin.site.site_header = "Abdelbari Portfolio Website"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeViews.index,name='home_index'),
    path('contact-me',homeViews.contactMe,name='contactme'),
    path('portfolio-detail/<int:id>',homeViews.portfoliodetail,name='portfoliodetail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
