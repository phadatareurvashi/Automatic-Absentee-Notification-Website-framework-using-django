# Generated by Django 5.0 on 2024-04-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0007_student_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='roll_number',
            new_name='roll',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]