# Generated by Django 5.0 on 2024-01-22 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_question_expected_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='input1',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='question',
            name='input2',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='question',
            name='input3',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
