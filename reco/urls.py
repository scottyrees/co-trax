from django.conf.urls import url
from . import views


app_name = 'reco'
urlpatterns = [
    url(r'^$', views.public_overview, name='public_overview'),
    url(r'^corporate/$', views.public_corporate, name='public_corporate'),
    url(r'^contact/$', views.public_contact, name='public_contact'),
    url(r'^company_select/$', views.company_select, name='company_select'),
    url(r'^(?P<pk>[0-9]+)/home/$', views.company_home, name='company_home'),
    url(r'^(?P<pk>[0-9]+)/directors/$', views.company_directors, name='company_directors'),
    url(r'^(?P<pk>[0-9]+)/shareholdings/$', views.company_sharelog, name='company_sharelog'),
    url(r'^(?P<pk>[0-9]+)/shareholdings/history/$', views.sharelog_history, name='sharelog_history'),

    url(r'^(?P<pk>[0-9]+)/properties/$', views.buildings_list, name='buildings_list'),
    url(r'^(?P<pk>[0-9]+)/properties/add/$', views.add_building, name='add_building'),
    url(r'^(?P<pk>[0-9]+)/properties/(?P<pk1>[0-9]+)/$', views.building_detail, name='building_detail'),
    url(r'^(?P<pk>[0-9]+)/properties/(?P<pk1>[0-9]+)/unit/(?P<pk2>[0-9]+)/$', views.unit_detail, name='unit_detail'),
    url(r'^(?P<pk>[0-9]+)/properties/(?P<pk1>[0-9]+)/unit/add/$', views.add_unit, name='add_unit'),
    url(r'^(?P<pk>[0-9]+)/properties/(?P<pk1>[0-9]+)/unit/(?P<pk2>[0-9]+)/edit/$', views.edit_unit, name='edit_unit'),
    url(r'^(?P<pk>[0-9]+)/properties/(?P<pk1>[0-9]+)/unit/(?P<pk2>[0-9]+)/remove/$', views.remove_unit, name='remove_unit'),
    url(r'^(?P<pk>[0-9]+)/properties/(?P<pk1>[0-9]+)/unit/(?P<pk2>[0-9]+)/tenant/add/$', views.add_tenant, name='add_tenant'),
    url(r'^(?P<pk>[0-9]+)/properties/(?P<pk1>[0-9]+)/unit/(?P<pk2>[0-9]+)/tenant/(?P<pk3>[0-9]+)/$', views.tenant_detail, name='tenant_detail'),
    url(r'^(?P<pk>[0-9]+)/properties/(?P<pk1>[0-9]+)/unit/(?P<pk2>[0-9]+)/tenant/(?P<pk3>[0-9]+)/add_payment/$', views.add_tenant_payment, name='add_tenant_payment'),

    url(r'^(?P<pk>[0-9]+)/accounting/$', views.accounting_overview, name='accounting_overview'),
    url(r'^(?P<pk>[0-9]+)/accounting/banking/accounts/$', views.bank_accounts, name='bank_accounts'),
    url(r'^(?P<pk>[0-9]+)/accounting/banking/accounts/(?P<pk4>[0-9]+)/$', views.transaction_log, name='transaction_log'),
    url(r'^(?P<pk>[0-9]+)/accounting/banking/accounts/(?P<pk4>[0-9]+)/add_transaction/$', views.add_transaction, name='add_transaction'),
    url(r'^(?P<pk>[0-9]+)/accounting/creditcards/accounts/$', views.creditcard_accounts, name='creditcard_accounts'),
    url(r'^(?P<pk>[0-9]+)/accounting/mortgages/accounts/$', views.mortgage_accounts, name='mortgage_accounts'),
    url(r'^(?P<pk>[0-9]+)/accounting/loans/receivable/$', views.loans_receivable, name='loans_receivable'),
    url(r'^(?P<pk>[0-9]+)/accounting/loans/payable/$', views.loans_payable, name='loans_payable'),
    url(r'^(?P<pk>[0-9]+)/accounting/current/receivable/$', views.accounts_receivable, name='accounts_receivable'),
    url(r'^(?P<pk>[0-9]+)/accounting/current/payable/$', views.accounts_payable, name='accounts_payable'),
    url(r'^(?P<pk>[0-9]+)/accounting/current/payable/add/$', views.add_ap, name='add_ap'),
    url(r'^(?P<pk>[0-9]+)/accounting/staff/$', views.staff_list, name='staff_list'),
    
    url(r'^(?P<pk>[0-9]+)/financials/$', views.financials_view, name='financials_view'),
    url(r'^(?P<pk>[0-9]+)/balance_sheet/$', views.balance_sheet, name='balance_sheet'),
    url(r'^(?P<pk>[0-9]+)/income_statement/$', views.income_statement, name='income_statement'),
    url(r'^(?P<pk>[0-9]+)/cashflow_statement/$', views.cashflow_statement, name='cashflow_statement'),
    url(r'^(?P<pk>[0-9]+)/equity_plot/$', views.equity_plot, name='equity_plot'),

    url(r'^(?P<pk>[0-9]+)/archive/$', views.archive_view, name='archive_view'),
]
