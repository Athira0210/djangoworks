# Generated by Django 4.0.6 on 2022-07-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=150)),
                ('rating', models.FloatField()),
            ],
        ),
    ]