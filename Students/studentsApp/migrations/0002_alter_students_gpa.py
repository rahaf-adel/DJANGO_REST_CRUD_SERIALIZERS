# Generated by Django 4.0.5 on 2022-06-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='GPA',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
