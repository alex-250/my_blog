# Generated by Django 4.0.4 on 2022-06-10 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_articlepost_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='webapp.articlecolumn'),
        ),
    ]
