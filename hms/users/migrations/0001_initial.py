# Generated by Django 5.1.4 on 2025-01-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("enrollment_number", models.CharField(max_length=12, unique=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=10
                    ),
                ),
                (
                    "branch",
                    models.CharField(
                        choices=[
                            ("COMPUTER", "Computer Engg."),
                            ("CIVIL", "Civil Engg."),
                            ("CHEMICAL", "Chemical Engg."),
                            ("ELECTRICAL", "Electrical Engg."),
                            ("EC", "Electronics and Communication Engg."),
                            ("MECHANICAL", "Mechanical Engg."),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "semester",
                    models.IntegerField(
                        choices=[
                            (1, "1"),
                            (2, "2"),
                            (3, "3"),
                            (4, "4"),
                            (5, "5"),
                            (6, "6"),
                            (7, "7"),
                            (8, "8"),
                        ]
                    ),
                ),
                ("contact_number", models.CharField(max_length=15)),
                ("parent_contact_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("OLD", "Old"), ("NEW", "New")], max_length=10
                    ),
                ),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
