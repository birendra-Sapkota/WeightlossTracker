import datetime
from collections import defaultdict

from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import BmiForm, AddConsumeFood, FoodDetailForm

# Create your views here.
from home.models import Person, FoodDetail, ConsumeFoodDetail


def edit_profile(request):

    if request.method == 'POST':
        user = User.objects.filter(username=request.user)
        person = Person.objects.filter(username=request.user)

        if user.exists():

            if request.method == 'POST':
                # form = PersonForm(request.POST, request.FILES)
                # print(form.is_valid())

                usrr = str(user)
                usr = usrr[18:]
                user_len = len(usr)
                user_str = usr[0: user_len - 3]
                per = str(person)
                slice_per = per[20:]
                per_len = len(slice_per)
                person_str = slice_per[0:per_len - 3]

                if user_str == person_str:
                    Person.objects.filter(username=request.user).delete()
                first_name = request.user.first_name
                last_name = request.user.last_name
                username = request.user.username
                email = request.user.email
                current_weight = request.POST['cweight']
                age = request.POST['cage']
                targeted_weight = request.POST['tweight']
                time_period = request.POST['timep']
                gender = request.POST['gender']
                height = request.POST['height']
                date_of_birth = request.POST['dob']

                password = request.user.password
                if request.user.is_staff == 1:
                    user_type = 'admin'
                else:
                    user_type = 'user'
                # img = form.data.get('profile')
                # print(form.data.get('profile'))
                p = Person.objects.create(username=username, usertype=user_type,profile=img, password=password, email=email,
                                          firstname=first_name, lastname=last_name, gender=gender, age=age,
                                          date_of_birth=date_of_birth, current_weight=current_weight,
                                          targeted_weight=targeted_weight, height=height, time_period=time_period)
                p.save()

                messages.info(request, "profile successfully updated", extra_tags='updatesus')

                return redirect('home:userprofile')
    else:
        print()
        # form = PersonForm()
    # context = {
    #     'form': form
    # }

    return render(request, 'user_edit_profile.html')


def home(request):
    return render(request, 'index.html')


def user_home(request):
    return render(request, 'user_home.html')


def user_dashboard(request):
    user = User.objects.filter(username=request.user)

    if user.exists():
        print("trueeee")
        person = Person.objects.filter(username=request.user)

        usrr = str(user)
        usr = usrr[18:]
        user_len = len(usr)
        user_str = usr[0: user_len - 3]

        per = str(person)
        slice_per = per[20:]
        per_len = len(slice_per)
        person_str = slice_per[0:per_len - 3]

        if user_str == person_str:

            messages.info(request, "You have successfully Logged in", extra_tags="login")
        else:
            messages.info(request,
                          "Its your first time, so please edit your profile first to continue", extra_tags="clogin")
            return render(request, 'user_edit_profile.html')

    if request.method == 'POST':
        form = BmiForm(request.POST)
        if form.is_valid():
            print("ffffffffffffffffff")
            form.save()
    form = BmiForm()

    if request.method == 'POST':
        bmidata = request.POST.dict()
        height = float(bmidata.get('height'))
        weight = float(bmidata.get('weight'))

        height_in_meter = height * 0.3048

        bmi = float(weight / (height_in_meter * height_in_meter))

        if bmi < 18.5:
            messages.info(request, "Your BMI = " + str(bmi) + " You are Underweight", extra_tags="bmi")
            messages.info(request, "underweight", extra_tags="underweight")
        elif 18.5 < bmi < 24.9:
            messages.info(request, "Your BMI = " + str(bmi) + " You are Normal", extra_tags="bmi")
            messages.info(request, "normal", extra_tags="normal")
        elif 25 < bmi < 29.9:
            messages.info(request, "Your BMI = " + str(bmi) + " You are overweight", extra_tags="bmi")
            messages.info(request, "overweight", extra_tags="overweight")
        elif 30 < bmi < 34.9:
            messages.info(request, "Your BMI = " + str(bmi) + " You are Obese", extra_tags="bmi")
            messages.info(request, "obese", extra_tags="obese")
        else:
            messages.info(request, " Your BMI = " + str(bmi) + " You are Extremely Obese", extra_tags="bmi")
            messages.info(request, "Extremely Obese", extra_tags="exobese")

    return render(request, 'user_home.html', {'form': form})


def add_cf(request):
    person = Person.objects.filter(username=request.user)
    per = str(person)
    slice_per = per[20:]
    per_len = len(slice_per)
    person_str = slice_per[0:per_len - 3]

    adm_food = FoodDetail.objects.all()
    food_consume = []
    detail = {}
    foods = {}

    for food in adm_food:
        detail['cal'] = food.cal
        detail['fat'] = food.fat
        detail['protein'] = food.protein
        detail['carbs'] = food.carbs
        detail['category'] = food.category
        foods[food.food_name] = detail
        food_consume.append(food.food_name)

    form = AddConsumeFood(initial={'username': person_str, 'date': datetime.datetime.now().date()})
    food_name_valid = ''
    if request.method == 'POST':
        form = AddConsumeFood(request.POST)
        food_name_valid = form.data['food_name']
        if form.is_valid():
            if food_name_valid in food_consume:
                form.save()
                # print("Food added successfully")
                messages.info(request, "Consumed Food --  "+form.data['food_name'] +", added successfully",
                              extra_tags='consumedfood')
            else:
                messages.error(request, form.data['food_name']+" failed to add. It seems the food detail is not yet registered ",
                               extra_tags='consumedfood')

    return render(request, 'user_add_consume_food.html', {'form': form})


def recommend_plan(request):
    # display total calories intake in a day.

    # user weight height bata bmi calculate garincha
    # ani aaja ko day ma kati calories intake garnu parne ho tara kati gareko cha herincha

    # BMI calculation of the logged in user
    print(request.user)

    p = Person.objects.get(username=request.user)

    age = float(p.age)
    weight_u = p.current_weight
    height_ft = p.height
    height_m = height_ft * 0.3048
    userbmis = float(weight_u / (height_m * height_m))
    mes = ''

    if 1 < age < 3:
        mes = "take 1200 calories a day"
        messages.info(request, "take 1200 calories a day", extra_tags='calneeds')

    elif 3 < age < 6:
        mes = "take 1450 calories a day"
        messages.info(request, "take 1450 calories a day", extra_tags='calneeds')

    elif 6 < age < 9:
        mes = "take 1600 calories a day"
        messages.info(request, "take 1600 calories a day", extra_tags='calneeds')
    elif 9 < age < 12:
        mes = "take 1850 calories a day"
        messages.info(request, "take 1850 calories a day", extra_tags='calneeds')
    elif 12 < age < 15:
        mes = "take 2300 calories a day"
        messages.info(request, "take 2300 calories a day", extra_tags='calneeds')
    elif 15 < age < 19:
        mes = "take 2400 calories a day"
        messages.info(request, "take 2400 calories a day", extra_tags='calneeds')
    elif 19 < age < 29:
        mes = "take 2787 calories a day"
        messages.info(request, "take 2787 calories a day", extra_tags='calneeds')
    elif 29 < age < 59:
        mes = "take 2767 calories a day"
        messages.info(request, "take 2767 calories a day", extra_tags='calneeds')
    else:
        mes = "take 1969 calories a day"
        messages.info(request, "take 1969 calories a day", extra_tags='calneeds')

    # calories intake check
    adm_food = FoodDetail.objects.all()
    food_consume = []
    detail = {}
    foods = {}
    for food in adm_food:
        detail['cal'] = food.cal
        detail['fat'] = food.fat
        detail['protein'] = food.protein
        detail['carbs'] = food.carbs
        detail['category'] = food.category
        foods[food.food_name] = detail
        food_consume.append(food.food_name)

    date = datetime.datetime.now().date()
    adm_food = ConsumeFoodDetail.objects.filter(date=date, username=request.user)
    total_calories = 0
    total_fat = 0
    total_carbs = 0
    total_protein = 0

    for food in adm_food:
        if food.food_name in foods:

            total_calories = total_calories + (float(foods[food.food_name]['cal']) / 100 * float(food.gram))
            total_fat = total_calories + (float(foods[food.food_name]['fat']) / 100 * float(food.gram))
            total_carbs = total_calories + (float(foods[food.food_name]['carbs']) / 100 * float(food.gram))
            total_protein = total_calories + (float(foods[food.food_name]['protein']) / 100 * float(food.gram))

    print(adm_food)
    # food_temp = defaultdict(list)
    # for af in adm_food:
    #     food_temp['foods'].append(af)
    #

    # print(food_temp)
    content = {
        'cal': total_calories,
        'fat': total_fat,
        'carbs': total_carbs,
        'protein': total_protein,
        'date': date,
        'userbmis': userbmis,
        'age': age,
        'message': mes,
        'f': adm_food,
        'fod_t': foods

    }

    return render(request, 'user_recommend_plan.html', {'detail_food': content})


def admin_home(request):
    return render(request, 'admin_home.html')


def adm_user_dashboard(request):
    return render(request, 'admin_home.html')


def adm_verify_user(request):
    u = User.objects.all()
    contex = {
        'user': u
    }
    return render(request, 'admin_verifyuser.html', contex)


def adm_addfood(request):
    form = FoodDetailForm()
    if request.method == 'POST':
        form = FoodDetailForm(request.POST)
        if form.is_valid():
            form.save()
            print("Food added successfully")
            messages.info(request, "Food added successfully. Would you like to add this food in another category ??",
                          extra_tags='foodadded')
    return render(request, 'admin_addFood.html', {'form': form})


def adm_view_all_user(request):
    usr = User.objects.all()
    context = {
        'user': usr
    }
    return render(request, 'admin_viewAllUser.html', context)


def adm_view_allfood(request):

    foods = FoodDetail.objects.all()
    print(type(foods))
    context = {
        'f': foods
    }

    return render(request, 'admin_viewAllFood.html', context)


def user_profile(request):
    if Person.objects.filter(username=request.user).exists():

        person = Person.objects.get(username=request.user, email=request.user.email)
        dataset = {
            "username": person.username,
            "firstname": person.firstname,
            "lastname": person.lastname,
            "email": person.email,
            "currentweight": person.current_weight,
            "age": person.age,
            "targetedweight": person.targeted_weight,
            "timeperiod": person.time_period,
            "gender": person.gender,
            "height": person.height,
            "dob": person.date_of_birth
        }

    else:
        dataset = {
            "username": "not yet updated",
            "firstname": "not yet updated",
            "lastname": "not yet updated",
            "email": "not yet updated",
            "currentweight": "not yet updated",
            "age": "not yet updated",
            "targetedweight": "not yet updated",
            "timeperiod": "not yet updated",
            "gender": "not yet updated",
            "height": "not yet updated",
            "dob": "not yet updated"
        }
    # per = str(person)
    # slice_per = per[20:]
    # per_len = len(slice_per)
    # person_str = slice_per[0:per_len - 3]
    # print(person_str)
    # dataset={}
    #
    # if person_str != "":

    # else:
    #     print("failed")

    return render(request, 'userprofile.html', {'dataset': dataset})


class weeklyReportView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user_weekly_report.html')


def get_data(request, *args, **kwargs):
    adm_food = FoodDetail.objects.all()
    food_consume = []
    detail = {}
    foods = {}
    for food in adm_food:
        detail['cal'] = food.cal
        detail['fat'] = food.fat
        detail['protein'] = food.protein
        detail['carbs'] = food.carbs
        detail['category'] = food.category
        foods[food.food_name] = detail
        food_consume.append(food.food_name)

    date = datetime.datetime.now().date()
    adm_food = ConsumeFoodDetail.objects.filter(date=date, username=request.user)
    total_calories = 0
    total_fat = 0
    total_carbs = 0
    total_protein = 0

    for food in adm_food:
        if food.food_name in foods:
            total_calories = total_calories + (float(foods[food.food_name]['cal']) / 100 * float(food.gram))
            total_fat = total_calories + (float(foods[food.food_name]['fat']) / 100 * float(food.gram))
            total_carbs = total_calories + (float(foods[food.food_name]['carbs']) / 100 * float(food.gram))
            total_protein = total_calories + (float(foods[food.food_name]['protein']) / 100 * float(food.gram))

    labels = ["Calories", "Fat", "Protein", "Carbs"]
    default_items = [total_calories, total_fat, total_protein, total_carbs]
    dt = "Report of " + str(date)



    # hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

    dateweek = datetime.datetime.now().date()
    lis = list(str(dateweek))
    print(lis)
    yr = lis[0:4]
    year=''
    for ele in yr:
        year += ele
    month = lis[5:7]
    mt = ''
    for m in month:
        mt += m
    if len(mt) == 1:
        mt = '0'+mt

    print(mt)
    dy = lis[8:]
    day = ''
    for da in dy:
        day += da
    final_year = int(year)
    final_month = int(mt)
    final_day = int(day)

    wtotal_calories = 0
    wtotal_fat = 0
    wtotal_carbs = 0
    wtotal_protein = 0

    for i in range(7):
        date_str = str(final_year) + '-'+str(final_month) +'-'+str(final_day-i)
        adm_food = ConsumeFoodDetail.objects.filter(date=date_str, username=request.user)
        print(adm_food)
        for food in adm_food:
            if food.food_name in foods:
                wtotal_calories = wtotal_calories + (float(foods[food.food_name]['cal']) / 100 * float(food.gram))
                wtotal_fat = wtotal_calories + (float(foods[food.food_name]['fat']) / 100 * float(food.gram))
                wtotal_carbs = total_calories + (float(foods[food.food_name]['carbs']) / 100 * float(food.gram))
                wtotal_protein = wtotal_calories + (float(foods[food.food_name]['protein']) / 100 * float(food.gram))
    weekly_data_item = [wtotal_calories, wtotal_fat, wtotal_protein, wtotal_carbs]
    from_info = 'Report from ' + date_str + ' to '+ str(date)
    print(from_info)

    data = {
        'date': dt,
        'labels': labels,
        'default': default_items,
        'data_weekly': weekly_data_item,
        'weekly_date': from_info,
    }
    return JsonResponse(data)







class Weekly_Rep(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # labels = ["user", "red", "green", "yello"]
        # default_items = [10, 22, 15, 6]
        # data = {
        #     'labels': labels,
        #     'default': default_items,
        # }
        return Response()


def aboutus(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')