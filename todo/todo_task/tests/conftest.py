import random
from model_bakery.recipe import Recipe, foreign_key
import pytest
from django.utils import timezone
from faker import Faker
import factory
from todo_task.models import Task


STATUS_TYPES = ['IP', 'CP']
fake = Faker()


class TaskFactory(factory.Factory):
    class Meta:
        model = Task


@ pytest.fixture(autouse=True)
def enable_db_access(db):
    pass


@ pytest.fixture
def single_task():
    task = TaskFactory()
    task.udpdated_at = timezone.now()
    task.save()
    return task


@ pytest.fixture
def twenty_task():
    for i in range(20):
        task = TaskFactory()
        task.udpdated_at = timezone.now()
        task.save()
    return None
