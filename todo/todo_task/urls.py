from django.urls import include, path
from rest_framework import routers
from todo_task.views import TaskViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)


app_name = "todo_task"
urlpatterns = [
    path('', include(router.urls)),
]
