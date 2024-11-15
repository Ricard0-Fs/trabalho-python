from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from eventos.views import EventoViewSet, ParticipanteViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'participantes', ParticipanteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/admin/')),
]
