from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    last_login = models.DateTimeField(auto_now=True)
    
class Question(models.Model):
    num_q = models.CharField(max_length=32, unique=True)
    question = models.CharField(max_length=200)
    type = models.CharField(max_length=32)
    parent = models.CharField(max_length=32, null=True)
    alias = models.CharField(max_length=64, null=True)
    
class Diligence(models.Model):
    dili_name = models.CharField(max_length=32, unique=True)
    date = models.DateTimeField(auto_now=True)
    
    def get_questions_answers(self, dili) -> Any:
        questions = {}
        for answer in Answer.objects.filter(diligence=dili):
            questions[answer.question.id] = [{'id_q': answer.question.id, 'num_q': answer.question.num_q, 'question': answer.question.question, 'type': answer.question.type, 'parent': answer.question.parent},{'id_res': answer.id , 'ai_res': answer.ai_res, 'answer': answer.answer, 'answer_type': answer.answer_type}]
        return questions
    
class Answer(models.Model):
    ai_res = models.CharField(max_length=500, null=True)
    answer = models.CharField(max_length=200, null=True)
    answer_type = models.CharField(max_length=32)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    diligence = models.ForeignKey(Diligence, on_delete=models.CASCADE)
    
class Mapping(models.Model):
    num_map = models.CharField(max_length=32, primary_key=True, unique=True)
    num_q = models.ForeignKey(Question, on_delete=models.CASCADE)
    
