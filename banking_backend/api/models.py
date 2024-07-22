from django.db import models

class CustomerInformation(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    default_status = models.IntegerField()
    bankruptcy_indicator = models.IntegerField()
    credit_inquiries_past_6_months = models.IntegerField()
    months_since_last_inquiry = models.IntegerField()
    percentage_open_accounts = models.DecimalField(max_digits=5, decimal_places=2)
    percentage_open_accounts_past_24_months = models.DecimalField(max_digits=5, decimal_places=2)
    total_open_accounts = models.IntegerField()
    total_credit_limit_sum = models.DecimalField(max_digits=10, decimal_places=2)
    max_credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_high_balance_accounts = models.DecimalField(max_digits=5, decimal_places=2)
    percentage_satisfied_accounts = models.DecimalField(max_digits=5, decimal_places=2)
    bad_derogatory_marks_count = models.IntegerField()
    satisfied_accounts_count = models.IntegerField()
    months_since_first_credit_account = models.IntegerField()
    months_since_last_credit_account = models.IntegerField()
    delinquent_accounts_30_to_60_days_past_24_months = models.IntegerField()
    delinquent_accounts_90_days_past_24_months = models.IntegerField()
    total_delinquent_accounts_60_days = models.IntegerField()

    def __str__(self):
        return self.name

class AccountInformation(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    account_status = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    overdraft_limit = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    date_opened = models.DateField()
    date_closed = models.DateField(null=True, blank=True)
    monthly_fee = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_balance_required = models.DecimalField(max_digits=10, decimal_places=2)
    last_transaction_date = models.DateField()
    total_deposits = models.DecimalField(max_digits=10, decimal_places=2)
    total_withdrawals = models.DecimalField(max_digits=10, decimal_places=2)
    total_transactions = models.IntegerField()

    def __str__(self):
        return self.account_number

class TransactionInformation(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(AccountInformation, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.transaction_type} - {self.transaction_amount}'

class LoanInformation(models.Model):
    loan_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE)
    dependents = models.IntegerField()
    education = models.CharField(max_length=50)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_type = models.CharField(max_length=50)
    loan_term = models.CharField(max_length=50)
    collateral = models.CharField(max_length=50)
    loan_status = models.CharField(max_length=50)
    applicant_income = models.IntegerField()
    coapplicant_income = models.IntegerField()

    def __str__(self):
        return f'{self.loan_type} - {self.loan_amount}'

class CreditCardInformation(models.Model):
    credit_card_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    credit_card_status = models.CharField(max_length=50)
    credit_card_application_date = models.DateField()

    def __str__(self):
        return f'Credit Card - {self.credit_card_id}'

