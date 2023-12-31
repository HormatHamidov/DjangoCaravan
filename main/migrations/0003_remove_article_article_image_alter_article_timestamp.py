# Generated by Django 4.2.2 on 2023-06-08 11:25

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_image',
        ),
        migrations.AlterField(
            model_name='article',
            name='timestamp',
            field=models.DateField(blank=True, null=True, validators=[main.validators.validate_timestamp]),
        ),
    ]
