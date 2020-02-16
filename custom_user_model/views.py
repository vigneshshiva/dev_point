from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import login,authenticate,logout
from .forms import UserForm,UserLoginForm
from django.views.decorators.csrf import csrf_exempt
from . models import Custom_user
@csrf_exempt
def register(request):
    if request.POST:
        form = UserForm(request.POST)
        print('request')
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print('request valid')
        print(email)
        if Custom_user.objects.filter(username=username).exists():
            return JsonResponse({'username':'username'})
        elif Custom_user.objects.filter(email=email).exists():
            return JsonResponse({'email':'email'})
        elif password1 != password2:
            return JsonResponse({'password':'password'})
        else:
            if form.is_valid():
                form.save()
                custom_user = authenticate(email=email,password=password1)
                print('request valid')
                login(request,custom_user)
                print('request valid')
                return JsonResponse({'success':'success'})
            else:
                print(form.errors)
    return render(request,'html/intro.html',{'user':form})
    # email  =form.cleaned_data.get('email')
    # username = form.cleaned_data.get('username')
    # password1 = form.cleaned_data.get('password1')
        # elif Custom_user.objects.filter(password=password1).exists():
        #     print('password')
        #     return JsonResponse({'success':'password_taken'})
        # else:
            #     custom_user = authenticate(email=email,password=password1)
            #     print('request valid')
            #     login(request,custom_user)
            # return JsonResponse({'success':'success'})
def logout_view(request):
    print('logout')
    logout(request)
    return redirect('home')
@csrf_exempt
def login_view(request):
    print('login')
    user = request.user
    email = request.POST['email']
    print(email)
    password = request.POST['password']
    print(password)
    if request.method == 'POST':
        print('login')
        form = UserLoginForm(data=request.POST)
        # if form.is_valid():
        print('login2')
        user = authenticate(email=email,password=password)
        if user:
            print('loginlogin')
            login(request,user)
            # return redirect('')
            return JsonResponse({'success':'success'})
    else:
        print('form invalid')
        form =UserLoginForm()
    return render(request,'html/intro.html',{'form':form})
