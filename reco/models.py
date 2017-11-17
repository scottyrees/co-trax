from django.db import models
from django.utils import timezone

class Province(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Account_Holder(models.Model):
    name = models.CharField(max_length=100)
    entry_by = models.ForeignKey('auth.User',default='')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    province = models.ForeignKey('Province')
    postalcode = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Shareholder_Type(models.Model):
    category = models.CharField(max_length=25)

    def __str__(self):
        return self.category

class Shareholder(models.Model):
    company = models.ForeignKey('Account_Holder')
    category = models.ForeignKey('Shareholder_Type')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Personal_Shareholder(models.Model):
    company = models.ForeignKey('Account_Holder')
    category = models.ForeignKey('Shareholder_Type')
    name = models.CharField(max_length=25)
    fname = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name+', '+self.fname

class Shares_Transaction(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Corporate_Shares(models.Model):
    company = models.ForeignKey('Account_Holder')
    transaction_date = models.DateField()
    shareholder = models.ForeignKey('Shareholder',default=None)
    transaction_type = models.ForeignKey('Shares_Transaction')
    number_of_shares = models.IntegerField()
    price = models.FloatField()

class Personal_Shares(models.Model):
    company = models.ForeignKey('Account_Holder')
    transaction_date = models.DateField()
    shareholder = models.ForeignKey('Personal_Shareholder',default=None)
    transaction_type = models.ForeignKey('Shares_Transaction')
    number_of_shares = models.IntegerField()
    price = models.FloatField()
    
class Director(models.Model):
    company = models.ForeignKey('Account_Holder')
    lname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    position = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.lname
 

class Account(models.Model):
    account_holder = models.ForeignKey('Account_Holder',default='')
    bank = models.ForeignKey('Bank', default=None)
    acct_number = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.acct_number

class Transaction(models.Model):
    account = models.ForeignKey('Account')
    entry_by = models.ForeignKey('auth.User')
    entry_date = models.DateTimeField(default=timezone.now)
    transaction_date = models.DateField(blank=True, null=True)
    bank_description = models.CharField(max_length=200)
    user_description = models.CharField(max_length=200)
    value = models.FloatField()
    
    def entry_submit(self):
        self.entry_date = timezone.now()
        self.save()

"""
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
"""



class Expense_Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Accounts_Payable(models.Model):
    bill_to = models.ForeignKey('Account_Holder')
    invoice_date = models.DateField(blank=True)
    expense_category = models.ForeignKey('Expense_Category')
    vendor = models.CharField(max_length=100)
    bill_value = models.FloatField()
    document = models.FileField(upload_to='documents/')
    payment_status = models.ForeignKey('Payment_Status')

    def __str__(self):
        return self.vendor

class Payment_Status(models.Model):
    status = models.CharField(max_length=25)
    def __str__(self):
        return self.status

class Revenue_Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Building_Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Buildings(models.Model):
    owner = models.ForeignKey('Account_Holder',null=True)
    building_type = models.ForeignKey('Building_Category',default='')
    name = models.CharField(max_length=50)
    legal_description = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.ForeignKey('Province')
    postalcode = models.CharField(max_length=10)
    year_built = models.IntegerField()
    purchase_date = models.DateField(null=True)
    purchase_price = models.FloatField(null=True)

    def __str__(self):
        return self.name



class Appraisals(models.Model):
    building = models.ForeignKey('Buildings')
    appraisal_by = models.CharField(max_length=50)
    appraisal_date = models.DateField(default=timezone.now)
    price = models.FloatField()

    def __str__(self):
        return self.building



class Units(models.Model):
    roomnumber = models.CharField(max_length=20)
    building = models.ForeignKey('Buildings')
    sqft = models.IntegerField()
    bedrooms = models.IntegerField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.roomnumber



class Bedrooms(models.Model):
    roomtype = models.CharField(max_length=20)

    def __str__(self):
        return self.roomtype



class Tenants(models.Model):
    lname = models.CharField(max_length=100, null=True)
    fname = models.CharField(max_length=100, null=True)
    tenant_bday = models.DateField()
    building = models.ForeignKey('Buildings',default=None)
    unit = models.ForeignKey('Units')
    start_date = models.DateField(default=timezone.now)
    contract_renewal = models.DateField(default=timezone.now)
    moveout_date = models.DateField(null=True, blank=True)
    current_rent = models.FloatField()
    
    def __str__(self):
        return self.lname

class Tenant_Payments(models.Model):
    tenant = models.ForeignKey('Tenants')
    date = models.DateField(default=timezone.now)
    category = models.ForeignKey('Revenue_Category',default='')
    amount = models.FloatField()
    description = models.CharField(max_length=100,blank=True)
    


