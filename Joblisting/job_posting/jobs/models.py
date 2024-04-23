from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserInterest(models.Model):
    Job = models.ForeignKey(Job, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Resume = models.FileField(upload_to='resumes/')
    Message = models.TextField()

    def __str__(self):
        return self.name
