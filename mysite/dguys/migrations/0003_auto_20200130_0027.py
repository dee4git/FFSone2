# Generated by Django 2.2 on 2020-01-29 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dguys', '0002_auto_20200130_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dguy',
            name='photo',
            field=models.ImageField(blank=True, default='avatar.gif', upload_to='propics'),
        ),
    ]