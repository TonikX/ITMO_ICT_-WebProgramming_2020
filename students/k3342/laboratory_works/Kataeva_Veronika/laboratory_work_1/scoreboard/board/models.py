from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Team(models.Model):

    class Meta:
        db_table = 'Team'

    team_name = models.CharField(max_length=40)
    team_country = models.CharField(max_length=20)

    def __str__(self):
        return self.team_name


class Car(models.Model):

    class Meta:
        db_table = 'Car'

    car_number = models.IntegerField()
    car_description = models.CharField(max_length=40)
    
    def __str__(self):
        full = str(self.car_number) + ', ' + self.car_description
        return full



class Racer(models.Model):

    class Meta:
        db_table = 'Racer'

    CLASSES_OF_LICENSES = (('Grade A', 'Grade A'),
                           ('Grade B', 'Grade B'),
                           ('Grade C', 'Grade C'),
                           ('International Grade A', 'International Grade A'),
                           ('International Grade B', 'International Grade B'),
                           ('International Grade C', 'International Grade C'))

    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    experience = models.IntegerField()
    grade_of_license = models.CharField(max_length=21, choices=CLASSES_OF_LICENSES)
    description = models.CharField(max_length=150)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

class Race(models.Model):

    class Meta:
        db_table = 'Race'

    race_name = models.CharField(max_length=20)
    series = models.CharField(max_length=20)
    year = models.IntegerField()
    winner = models.ForeignKey(Racer, on_delete=models.CASCADE)
    
    def __str__(self):
        full = str(self.year) + ' ' + self.race_name
        return full


class Comment(models.Model):

    class Meta:
        db_table = 'Comment'

    TYPES_OF_TAGS = (('Collaboration', 'Collaboration'),
                     ('Race', 'Race'),
                     ('Other', 'Other'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    racer = models.ForeignKey(Racer, on_delete=models.CASCADE)
    text = models.TextField('Comment')
    created = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=13, choices=TYPES_OF_TAGS)


    def __str__(self):
        return "{}".format(self.user)
