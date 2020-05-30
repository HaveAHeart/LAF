# Generated by Django 3.0.6 on 2020-05-30 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('vkID', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('time', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]