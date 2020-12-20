# Generated by Django 3.0.2 on 2020-03-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=128)),
                ('age', models.CharField(max_length=128)),
                ('date_of_birth', models.DateField()),
                ('current_weight', models.FloatField()),
                ('targeted_weight', models.FloatField()),
                ('height', models.FloatField()),
                ('time_period', models.IntegerField()),
                ('password', models.CharField(max_length=128)),
                ('usertype', models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], max_length=120)),
            ],
        ),
    ]