from django.shortcuts import render
from .models import Users,Products

# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        password = request.POST.get('password')
        # print(name)
        users = Users(name=name,email=email,password=password)
        users.save()
        return redirect('welcome')
    else:
        return render(request,'register.html')
def welcome(request):
    users = Users.objects.all()
    return render(request,'welcome.html')
#     # on = True
#     data = [1,2,3,4,5]
    context = {
        'users':Users
#         'data':data,
        # 'on':on

        
    }
    return render(request,'welcome.html',context)