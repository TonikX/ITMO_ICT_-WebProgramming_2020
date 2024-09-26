from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Homework(models.Model):
    discipline = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    issue_date = models.DateField()
    time_for_doing = models.DurationField()
    task_text = models.TextField()
    fine_info = models.TextField()

    class Meta:
        verbose_name = "Homework"
        verbose_name_plural = "Homeworks"

    def __str__(self):
        return self.discipline+" "+self.issue_date.strftime("%d/%m/%Y")


class Comment(models.Model):
    CType = (
        ('вопрос', 'вопрос'),
        ('найдена ошибка', 'найдена ошибка'),
        ('иное', 'иное'))
    IType = (
        ('высочайшая', 'высочайшая'),
        ('высокая', 'высокая'),
        ('средняя', 'средняя'),
        ('низкая', 'низкая'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст")
    type = models.CharField(verbose_name="Тип", choices=CType, max_length=14)
    importance = models.CharField(verbose_name="Важность", choices=IType, max_length=10)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
