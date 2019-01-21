# Generated by Django 2.1.5 on 2019-01-20 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviepoll', '0004_remove_choice_choice_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_description',
            field=models.CharField(blank=True, default=False, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_genre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_imdb',
            field=models.FloatField(blank=True, default=False, null=True),
        ),
    ]
