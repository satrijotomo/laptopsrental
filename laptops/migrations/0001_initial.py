# Generated by Django 3.1.1 on 2022-04-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laptopmodel', models.CharField(default='', max_length=70)),
                ('serialno', models.CharField(default='', max_length=50)),
                ('image_path', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(default='', max_length=300)),
                ('owner', models.BooleanField(default=False)),
            ],
        ),
    ]