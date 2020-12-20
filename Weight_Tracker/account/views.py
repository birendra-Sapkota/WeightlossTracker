from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']
        answer = request.POST['usert']

        if answer == 'admin':
            is_staff = 1
        else:
            is_staff = 0

        #after register only
        # dob = request.POST['dob']
        # current_weight = request.POST['cweight']
        # targeted_weight = request.POST['tweight']
        # time_period = request.POST['atime'] #time perion in day
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken")
                return redirect('account:register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken")
                return redirect('account:register')

            else:
                user = User.objects.create_user(username=username,  is_staff=is_staff, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()

                print('user created')
                return redirect('account:login')
        else:
            messages.info(request, "Unable to register. Password did not matched....")
            return redirect('account:register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid crediential")
            return redirect('account:login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")



