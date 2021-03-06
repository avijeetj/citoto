# Generated by Django 3.0.8 on 2020-07-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=20)),
                ('ph_valid', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
