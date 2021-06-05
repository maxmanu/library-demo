# Generated by Django 3.2.3 on 2021-06-04 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("nationality", models.CharField(max_length=50)),
                ("genere", models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name="book",
            name="autor",
        ),
        migrations.AlterField(
            model_name="book",
            name="volume",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.author",
            ),
        ),
    ]
