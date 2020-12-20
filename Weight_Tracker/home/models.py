from django.db import models

# Create your models here.


class Person(models.Model):
    # profile = models.ImageField(upload_to='uploads/', null=True)
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    age = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    current_weight = models.FloatField()
    targeted_weight = models.FloatField()
    height = models.FloatField()
    time_period = models.IntegerField()
    password = models.CharField(max_length=128)
    usertype = models.CharField(max_length=120)

    def __str__(self):
        return self.username


food_category = {
    ('breakfast', 'breakfast'),('lunch', 'lunch'),('snacks','snacks'),('dinner', 'dinner')
}


class FoodDetail(models.Model):
    food_name = models.CharField(max_length=128)
    cal = models.CharField(max_length=128, null=True)
    fat = models.CharField(max_length=128)
    protein = models.CharField(max_length=128)
    carbs = models.CharField(max_length=128, null=True)
    category = models.CharField(max_length=128, choices=food_category, default="lunch")

    def __str__(self):
        return self.food_name


class Bmi(models.Model):
    username = models.CharField(max_length=128)
    height = models.CharField(max_length=128)
    weight = models.CharField(max_length=128)
    bmi = models.CharField(max_length=128)
    category = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class ConsumeFoodDetail(models.Model):
    username = models.CharField(max_length=128)
    food_name = models.CharField(max_length=128)
    gram = models.CharField(max_length=128)
    category = models.CharField(max_length=128, choices=food_category, default="breakfast")
    date = models.DateField()

    def __str__(self):
        return self.username + '  ' + str(self.date) + ' --> ' + self.food_name


