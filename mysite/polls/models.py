from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
  # these variables are a Field instance, a column in the db
  # char field: required param max_length
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  # ForeignKey defines a relationship. Choice is related to a single Question
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

