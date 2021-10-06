from django.shortcuts import render, redirect
from invoices.models import Invoice

from invoices.forms import InvoiceForm


def invoice(request):
    invoice_form = InvoiceForm()

    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST or None)
        if invoice_form.is_valid():
            invoice_form.save()
            return redirect('invoice:invoice_show')
        else:

            invoice_form = InvoiceForm()
            context = {
                'invoice_form': invoice_form,
            }
        return render(request, 'invoice.html', context)

    return render(request, 'invoice.html', {'invoice_form': invoice_form})


def invoice_show(request):
    invoice_list = Invoice.objects.all()
    return render(request, 'invoice_detail.html', {'invoice_list': invoice_list})
