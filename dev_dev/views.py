from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from custom_user_model.models import Custom_user
from . forms import ask_Question_Form,Answer_Question_Form
from custom_user_model.forms import UserForm,UserLoginForm
from .models import ask_question,comment_model,answer_question
import random
from . import models
from django.template.loader import render_to_string
from django.db.models import F
from dev_point.settings import EMAIL_HOST_USER
import socket
from django.core.mail import send_mail
from custom_user_model.models import Custom_user
def intro(request):
    user = UserForm()
    form = UserLoginForm()
    return render(request,'html/intro.html',{'user':user,'form':form})

def home(request):
    user = UserForm()
    form = UserLoginForm()
    form_ans = ask_Question_Form()
    return render(request,'html/home.html',{'form_ans':form_ans,'user':user,'form':form})
# def modal(request):
#     user = UserForm()
#     form_login = UserLoginForm()
#     form = ask_Question_Form()
#     return render(request,'html/modal.html',{'form':form,'user':user,'form_login':form_login})

@csrf_exempt
def ask_question_view(request):
    if request.method == 'POST':
        form = ask_Question_Form(data=request.POST)
        if form.is_valid():
            form.question_title = request.POST['question_title']
            question_title = form.question_title
            print(question_title)
            form.question = request.POST['question']
            form.instance.user = request.user
            form.save()
            print('form valid')
        else:
            print(form.errors)
    return JsonResponse({'success':'success'})

@csrf_exempt
def comment_view(request):
    value = request.POST['input']
    id = request.POST['id']
    if value == '':
        print('empty')
        return JsonResponse({'success':'empty'})
    else:
        question = get_object_or_404(ask_question,id=id)
        user = request.user
        data =  comment_model(comment=value,user_answer=user,question=question).save()
        return JsonResponse({'success':'success'})

@csrf_exempt
def question_comment_list(request):
    pk_comt = int(request.POST['pk_c'])
    print(type(pk_comt))
    question = get_object_or_404(ask_question,id=pk_comt)
    comment_question = comment_model.objects.filter(question=question).values('id','comment','user_answer__username','create').order_by('-id')
    comment = list(comment_question)
    return JsonResponse({ 'comment':comment })

@csrf_exempt
def answer_question_view(request):
    if request.method == 'POST':
        id = request.POST['detail_id']
        question = get_object_or_404(ask_question,id=id)
        print(question.id)
        # print('answer_from user')
        form = Answer_Question_Form(data=request.POST)
        if form.is_valid():
            form.answer = request.POST['answer']
            form.instance.user_answer = request.user
            form.instance.question = question
            form.save()
        else:
            print(form.errors)
    return JsonResponse({'success':'success'})

@csrf_exempt
def like(request):
    ASK_QUESTION  =int( request.POST['like_id'])
    question = get_object_or_404(ask_question , id=ASK_QUESTION)
    user = request.user
    is_liked = False
    # print(user)
    # print(is_liked)
    if ask_question.objects.filter(id=ASK_QUESTION,like=user).exists():
        # print('unliked')
        question.like.remove(request.user)
        is_liked = False
        count= question.like.count()
        # print(count)
        # print(is_liked)
        return JsonResponse({ 'success':'is_liked' })
    else:
        print('liked')
        question.like.add(request.user)
        count= question.like.count()
        # print(count)
        is_liked = True
        # print(is_liked)
        return JsonResponse({ 'success':'liked' })
@csrf_exempt
def answer_like(request):
    id = int(request.POST['like_id'])
    like_add_remove=get_object_or_404(answer_question,id=id)
    print(type(id))
    print('liked')
    user = request.user
    if answer_question.objects.filter(id=id,answer_like=user).exists():
        like_add_remove.answer_like.remove(request.user)
        return JsonResponse({ 'success':'answer_unliked' })
    else:
        like_add_remove.answer_like.add(request.user)
        return JsonResponse({ 'success':'answer_liked' })

@csrf_exempt
def like_count(request):
    id = int(request.POST['like_id'])
    like_count = get_object_or_404(ask_question,id=id)
    cou = like_count.like.count()
    # print(type(cou))\
    print(cou)
    return JsonResponse({'success':cou })
@csrf_exempt
def question_view(request):
    question_list = models.ask_question.objects.filter().values('id','question_title','view','create__date','user__username')
    question_list = list(question_list)
    print(question_list)
    return JsonResponse({ 'question':question_list })

@csrf_exempt
def answer_list(request):
    id= request.POST['answer_list_id']
    data_like = get_object_or_404(ask_question, id=id)
    answer = answer_question.objects.filter(question=data_like).values('answer','id','user_answer__username').order_by('-id')
    answer_list = list(answer)
    return JsonResponse({ 'answer_answer':answer_list })

def detail_url_view(request,pk):
    form = ask_Question_Form()
    form_answer = Answer_Question_Form()
    print('detail')
    user = request.user
    data_like = get_object_or_404(ask_question, id = pk)
    count_like = data_like.like.count()
    data = ask_question.objects.filter(id=pk).values('id','question_title','question','create','view','user__username')
    view = ask_question.objects.filter(id=pk).update(view=F('view')+1)
    is_liked = False
    if ask_question.objects.filter(id =pk,like=user).exists():
        is_liked = True
        print(is_liked)
    return render(request,'html/detail_view.html',{'form_ans':form,'form_answer':form_answer,'is_liked':is_liked, 'data':data,'count_like':count_like})
# @csrf_exempt
# def email_send(request):
#     user_email_address = request.POST['val']
#     print(user_email_address)
#     subject = 'l'
#     message = 'message password'
#     email_from = EMAIL_HOST_USER
#     recipient_list = [user_email_address]
#     send_mail(subject,message,email_from,recipient_list)
#     print('message')
#     return JsonResponse({'success':'success'})
@csrf_exempt
def pacchaiamman(request):
    green = request.POST['val']
    subject = 'pacchaiamman potri'
    message = ' pacchaiamman manathieswara potri'
    email =  EMAIL_HOST_USER
    print(green)
    recipient_list = list(green)
    print(type(recipient_list))
    send_mail(subject,message,email,recipient_list)
    print(send_mail)
    return JsonResponse({'success':'success'})
