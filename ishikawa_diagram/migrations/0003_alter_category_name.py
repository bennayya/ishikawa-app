# Generated by Django 5.0.4 on 2024-04-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ishikawa_diagram', '0002_ishikawadiagram_updated_at_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
