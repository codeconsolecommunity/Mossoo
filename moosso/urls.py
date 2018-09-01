from django.conf.urls import include, url
from django.contrib import admin
from shoesHandler import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'moosso.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
        url(r'^$',views.home, name='home'),
    url(r'^mark/(?P<mark>\w+)/',views.shoesByMark,name='shoes_by_mark'),
    url(r'^(?P<category>\w+)/(?P<pageNumber>\d+)/', views.shoesByCategory,name='shoes_by_category'),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
