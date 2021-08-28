# Generated by Django 3.2.6 on 2021-08-28 03:25

import aseb.apps.users.models
import aseb.core.db.utils
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.crypto
import django.utils.timezone
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True,
                        help_text="Required. 50 characters or fewer. Letters, digits and -/_ only.",
                        max_length=50,
                        validators=[django.core.validators.RegexValidator("^[\\w_\\-.]+\\Z")],
                        verbose_name="username",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        upload_to=aseb.core.db.utils.UploadToFunction("avatars/{uuid}.{ext}"),
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("first_name", models.CharField(blank=True, max_length=256)),
                ("last_name", models.CharField(blank=True, max_length=256)),
                (
                    "secret_key",
                    models.CharField(
                        default=functools.partial(
                            django.utils.crypto.get_random_string,
                            *(),
                            **{
                                "allowed_chars": "abcdefghijklmnopqrstuvwxyz0123456789-_=+",
                                "length": 42,
                            },
                        ),
                        max_length=42,
                    ),
                ),
                ("jwt_jti", models.CharField(blank=True, editable=False, max_length=256)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "ordering": ["date_joined"],
            },
            managers=[
                ("objects", aseb.apps.users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="AccessToken",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("token", models.CharField(max_length=255, unique=True)),
                ("expires", models.DateTimeField(null=True)),
                ("scope", models.TextField(blank=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tokens",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
