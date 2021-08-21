# Generated by Django 3.2.6 on 2021-08-21 04:38

import aseb.core.db.fields
import aseb.core.db.utils
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.datetime
import django_editorjs_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.db.models.functions.datetime.Now, editable=False
                    ),
                ),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("removed_at", models.DateTimeField(blank=True, editable=False, null=True)),
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
                ("seo_title", models.CharField(blank=True, max_length=70)),
                ("seo_description", models.CharField(blank=True, max_length=300)),
                (
                    "main_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=aseb.core.db.utils.UploadToFunction(
                            "{model_name}/{obj.pk}/{filename}.{ext}"
                        ),
                    ),
                ),
                ("content", django_editorjs_fields.fields.EditorJsJSONField(blank=True, null=True)),
                ("display_name", models.CharField(blank=True, max_length=140)),
                ("headline", models.CharField(blank=True, max_length=140)),
                ("presentation", models.TextField(blank=True)),
                ("contact", aseb.core.db.fields.PropertiesField(default=dict, blank=True)),
                (
                    "size",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "1 - 4 employees"),
                            (2, "5 - 9 employees"),
                            (3, "10 - 19 employees"),
                            (4, "20 - 49 employees"),
                            (5, "50 - 99 employees"),
                            (6, "100 - 249 employees"),
                            (7, "250 - 499 employees"),
                            (8, "500 - 999 employees"),
                            (9, "1,000+ employees"),
                        ],
                        null=True,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "companies",
            },
        ),
        migrations.CreateModel(
            name="Interest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "emoji",
                    models.CharField(
                        max_length=3,
                        validators=[
                            django.core.validators.RegexValidator(
                                "(\\u00a9|\\u00ae|[\\u2000-\\u3300]|\\ud83c[\\ud000-\\udfff]|\\ud83d[\\ud000-\\udfff]|\\ud83e[\\ud000-\\udfff])"
                            )
                        ],
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Market",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "sibling",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_organization_market_sibling_+",
                        to="organization.Market",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.db.models.functions.datetime.Now, editable=False
                    ),
                ),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("removed_at", models.DateTimeField(blank=True, editable=False, null=True)),
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
                ("seo_title", models.CharField(blank=True, max_length=70)),
                ("seo_description", models.CharField(blank=True, max_length=300)),
                (
                    "main_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=aseb.core.db.utils.UploadToFunction(
                            "{model_name}/{obj.pk}/{filename}.{ext}"
                        ),
                    ),
                ),
                ("content", django_editorjs_fields.fields.EditorJsJSONField(blank=True, null=True)),
                ("display_name", models.CharField(blank=True, max_length=140)),
                ("headline", models.CharField(blank=True, max_length=140)),
                ("presentation", models.TextField(blank=True)),
                ("contact", aseb.core.db.fields.PropertiesField(default=dict)),
                ("first_name", models.CharField(blank=True, max_length=140)),
                ("last_name", models.CharField(blank=True, max_length=140)),
                ("birthday", models.DateField(blank=True, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("member", "Member"), ("partner", "Partner")], max_length=20
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("president", "President"),
                            ("advisor", "Advisor"),
                            ("boardMember", "Board Member"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("activated_at", models.DateField(blank=True, null=True)),
                ("expires_at", models.DateField(blank=True, null=True)),
                ("mentor_since", models.DateTimeField(blank=True, null=True)),
                ("mentor_presentation", models.TextField(blank=True)),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="members",
                        to="organization.company",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("interests", models.ManyToManyField(blank=True, to="organization.Interest")),
                (
                    "login",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "markets",
                    models.ManyToManyField(
                        blank=True, to="organization.Market", verbose_name="Market's of interest"
                    ),
                ),
                (
                    "mentor_interests",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_organization_member_mentor_interests_+",
                        to="organization.Interest",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "nominated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="nominated_members",
                        to="organization.member",
                    ),
                ),
                (
                    "removed_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="company",
            name="interests",
            field=models.ManyToManyField(blank=True, to="organization.Interest"),
        ),
        migrations.AddField(
            model_name="company",
            name="markets",
            field=models.ManyToManyField(
                blank=True, to="organization.Market", verbose_name="Market's of interest"
            ),
        ),
        migrations.AddField(
            model_name="company",
            name="modified_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="company",
            name="removed_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
