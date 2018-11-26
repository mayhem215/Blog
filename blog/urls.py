from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include


urlpatterns = [
    url(r'^$', views.all, name='all'),
    url(r'^post/(?P<pk>\d+)/$', views.stat, name='stat'),
    url(r'^ ckeditor /', include ('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, )
urlpatterns += staticfiles_urlpatterns()
