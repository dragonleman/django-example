# Generated by Django 4.2.2 on 2023-06-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter', models.CharField(max_length=1000, unique=True)),
                ('choices', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]