# Generated by Django 4.0.2 on 2022-07-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('marks', models.FloatField()),
                ('dob', models.DateField()),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]