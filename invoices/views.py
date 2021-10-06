from django.shortcuts import render, redirect
from invoices.models import Invoice

from invoices.forms import InvoiceForm


def invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/invoice/show')
        else:
            form = InvoiceForm()
        return render(request, 'invoice.html', {'form': form})


def invoice_show(request):
    invoice_list = Invoice.objects.all()
    return render(request, 'invoice_show.html', {'invoice_list': invoice_list})

