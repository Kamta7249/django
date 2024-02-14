# Generated by Django 5.0.1 on 2024-01-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sal', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Programmer', models.ManyToManyField(to='empApp.programmer')),
            ],
        ),
    ]
