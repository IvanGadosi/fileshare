from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fileshare.urls')),
    path('', include('contact.urls')),
    path('', include('pricing.urls')),
    path('pricing/', include('paypal.standard.ipn.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'fileshare.views.view_404' 