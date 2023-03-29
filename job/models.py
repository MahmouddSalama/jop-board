from django.db import models
JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

# Create your models here.
class Job(models.Model):

    title=models.CharField(max_length=100)
    # location
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    Published_ad=models.DateTimeField( auto_now=True, auto_now_add=False)
    vancany=models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experance = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title


