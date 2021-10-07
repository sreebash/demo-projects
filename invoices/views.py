from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from invoices.models import Invoice

from invoices.forms import InvoiceForm


def invoice(request):
    invoice_form = InvoiceForm()

    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST or None)
        if invoice_form.is_valid():
            invoice_form.save()
            return redirect('invoice:show_invoice')
        else:

            invoice_form = InvoiceForm()
            context = {
                'invoice_form': invoice_form,
            }
        return render(request, 'invoice.html', context)

    return render(request, 'invoice.html', {'invoice_form': invoice_form})


def show_invoice(request):
    invoice_list = Invoice.objects.all()
    return render(request, 'invoice_detail.html', {'invoice_list': invoice_list})


def invoice_render_pdf(request, *args, **kwargs):
    pk = kwargs.get('pk')
    invoice = get_object_or_404(Invoice, pk=pk)
    template_path = 'pdf2.html'
    context = {
        'invoice': invoice
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="invoice.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
