# Generated by Django 4.2.1 on 2023-06-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=90)),
                ('user_id', models.PositiveIntegerField()),
                ('product_id', models.PositiveIntegerField()),
                ('ratings', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
