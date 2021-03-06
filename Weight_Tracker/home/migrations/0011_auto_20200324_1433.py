# Generated by Django 3.0.2 on 2020-03-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200320_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='consumefooddetail',
            name='category',
            field=models.CharField(choices=[('snacks', 'snacks'), ('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner')], default='breakfast', max_length=128),
        ),
        migrations.AlterField(
            model_name='fooddetail',
            name='category',
            field=models.CharField(choices=[('snacks', 'snacks'), ('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner')], default='lunch', max_length=128),
        ),
    ]
