from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social.urls', namespace='social')),
    path('user/', include('users.urls', namespace='user')),
    path('api/v1/', include('api.urls', namespace='apiv1')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    