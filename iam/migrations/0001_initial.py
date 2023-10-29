# Generated by Django 4.2.6 on 2023-10-21 06:49

from django.db import migrations, models
import django.db.models.deletion
import django_enum_choices.choice_builders
import django_enum_choices.fields
import django_enumfield.db.fields
import iam.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_remove_user_id_alter_user_root_id_alter_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iam',
            fields=[
                ('iam_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('last_modified', models.DateTimeField()),
                ('passed_num', models.IntegerField()),
                ('total_num', models.IntegerField()),
                ('root_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_iam', to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='IamList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_name', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('iam_administrator_access_with_mfa', 'iam_administrator_access_with_mfa'), ('iam_avoid_root_usage', 'iam_avoid_root_usage'), ('iam_aws_attached_policy_no_administrative_privileges', 'iam_aws_attached_policy_no_administrative_privileges'), ('iam_check_saml_providers_sts', 'iam_check_saml_providers_sts'), ('iam_customer_attached_policy_no_administrative_privileges', 'iam_customer_attached_policy_no_administrative_privileges'), ('iam_customer_unattached_policy_no_administrative_privileges', 'iam_customer_unattached_policy_no_administrative_privileges'), ('iam_disable_30_days_credentials', 'iam_disable_30_days_credentials'), ('iam_disable_45_days_credentials', 'iam_disable_45_days_credentials'), ('iam_disable_90_days_credentials', 'iam_disable_90_days_credentials'), ('iam_inline_policy_no_administrative_privileges', 'iam_inline_policy_no_administrative_privileges'), ('iam_no_custom_policy_permissive_role_assumption', 'iam_no_custom_policy_permissive_role_assumption'), ('iam_no_expired_server_certificates_stored', 'iam_no_expired_server_certificates_stored'), ('iam_no_root_access_key', 'iam_no_root_access_key'), ('iam_password_policy_expires_passwords_within_90_days_or_less', 'iam_password_policy_expires_passwords_within_90_days_or_less'), ('iam_password_policy_minimum_length_14', 'iam_password_policy_minimum_length_14'), ('iam_password_policy_number', 'iam_password_policy_number'), ('iam_password_policy_lowercase', 'iam_password_policy_lowercase'), ('iam_password_policy_reuse_24', 'iam_password_policy_reuse_24'), ('iam_password_policy_symbol', 'iam_password_policy_symbol'), ('iam_password_policy_uppercase', 'iam_password_policy_uppercase'), ('iam_policy_allows_privilege_escalation', 'iam_policy_allows_privilege_escalation'), ('iam_policy_attached_only_to_group_or_roles', 'iam_policy_attached_only_to_group_or_roles'), ('iam_policy_no_full_access_to_cloudtrail', 'iam_policy_no_full_access_to_cloudtrail'), ('iam_policy_no_full_access_to_kms', 'iam_policy_no_full_access_to_kms'), ('iam_role_administratoraccess_policy', 'iam_role_administratoraccess_policy'), ('iam_role_cross_account_readonlyaccess_policy', 'iam_role_cross_account_readonlyaccess_policy'), ('iam_role_cross_service_confused_deputy_prevention', 'iam_role_cross_service_confused_deputy_prevention'), ('iam_root_hardware_mfa_enabled', 'iam_root_hardware_mfa_enabled'), ('iam_root_mfa_enabled', 'iam_root_mfa_enabled'), ('iam_rotate_access_key_90_days', 'iam_rotate_access_key_90_days'), ('iam_securityaudit_role_created', 'iam_securityaudit_role_created'), ('iam_support_role_created', 'iam_support_role_created'), ('iam_user_hardware_mfa_enabled', 'iam_user_hardware_mfa_enabled'), ('iam_user_mfa_enabled', 'iam_user_mfa_enabled'), ('iam_user_no_administrator_access', 'iam_user_no_administrator_access'), ('iam_user_no_setup_initial_access_key', 'iam_user_no_setup_initial_access_key'), ('iam_user_two_active_access_keys', 'iam_user_two_active_access_keys')], enum_class=iam.models.IamEnum, max_length=60)),
                ('check_code', models.CharField(max_length=255)),
                ('importance', django_enumfield.db.fields.EnumField(default=1, enum=iam.models.IMPORTANCE)),
                ('status', models.BooleanField()),
                ('pass_line', models.TextField()),
                ('check_point', models.TextField()),
                ('modified_data', models.DateTimeField()),
                ('iam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iam_list_entries', to='iam.iam')),
                ('root_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iam_list_records', to='users.user')),
            ],
        ),
    ]
