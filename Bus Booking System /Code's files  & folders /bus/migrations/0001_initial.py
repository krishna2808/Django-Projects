# Generated by Django 2.2.14 on 2020-09-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busName', models.CharField(max_length=30)),
                ('busFrom', models.CharField(max_length=30)),
                ('busTo', models.CharField(max_length=30)),
                ('busTime', models.DateTimeField()),
            ],
        ),
    ]