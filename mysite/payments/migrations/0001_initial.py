# Generated by Django 2.2 on 2020-01-31 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enrolments', '0002_auto_20200131_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refid', models.CharField(default='xxxxxxxx', max_length=200)),
                ('enrolment', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='enrolments.Enrolment')),
            ],
        ),
    ]
