# Generated by Django 5.1.4 on 2024-12-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelApp', '0002_student_father_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mother_name',
            field=models.CharField(default='Mrs', max_length=100),
        ),
    ]
