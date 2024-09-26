from django.db import models
#from django-utils.choices import Choice, Choices
# Create your models here.

class Hotel(models.Model):
    name=models.TextField(max_length=20)
    address=models.TextField(max_length=40)
    desc=models.TextField(max_length=20)
    places=models.IntegerField(max_length=4)
    types=models.TextField()
    facilities=models.TextField()
    owner=models.TextField(max_length=20)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Hotel,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    datein=models.DateField(default='2006-06-06')
    dateout=models.DateField(default='2006-06-06')
    list=((1,1),(2,2),(3,3)
          ,(4,4),(5,5),(6,6)
          ,(7,7),(8,8),(9,9),(10,10))
    rating=models.IntegerField(max_length=2,choices=list,default='1')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
