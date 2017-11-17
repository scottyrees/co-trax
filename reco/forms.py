from django import forms

from .models import Buildings, Units, Tenants, Tenant_Payments, Account_Holder, Account, Transaction
from .models import Accounts_Payable, Expense_Category

class AddBuildingForm(forms.ModelForm):

    class Meta:
        model = Buildings
        fields = ('owner', 'name', 'building_type', 'legal_description', 'address', 'city', 'province', 'postalcode', 'year_built', 'purchase_date', 'purchase_price',)

class AddUnitForm(forms.ModelForm):

    class Meta:
        model = Units
        fields = ('roomnumber', 'bedrooms', 'sqft', 'description',)

class AddTenantForm(forms.ModelForm):

    class Meta:
        model = Tenants
        fields = ('lname', 'fname', 'tenant_bday', 'start_date', 'contract_renewal', 'current_rent', 'moveout_date',)


class AddTenantPaymentForm(forms.ModelForm):

    class Meta:
        model = Tenant_Payments
        fields = ('date', 'category', 'amount', 'description',)

class AddTransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('transaction_date', 'bank_description', 'value', 'user_description',)

class AddAccountsPayableForm(forms.ModelForm):

    class Meta:
        model = Accounts_Payable
        fields = ('invoice_date', 'expense_category', 'vendor', 'bill_value', 'document', 'payment_status')
        
