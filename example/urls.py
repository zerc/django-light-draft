import django
from django.conf.urls import include, url
from django.contrib import admin

from blog.urls import router

admin.autodiscover()

urlpatterns = [
    url(r'^', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
]
