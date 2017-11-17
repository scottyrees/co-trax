from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from .models import Buildings, Units, Tenants, Tenant_Payments, Account_Holder, Account, Transaction, Accounts_Payable, Payment_Status
from .models import Shareholder_Type, Shareholder, Personal_Shareholder, Shares_Transaction, Corporate_Shares, Personal_Shares, Director
from .forms import AddBuildingForm, AddUnitForm, AddTenantForm, AddTenantPaymentForm, AddTransactionForm, AddAccountsPayableForm
from django.contrib.auth.decorators import login_required
from itertools import chain

def public_overview(request):
    return render(request, 'reco/public.html', {})

def public_corporate(request):
    return render(request, 'reco/public_corporate.html', {})

def public_contact(request):
    return render(request, 'reco/public_contact.html', {})

@login_required
def company_select(request):
    companies = Account_Holder.objects.filter(entry_by=request.user)
    return render(request, 'reco/company_select.html', {'companies':companies})

@login_required
def company_home(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    t1 = Personal_Shares.objects.filter(company__pk=pk)
    t2 = Corporate_Shares.objects.filter(company__pk=pk)
    result_list = sorted(chain(t1,t2),key=lambda instance: instance.transaction_date)

    share_count = 0
    for i in result_list:
        if str(i.transaction_type) == 'Issue':
            share_count += i.number_of_shares
        elif str(i.transaction_type) == 'Cancel':
            share_count -= i.number_of_shares

    return render(request, 'reco/company_home.html', {'company':company, 'share_count':share_count})

@login_required
def company_directors(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    directors = Director.objects.filter(company__pk=pk)
    return render(request, 'reco/company_directors.html', {'company':company, 'directors':directors})

@login_required
def company_sharelog(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    s1 = Personal_Shareholder.objects.filter(company__pk=pk)
    s2 = Shareholder.objects.filter(company__pk=pk)
    result_list = sorted(chain(s1,s2),key=lambda instance: instance.name)
    shareholdings = []
    for sh in result_list:
        if str(sh.category) == 'Individual':
            transactions = Personal_Shares.objects.filter(shareholder__pk=sh.id)
        else:
            transactions = Corporate_Shares.objects.filter(shareholder__pk=sh.id)
        tally = 0
        for t in transactions:
            if str(t.transaction_type) == 'Issue':
                tally += t.number_of_shares
            elif str(t.transaction_type) == 'Buy':
                tally += t.number_of_shares
            else:
                tally -= t.number_of_shares
        shareholdings.append(tally)
    total_shares = sum(shareholdings)
    percents = []
    for i in shareholdings:
        percents.append(round(100*i/total_shares,2))
    data = zip(result_list, shareholdings, percents)
    return render(request, 'reco/sharelog.html', {'company':company, 'total_shares':total_shares, 'data':data})

@login_required
def sharelog_history(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    t1 = Personal_Shares.objects.filter(company__pk=pk)
    t2 = Corporate_Shares.objects.filter(company__pk=pk)
    result_list = sorted(chain(t1,t2),key=lambda instance: instance.transaction_date)
    return render(request, 'reco/sharelog_history.html', {'company':company, 'result_list':result_list})

@login_required
def buildings_list(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    buildings = Buildings.objects.filter(owner__pk=pk).order_by('name')
    units = []
    vacancies = []
    rent = []
    for building in buildings:
        u=len(Units.objects.filter(building__name=building))
        units.append(u)
        tenants=Tenants.objects.filter(building__name=building).filter(moveout_date=None)
        t=len(tenants)
        vacancies.append(u-t)
        r=0
        for tenant in tenants:
            r += tenant.current_rent
        rent.append(r)
    data = zip(buildings, units, vacancies, rent)
    unitsum = sum(units)
    vacantsum = sum(vacancies)
    rentsum = sum(rent)
    return render(request, 'reco/buildings_list.html', {'company':company, 'data':data, 'unitsum': unitsum, 'vacantsum':vacantsum, 'rentsum':rentsum})

@login_required
def building_detail(request, pk, pk1):
    company = get_object_or_404(Account_Holder, pk=pk)
    building = get_object_or_404(Buildings, pk=pk1)
    units = Units.objects.filter(building__pk=pk1).order_by('roomnumber')
    number_of_units = len(units)
    tenants = Tenants.objects.filter(building__pk=pk1).filter(moveout_date=None)
    number_of_vacancies = number_of_units - len(tenants)
    bedrooms, tenantlist, startdate, renewaldate, rentlist = [], [], [], [], []
    for unit in units:
        bedrooms.append(unit.bedrooms)
        count = 0
        for tenant in tenants:
            if unit.roomnumber != str(tenant.unit):
                count += 1
            else:
                tenantlist.append(str(tenant.lname + ", " + tenant.fname))
                startdate.append(tenant.start_date)
                renewaldate.append(tenant.contract_renewal)
                rentlist.append(tenant.current_rent)
                break
        if count == len(tenants):
            tenantlist.append('Vacant')
            startdate.append('-')
            renewaldate.append('-')
            rentlist.append(0)
    data = zip(units, bedrooms, tenantlist, startdate, renewaldate, rentlist)
    roomsum = sum(bedrooms)
    rentsum = sum(rentlist)
    return render(request, 'reco/building_detail.html', {'company': company, 'building': building, 'units': units, 'roomsum': roomsum, 'rentsum': rentsum, 'data': data, 'tenants': tenants, 'number_of_units': number_of_units, 'number_of_vacancies': number_of_vacancies})

@login_required
def add_unit(request, pk, pk1):
    company = get_object_or_404(Account_Holder, pk=pk)
    building = get_object_or_404(Buildings, pk=pk1)
    if request.method == "POST":
        form = AddUnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.building = building
            unit.save()
            return redirect('reco:building_detail', pk=company.id, pk1=building.id)
    else:
        form = AddUnitForm()
        return render(request, 'reco/add_unit.html', {'form': form})


@login_required
def edit_unit(request, pk, pk1, pk2):
    company = get_object_or_404(Account_Holder, pk=pk)
    building = get_object_or_404(Buildings, pk=pk1)
    unit = get_object_or_404(Units, pk=pk2)
    if request.method == "POST":
        form = AddUnitForm(request.POST, instance=unit)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.building = building
            unit.save()
            return redirect('reco:building_detail', pk=company.id, pk1=building.id)
        else:
            form = AddUnitForm(instance=unit)
            return render(request, 'reco/add_unit.html', {'form': form})
        
@login_required
def remove_unit(request, pk, pk1, pk2):
    company = get_object_or_404(Account_Holder, pk=pk)
    building = get_object_or_404(Buildings, pk=pk1)
    unit = get_object_or_404(Units, pk=pk2)
    unit.delete()
    return redirect('reco:building_detail', pk=company.id, pk1=building.id)



@login_required
def unit_detail(request, pk, pk1, pk2):
    company = get_object_or_404(Account_Holder, pk=pk)
    unit = get_object_or_404(Units, pk=pk2)
    building = get_object_or_404(Buildings, pk=pk1)
    tenants = Tenants.objects.filter(unit__roomnumber=unit).order_by('-start_date')
    return render(request, 'reco/unit_detail.html', {'company':company, 'unit': unit, 'tenants': tenants, 'building': building})

@login_required
def add_tenant(request, pk, pk1, pk2):
    company = get_object_or_404(Account_Holder, pk=pk)
    building = get_object_or_404(Buildings, pk=pk1)
    unit = get_object_or_404(Units, pk=pk2)
    if request.method == "POST":
        form = AddTenantForm(request.POST)
        if form.is_valid():
            tenant = form.save(commit=False)
            tenant.building = building
            tenant.unit = unit
            tenant.save()
            return redirect('reco:unit_detail', pk=company.id, pk1=building.id, pk2=unit.id)
    else:
        form = AddTenantForm()
    return render(request, 'reco/add_tenant.html', {'form': form})

@login_required
def tenant_detail(request, pk, pk1, pk2, pk3):
    company = get_object_or_404(Account_Holder, pk=pk)
    unit = get_object_or_404(Units, pk=pk2)
    building = get_object_or_404(Buildings, pk=pk1)
    tenant = get_object_or_404(Tenants, pk=pk3)
    payments = Tenant_Payments.objects.filter(tenant__pk=pk3).order_by('-date')
    return render(request, 'reco/tenant_details.html', {'company':company, 'unit': unit, 'tenant': tenant, 'building': building, 'payments': payments})

@login_required
def add_tenant_payment(request, pk, pk1, pk2, pk3):
    company = get_object_or_404(Account_Holder, pk=pk)
    building = get_object_or_404(Buildings, pk=pk1)
    unit = get_object_or_404(Units, pk=pk2)
    tenant = get_object_or_404(Tenants, pk=pk3)
    if request.method == "POST":
        form = AddTenantPaymentForm(request.POST)
        if form.is_valid():
            tenant_payment = form.save(commit=False)
            tenant_payment.tenant = tenant
            tenant_payment.save()
            return redirect('reco:tenant_detail', pk=company.id, pk1=building.id, pk2=unit.id, pk3=tenant.id)
    else:
        form = AddTenantPaymentForm()
        return render(request, 'reco/add_tenant_payment.html', {'form': form})



@login_required
def add_building(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    if request.method == "POST":
        form = AddBuildingForm(request.POST)
        if form.is_valid():
            building = form.save(commit=False)
            building.save()
            return redirect('reco:buildings_list', pk=company.id)
    else:
        form = AddBuildingForm()
    return render(request, 'reco/add_building.html', {'form': form})

@login_required
def accounting_overview(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    return render(request, 'reco/accounting_overview.html', {'company':company})

@login_required
def bank_accounts(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    accounts = Account.objects.filter(account_holder__pk=pk).order_by('bank')
    account_balance = []
    for account in accounts:
        transactions = Transaction.objects.filter(account__pk=account.id)
        tran_sum = 0
        for transaction in transactions:
            tran_sum += transaction.value
        account_balance.append(round(tran_sum,2))
    data = zip(accounts,account_balance)
    return render(request, 'reco/bank_accounts.html', {'company':company, 'data':data})

@login_required
def transaction_log(request, pk, pk4):
    company = get_object_or_404(Account_Holder, pk=pk)
    account = get_object_or_404(Account, pk=pk4)
    transactions = Transaction.objects.filter(account__pk=pk4).order_by('transaction_date')
    balances = []
    balance = 0
    for transaction in transactions:
        balance += transaction.value
        balances.append(round(balance,2))
    transactions_reversed = transactions.order_by('-transaction_date')
    balances_reversed = balances[::-1]            
    data = zip(transactions_reversed,balances_reversed)
    return render(request, 'reco/transaction_record.html', {'company':company, 'account':account, 'data':data})

@login_required
def add_transaction(request, pk, pk4):
    company = get_object_or_404(Account_Holder, pk=pk)
    account = get_object_or_404(Account, pk=pk4)
    if request.method == "POST":
        form = AddTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.account = account
            transaction.entry_by = request.user
            transaction.entry_date = timezone.now()
            transaction.save()
            return redirect('reco:transaction_log', pk=company.id, pk4=account.id)
    else:
        form = AddTransactionForm()
        return render(request, 'reco/add_transaction.html', {'form': form})

@login_required
def creditcard_accounts(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    return render(request, 'reco/creditcard_accounts.html', {'company':company})

@login_required
def mortgage_accounts(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    return render(request, 'reco/mortgage_accounts.html', {'company':company})

@login_required
def loans_receivable(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    return render(request, 'reco/loans_receivable.html', {'company':company})

@login_required
def loans_payable(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    return render(request, 'reco/loans_payable.html', {'company':company})

@login_required
def accounts_receivable(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    ap_list = Accounts_Payable.objects.filter(bill_to__pk=1).order_by('-invoice_date')
    return render(request, 'reco/accounts_receivable.html', {'company': company})

@login_required
def accounts_payable(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    ap_list = Accounts_Payable.objects.filter(bill_to__pk=1).order_by('-invoice_date')
    return render(request, 'reco/accounts_payable.html', {'company': company, 'ap_list': ap_list})

@login_required
def add_ap(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    if request.method == "POST":
        form = AddAccountsPayableForm(request.POST)
        if form.is_valid():
            ap_item = form.save(commit=False)
            ap_item.bill_to = company
            ap_item.save()
            return redirect('reco:accounts_payable_view', pk=company.id)
    else:
        form = AddAccountsPayableForm()
        return render(request, 'reco/add_ap.html', {'form': form})

@login_required
def staff_list(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    return render(request, 'reco/staff_list.html', {'company':company})

@login_required
def financials_view(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    return render(request, 'reco/financials.html', {'company':company})


@login_required
def archive_view(request, pk):
    company = get_object_or_404(Account_Holder, pk=pk)
    return render(request, 'reco/archive.html', {'company':company})

