# Generated by Django 4.0.6 on 2023-02-05 14:13

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
                ('age', models.IntegerField()),
                ('sub', models.CharField(max_length=100)),
                ('collage', models.CharField(max_length=100)),
            ],
        ),
    ]