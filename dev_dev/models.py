from django.db import models
from django.utils import timezone
from custom_user_model.models import Custom_user
from dev_point import settings
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class ask_question(models.Model):
    question_title = models.TextField(max_length='10000',blank=True,null=True)
    question       = models.TextField(max_length='100000')
    user           = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE)
    view           = models.IntegerField(default=0,null=True,blank=True)
    create         = models.DateTimeField(auto_now=True)
    like           = models.ManyToManyField(Custom_user,related_name='like',blank=True)
    def __str__(self):
        return self.question_title
    def like_add(self):
        return self.like.count()
class answer_question(models.Model):
    # id_answer = models.ForeignKey(ask_question,related_name="id_answer",default=True,null=False,blank=True,on_delete=models.CASCADE)
    answer          = models.TextField(max_length='10000')
    create          = models.DateTimeField(auto_now=True)
    user_answer     = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE)
    question        = models.ForeignKey(ask_question,null=True,blank=True,on_delete=models.CASCADE)
    answer_like     = models.ManyToManyField(Custom_user,related_name='answer_like',blank=True)
    def __str__(self):
        return self.answer
# class like_add(models.Model):
#     user_liked = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE)
#     question = models.ForeignKey(ask_question,null=True,blank=True, on_delete = models.CASCADE)
#     val = models.BooleanField(default=False)
# question        = RichTextUploadingField()
# answer         = models.ManyToManyField(answer_question,null=True,blank=True)
class comment_model(models.Model):
    comment     = models.TextField(max_length='9000')
    create      = models.DateTimeField(auto_now=True)
    question        = models.ForeignKey(ask_question,null=True,blank=True,on_delete=models.CASCADE)
    user_answer = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE)
    answer      = models.ForeignKey(answer_question,null=True,blank=True,on_delete=models.CASCADE)

# answer = RichTextUploadingField()
