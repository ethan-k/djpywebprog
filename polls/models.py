from django.db import models

# Create your models here.


from django.db import models


class Question(models.Model):
    question_next = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):  # __str__ on Python 3
        return self.question_next


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):  # __str__ on Python 3
        return self.choice_text