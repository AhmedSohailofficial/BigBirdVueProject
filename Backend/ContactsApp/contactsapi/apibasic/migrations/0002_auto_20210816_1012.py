# Generated by Django 3.2.5 on 2021-08-16 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apibasic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MainText', models.CharField(max_length=200)),
                ('SubText', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
    ]
