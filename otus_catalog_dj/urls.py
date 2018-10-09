from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'catalog.views.error_404_view'
handler500 = 'catalog.views.error_500_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('catalog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
