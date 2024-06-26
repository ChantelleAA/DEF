# Generated by Django 4.2.13 on 2024-05-26 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Case",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "case_type",
                    models.CharField(
                        choices=[
                            ("appeals", "Appeals"),
                            ("aviation", "Aviation"),
                            ("business_dispute", "Business Dispute"),
                            ("chancery", "Chancery"),
                            ("clinical_negligence", "Clinical Negligence"),
                            ("construction", "Construction"),
                            ("costs", "Costs"),
                            ("employment", "Employment"),
                            ("family_children", "Family – Children"),
                            ("family_divorce", "Family – Divorce"),
                            ("family_financial", "Family – Financial"),
                            ("family_inheritance", "Family – Inheritance Act"),
                            ("fire_damage", "Fire damage"),
                            ("flood_damage", "Flood damage"),
                            (
                                "personal_injury_abuse_claims",
                                "Personal Injury - Abuse claims",
                            ),
                            ("personal_injury_cica", "Personal Injury - CICA"),
                            (
                                "personal_injury_employer_liability",
                                "Personal Injury - Employer Liability",
                            ),
                            (
                                "personal_injury_mib_untraced",
                                "Personal Injury - MIB untraced",
                            ),
                            ("personal_injury_military", "Personal Injury - Military"),
                            (
                                "personal_injury_occupational_disease",
                                "Personal Injury - Occupational disease",
                            ),
                            (
                                "personal_injury_public_liability",
                                "Personal Injury - Public Liability (PL)",
                            ),
                            (
                                "personal_injury_road_traffic_whiplash",
                                "Personal injury - Road Traffic and Whiplash",
                            ),
                            ("personal_injury_travel", "Personal injury - Travel"),
                            ("planning", "Planning"),
                            ("property_non_fire_flood", "Property (non-fire/flood)"),
                            ("shipping", "Shipping"),
                            ("travel_abta", "Travel – ABTA"),
                            ("travel_non_abta", "Travel – non-ABTA"),
                            (
                                "workplace_issues",
                                "Workplace issues (not personal injury)",
                            ),
                        ],
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Client",
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
                ("name", models.CharField(max_length=100)),
                ("contact_info", models.TextField()),
                ("claims", models.TextField()),
                (
                    "claim_type",
                    models.CharField(
                        choices=[
                            ("appeals", "Appeals"),
                            ("aviation", "Aviation"),
                            ("business_dispute", "Business Dispute"),
                            ("chancery", "Chancery"),
                            ("clinical_negligence", "Clinical Negligence"),
                            ("construction", "Construction"),
                            ("costs", "Costs"),
                            ("employment", "Employment"),
                            ("family_children", "Family – Children"),
                            ("family_divorce", "Family – Divorce"),
                            ("family_financial", "Family – Financial"),
                            ("family_inheritance", "Family – Inheritance Act"),
                            ("fire_damage", "Fire damage"),
                            ("flood_damage", "Flood damage"),
                            (
                                "personal_injury_abuse_claims",
                                "Personal Injury - Abuse claims",
                            ),
                            ("personal_injury_cica", "Personal Injury - CICA"),
                            (
                                "personal_injury_employer_liability",
                                "Personal Injury - Employer Liability",
                            ),
                            (
                                "personal_injury_mib_untraced",
                                "Personal Injury - MIB untraced",
                            ),
                            ("personal_injury_military", "Personal Injury - Military"),
                            (
                                "personal_injury_occupational_disease",
                                "Personal Injury - Occupational disease",
                            ),
                            (
                                "personal_injury_public_liability",
                                "Personal Injury - Public Liability (PL)",
                            ),
                            (
                                "personal_injury_road_traffic_whiplash",
                                "Personal injury - Road Traffic and Whiplash",
                            ),
                            ("personal_injury_travel", "Personal injury - Travel"),
                            ("planning", "Planning"),
                            ("property_non_fire_flood", "Property (non-fire/flood)"),
                            ("shipping", "Shipping"),
                            ("travel_abta", "Travel – ABTA"),
                            ("travel_non_abta", "Travel – non-ABTA"),
                            (
                                "workplace_issues",
                                "Workplace issues (not personal injury)",
                            ),
                        ],
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Keyword",
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
                ("word", models.CharField(max_length=255, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Mediator",
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
                ("name", models.CharField(max_length=100)),
                ("contact_info", models.TextField()),
                ("expertise", models.JSONField()),
                ("experience", models.IntegerField()),
                ("membership", models.TextField()),
                ("style_approach", models.TextField()),
                ("availability", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="MediatorKeyword",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "keyword",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mediators.keyword",
                    ),
                ),
                (
                    "mediator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mediators.mediator",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CaseKeyword",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "case",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mediators.case"
                    ),
                ),
                (
                    "keyword",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mediators.keyword",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CaseClient",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "case",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mediators.case"
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mediators.client",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="case",
            name="clients",
            field=models.ManyToManyField(
                through="mediators.CaseClient", to="mediators.client"
            ),
        ),
        migrations.CreateModel(
            name="Appointment",
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
                ("appointment_date", models.DateField()),
                ("appointment_time", models.TimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "case",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mediators.case"
                    ),
                ),
                (
                    "mediator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mediators.mediator",
                    ),
                ),
            ],
        ),
    ]
