from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Editor(models.Model):

    class Meta:
        db_table = 'Editor'

    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, default='John')
    last_name = models.CharField(max_length=40)


    def __str__(self):
        full_name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        return full_name


class Newspaper(models.Model):

    class Meta:
        db_table = 'Newspaper'

    name = models.CharField(max_length=40)
    edition_index = models.IntegerField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    price = models.FloatField()
    
    def __str__(self):
        return self.name


class PostOffice(models.Model):

    class Meta:
        db_table = 'Post Office'
    
    number = models.IntegerField(default=22)
    address = models.CharField(max_length=40)

    def __str__(self):
        return 'Post Office №' + str(self.number)


class PrintingHouse(models.Model):

    class Meta:
        db_table = 'Printing House'

    STATUSES = (('Working', 'Working'),
                ('Closed', 'Closed'))

    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    status = models.CharField(max_length=7, choices=STATUSES)

    def __str__(self):
        return self.name


class InStock(models.Model):

    class Meta:
        db_table = 'In Stock'

    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE)
    printing_house = models.ForeignKey(PrintingHouse, on_delete=models.CASCADE)
    print_run = models.IntegerField()
