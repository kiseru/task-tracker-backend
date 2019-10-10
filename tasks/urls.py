from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet

router = DefaultRouter()
router.register('', TaskViewSet)
urlpatterns = router.urls
