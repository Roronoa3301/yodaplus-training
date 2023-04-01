from django.test import TestCase
# Create your tests here.
from rest_framework.test import APIClient
from todo_task.models import Task
import json
client = APIClient()


def test_count_tasks(single_task):
    response = client.get('http://127.0.0.1:8000/tasks/')
    data = json.loads(response.content)
    count = data.get('count', None)
    assert 1 == count


def test_top_five(twenty_task):
    response = client.get('http://127.0.0.1:8000/tasks/top_five/')
    data = json.loads(response.content)
    assert 5 == len(data)
