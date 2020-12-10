# Generated by Django 3.1.4 on 2020-12-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_auto_20201210_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=200)),
                ('descricao', models.TextField(max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
