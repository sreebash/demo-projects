from django.urls import path

from invoices import views

urlpatterns = [
    path('invoice/', views.invoice, name='invoice'),
    path('invoice/show/', views.invoice_show, name='invoice_show')

]
