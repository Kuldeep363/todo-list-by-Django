# Generated by Django 3.0.3 on 2020-05-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=250)),
                ('description', models.TextField(default='')),
                ('deadline', models.DateField(blank = True , default = '2020-05-20')),
            ],
        ),
    ]
