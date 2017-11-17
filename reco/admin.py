from django.contrib import admin
from .models import Province, Bank, Account_Holder, Account, Transaction
from .models import Expense_Category, Revenue_Category, Accounts_Payable, Payment_Status
from .models import Building_Category, Buildings, Units, Bedrooms, Tenants
from .models import Shareholder, Personal_Shareholder, Shareholder_Type, Shares_Transaction, Corporate_Shares, Personal_Shares, Director
admin.site.register(Province)
admin.site.register(Bank)
admin.site.register(Account_Holder)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Expense_Category)
admin.site.register(Revenue_Category)
admin.site.register(Building_Category)
admin.site.register(Buildings)
admin.site.register(Units)
admin.site.register(Bedrooms)
admin.site.register(Tenants)
admin.site.register(Accounts_Payable)
admin.site.register(Payment_Status)
admin.site.register(Shareholder_Type)
admin.site.register(Shareholder)
admin.site.register(Personal_Shareholder)
admin.site.register(Shares_Transaction)
admin.site.register(Corporate_Shares)
admin.site.register(Personal_Shares)
admin.site.register(Director)
