# Generated by Django 5.1.1 on 2024-09-10 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0004_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
