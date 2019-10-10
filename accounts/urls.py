from rest_framework.routers import DefaultRouter

from accounts.views import AuthViewSet

router = DefaultRouter()
router.register(r'', AuthViewSet)
urlpatterns = router.urls
