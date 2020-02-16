from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from custom_user_model.models import Custom_user
from . forms import ask_Question_Form,Answer_Question_Form
from custom_user_model.forms import UserForm,UserLoginForm
from .models import ask_question,comment_model,answer_question
from . import models
from django.template.loader import render_to_string
from django.db.models import F
def intro(request):
    user = UserForm()
    form = UserLoginForm()
    return render(request,'html/intro.html',{'user':user,'form':form})
def home(request):
    form = ask_Question_Form()
    return render(request,'html/home.html',{'form':form})
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
    question = get_object_or_404(ask_question,id=id)
    user = request.user
    data =  comment_model(comment=value,user_answer=user,question=question).save()
    return JsonResponse({'success':'success'})
@csrf_exempt
def comment_answer_view(request):
    valu = request.POST['val']
    id_g    = request.POST['id_idg']
    pacchaiamman_id = int(id_g)
    print(type(pacchaiamman_id))
    question = get_object_or_404(answer_question,id=pacchaiamman_id)
    print('pacchaiamman');
    user = request.user
    data =  comment_model(comment=valu,user_answer=user,answer=question).save()
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
def answer_comment_list(request):
    pk_comt = int(request.POST['pk_c'])
    print(type(pk_comt))
    question = get_object_or_404(answer_question,id=pk_comt)
    comment_question = comment_model.objects.filter(answer=question).values('id','comment','user_answer__username','create').order_by('-id')
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
            # question.answer.add(request.answer)
            # id = form.instance.question
            # print(form.instance.question)
            form.save()
        else:
            print(form.errors)
    return JsonResponse({'success':'success'})
# def like(request,pk):
@csrf_exempt
def like(request):
    ASK_QUESTION  =int( request.POST['like_id'])
    question = get_object_or_404(ask_question , id=ASK_QUESTION)
    user = request.user
    is_liked = False
    print(is_liked)
    if ask_question.objects.filter(like=user).exists():
        print('unliked')
        question.like.remove(request.user)
        is_liked = False
        return JsonResponse({ 'success':'is_liked' })
    else:
        print('liked')
        question.like.add(request.user)
        is_liked = True
        return JsonResponse({ 'success':'liked' })
        # return JsonResponse({'success':'success'})
    # return render(request,'html/like_unlike_button.html',{'is_liked':is_liked,'like_count':question.like_add()})
    # return JsonResponse({'success':'success'})
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

#     print(id)
#     question = get_object_or_404(ask_question, id = id)
#     print(question)
#     print('answer_list')
#     answer  = models.answer_question.objects.filter(id_answer=question).values('answer','create','user_answer')
#     answer_list = list(answer)
#     # print(answer_list)
#     return JsonResponse({ 'answer_list':answer_list })
def detail_url_view(request,pk):
    form = ask_Question_Form()
    form_answer = Answer_Question_Form()
    print('detail')
    user = request.user
    data_like = get_object_or_404(ask_question, id = pk)
    # answer = answer_question.objects.filter(question=data_like).order_by('-id')
    data = ask_question.objects.filter(id=pk).values('id','question_title','question','create','view','user__username')
    view = ask_question.objects.filter(id=pk).update(view=F('view')+1)
    print(data)
    is_liked = False
    if ask_question.objects.filter(like=user).exists():
        is_liked = True
    return render(request,'html/detail_view.html',{'form':form,'form_answer':form_answer,'is_liked':is_liked,'data':data,'like_count':data_like.like_add()})
    # return JsonResponse({'detail':list(data)})
