from django import forms

from invoices.models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

        widgets = {
            'invoice_no': forms.TextInput(attrs={'class': 'form-control'}),
            # 'status': forms.TextInput(attrs={'class': 'form-control'}),
            'due': forms.TextInput(attrs={'class': 'form-control'})
        }
