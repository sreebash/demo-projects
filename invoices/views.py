import datetime

from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import xlwt

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
    template_path = 'pdf.html'
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


def export_excel(request, *args, **kwargs):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Expense' + str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expense')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['INVOICE #', 'STATUS', 'DUE', 'DATE']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Invoice.objects.all().values_list('invoice_no', 'status', 'due', 'created_on')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response
