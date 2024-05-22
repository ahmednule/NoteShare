from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
  """
  Model for notes
  """
  note_id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  content = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)
  is_public = models.BooleanField(default=False)

  def __str__(self):
    return self.title