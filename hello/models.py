from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    objects = None
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_owner')
    content = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content) + ' (' + str(self.owner) + ')'

    class Meta:
        ordering = ('-pub_date',)

