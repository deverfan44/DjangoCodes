# Generated by Django 5.1.4 on 2024-12-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.CharField(default='Mr', max_length=100),
        ),
    ]
