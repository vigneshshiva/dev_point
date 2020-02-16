from django.contrib import admin
from .models import ask_question,answer_question,comment_model
admin.site.register(ask_question)
admin.site.register(answer_question)
admin.site.register(comment_model)

# Register your models here.
