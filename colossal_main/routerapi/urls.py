from django.urls import include, path
from rest_framework import routers
from .views import RouterView

router = routers.DefaultRouter()
router.register(r"routerapi", RouterView)

urlpatterns = [
    path('', include(router.urls)),
    path('routerapi/', include('rest_framework.urls'))
]