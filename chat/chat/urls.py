
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf.urls.static import static
from . import settings
from django.conf.urls import handler404, handler403, handler500




urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),#githube
    path('captcha/', include('captcha.urls')),
    path('', include('appchat.urls')),
    path('rooms/', include('room.urls'))
]
handler404 = 'appchat.views.error_404'
handler403 = 'appchat.views.error_403'


#
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)