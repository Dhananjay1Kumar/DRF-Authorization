from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey('auth.user', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
