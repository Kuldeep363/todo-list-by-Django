# Generated by Django 3.0.3 on 2020-05-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_tasks_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='identity',
            field=models.CharField(blank=True, default='234', max_length=200),
        ),
    ]
