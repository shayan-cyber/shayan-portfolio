# Generated by Django 3.2.6 on 2021-08-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type_of',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
