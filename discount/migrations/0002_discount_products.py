# Generated by Django 4.2.1 on 2023-06-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='products',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]
