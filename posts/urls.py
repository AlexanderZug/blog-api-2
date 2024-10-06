from rest_framework import routers
from .views import PostViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r"", PostViewSet, basename="posts")
router.register(r"users", UserViewSet, basename="users")

urlpatterns = router.urls
