# Generated by Django 2.1.1 on 2018-09-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180928_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='images/no-img.png', null=True, upload_to='images/'),
        ),
    ]