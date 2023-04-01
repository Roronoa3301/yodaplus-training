import os
from model_bakery.recipe import Recipe, foreign_key
import random
from faker import factory, Faker
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")


import django
django.setup()




from todo_task.models import Task, Comment




fake = Faker()


STATUS_TYPES = ['IP', 'CP']
for k in range(100):
    task = Recipe(Task,
                  title=fake.sentence(
                      nb_words=4, variable_nb_words=True),
                  status=STATUS_TYPES[int(random.random()*len(STATUS_TYPES))])
   
    comment = Recipe(Comment,
                    task=foreign_key(task),
                    comment=fake.sentence(
                        nb_words=6, variable_nb_words=True)
                    )
    comment.make()
       
