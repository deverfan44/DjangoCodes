# Generated by Django 5.1.4 on 2024-12-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TaskModelApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categroy_name', models.CharField(max_length=100)),
                ('target', models.ManyToManyField(to='TaskModelApp.task')),
            ],
        ),
    ]
