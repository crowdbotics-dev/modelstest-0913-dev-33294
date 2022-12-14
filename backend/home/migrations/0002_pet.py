# Generated by Django 2.2.28 on 2022-09-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
