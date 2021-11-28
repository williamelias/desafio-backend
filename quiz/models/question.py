from django.db import models
from .quiz import *

class Question(models.Model):
    enunciation = models.CharField(max_length=128)
    # options = models.ForeignKey(
    #   Option,on_delete=models.CASCADE
    # )
    # answer = models.CharField(
    #   max_length=100
    # )
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    @property
    def is_available(self):
        if not hasattr(self,'options'):
            return False
        return self.options.all().count() == 3

class Option(models.Model):
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="options",null=True)

    # class Meta:
    #   unique_together =['is_correct','question']