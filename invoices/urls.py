from django.urls import path

from invoices import views

app_name = 'invoice'

urlpatterns = [
    path('', views.invoice, name='invoice'),
    path('invoice/', views.show_invoice, name='show_invoice'),
    path('/pdf/<int:pk>/', views.invoice_render_pdf, name='invoice_pdf'),

]
