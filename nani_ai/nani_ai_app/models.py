from django.db import models

class Users(models.Model):
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    timezone = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.email} ({self.first_name} {self.last_name})"


class Tasks(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    action_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    due = models.DateTimeField(null=True, blank=True)
    recurrence = models.CharField(max_length=50, null=True, blank=True)
    tags = models.JSONField(default=list, blank=True)
    source = models.CharField(max_length=50, choices=[('nani', 'Nani'), ('user', 'User')], default='user')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title} ({self.user.email})"
    
class Messages(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=50, choices=[('user', 'User'), ('nani', 'Nani')])
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    linked_task_id = models.ForeignKey(Tasks, on_delete=models.SET_NULL, null=True, blank=True, related_name='linked_messages')
