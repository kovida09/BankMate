# Generated by Django 5.0.7 on 2024-07-22 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInformation',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pin_code', models.CharField(max_length=10)),
                ('default_status', models.IntegerField()),
                ('bankruptcy_indicator', models.IntegerField()),
                ('credit_inquiries_past_6_months', models.IntegerField()),
                ('months_since_last_inquiry', models.IntegerField()),
                ('percentage_open_accounts', models.DecimalField(decimal_places=2, max_digits=5)),
                ('percentage_open_accounts_past_24_months', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_open_accounts', models.IntegerField()),
                ('total_credit_limit_sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_credit_limit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percentage_high_balance_accounts', models.DecimalField(decimal_places=2, max_digits=5)),
                ('percentage_satisfied_accounts', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bad_derogatory_marks_count', models.IntegerField()),
                ('satisfied_accounts_count', models.IntegerField()),
                ('months_since_first_credit_account', models.IntegerField()),
                ('months_since_last_credit_account', models.IntegerField()),
                ('delinquent_accounts_30_to_60_days_past_24_months', models.IntegerField()),
                ('delinquent_accounts_90_days_past_24_months', models.IntegerField()),
                ('total_delinquent_accounts_60_days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CreditCardInformation',
            fields=[
                ('credit_card_id', models.AutoField(primary_key=True, serialize=False)),
                ('credit_limit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit_card_status', models.CharField(max_length=50)),
                ('credit_card_application_date', models.DateField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customerinformation')),
            ],
        ),
        migrations.CreateModel(
            name='AccountInformation',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_type', models.CharField(max_length=50)),
                ('account_number', models.CharField(max_length=50)),
                ('account_status', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit_limit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('overdraft_limit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_opened', models.DateField()),
                ('date_closed', models.DateField(blank=True, null=True)),
                ('monthly_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('minimum_balance_required', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_transaction_date', models.DateField()),
                ('total_deposits', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_withdrawals', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_transactions', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customerinformation')),
            ],
        ),
        migrations.CreateModel(
            name='LoanInformation',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('dependents', models.IntegerField()),
                ('education', models.CharField(max_length=50)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loan_type', models.CharField(max_length=50)),
                ('loan_term', models.CharField(max_length=50)),
                ('collateral', models.CharField(max_length=50)),
                ('loan_status', models.CharField(max_length=50)),
                ('applicant_income', models.IntegerField()),
                ('coapplicant_income', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customerinformation')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionInformation',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateField()),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_type', models.CharField(max_length=50)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accountinformation')),
            ],
        ),
    ]