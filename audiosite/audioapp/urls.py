from django.urls import path
from audioapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('text',views.text),
    path('download',views.download),
    path('video',views.video),

]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
