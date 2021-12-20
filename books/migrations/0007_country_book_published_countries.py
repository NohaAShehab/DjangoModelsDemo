# Generated by Django 4.0 on 2021-12-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_address_author_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(to='books.Country'),
        ),
    ]
