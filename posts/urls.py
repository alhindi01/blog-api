from django.urls import path

# from .views import PostList, PostDetail, UserList, UserDetail  # new
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

# using routers
router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")
urlpatterns = router.urls

# normal urls
# urlpatterns = [
#     path("users/", UserList.as_view()),  # new
#     path("users/<int:pk>/", UserDetail.as_view()),  # new
#     path("", PostList.as_view()),
#     path("<int:pk>/", PostDetail.as_view()),
# ]
