import uuid


from django.db import models


class BaseTodo(models.Model):
    """
    Base class for this app
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    udpdated_at = models.DateTimeField("Updated At", auto_now=False)

    class Meta:
        abstract = True


class Task(BaseTodo):
    """
    Tasks to be created
    """
    UNDEFINED = 'UD'
    IN_PROGRESS = 'IP'
    COMPLETED = 'CP'
    TASK_STATUS_CHOICES = [
        (IN_PROGRESS, "In-Progress"),
        (COMPLETED, "Completed")
    ]
    title = models.CharField("Title", max_length=255)
    description = models.CharField("Description", max_length=255)
    status = models.CharField(
        max_length=3,
        choices=TASK_STATUS_CHOICES,
        default=UNDEFINED,
    )


class Comment(BaseTodo):
    """
    Comments for the tasks
    """
    task = models.ForeignKey(Task, related_name="task",
                             on_delete=models.PROTECT)
    comment = models.CharField("Comments", max_length=255)
