from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


from modelos_usuarios.views import ListCreateModeloUsuarioView, CreateUpdateDeleteModeloUsuarioView, ListModelosPorUsuarioView

router = routers.DefaultRouter()
# router.register("endpoint-teste", EndpointTesteViewSet, basename="Basename do endpoint-teste")

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path("modelo", ListCreateModeloUsuarioView.as_view()),
    path("modelo/<int:pk>", CreateUpdateDeleteModeloUsuarioView.as_view()),
    path("usuario/<int:user_id>/modelos", ListModelosPorUsuarioView.as_view())
]