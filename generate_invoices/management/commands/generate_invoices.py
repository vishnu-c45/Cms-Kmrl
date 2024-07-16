from django.core.management.base import BaseCommand
from datetime import datetime
from calendar import monthrange
from firstapp.models import *
from firstapp.utils import generate_invoice 
from django.db.models import Max
from django.db.models import Q 

class Command(BaseCommand):
    help = 'Auto-generate invoices on a specific date each month'

    def handle(self, *args, **options):
        login_obj = login_table.objects.get(usertype=1)
        login_id = login_obj.id
        date = datetime.now().strftime('%Y-%m-%d')
        dates = datetime.now().date()
        contracts = Contract.objects.filter(status=1)
        max_invoice_number = Invoices.objects.aggregate(Max('invoice_no'))['invoice_no__max'] or 0
        max_ackno = Invoices.objects.aggregate(Max('ack_no'))['ack_no__max'] or 1516278315551
        _, last_day = monthrange(dates.year, dates.month)
        invoice_start_date = datetime(dates.year, dates.month, 1).strftime('%Y-%m-%d')
        invoice_end_date = datetime(dates.year, dates.month, last_day).strftime('%Y-%m-%d')
        irn_no='7c2903chwc9329e399ff3278fcc88678c9e999d87889sfv9990v954s67vs792defc1'
        ack_date=date
        sac_code=997212
        status=1
        tax_percentage=9
        created_on=date
        bank = Bank.objects.latest('id')
        try:
            company = Company_details.objects.latest('id')
        except Company_details.DoesNotExist:
            company = ''
        for p in contracts:
            maintanence = 0
            existing_invoice = Invoices.objects.filter(
                Q(contract_id=p.id) & Q(invoice_issue_date__year=dates.year,
                                       invoice_issue_date__month=dates.month) & Q(status__in=['1', '2', '3', '4'])
            ).exists()
            if existing_invoice:
                continue

            max_invoice_number += 1
            max_ackno += 1
            taxable_amount=p.rent_amount
            # Use the generate_invoice function to generate the invoice details
            invoice_data = generate_invoice(p, max_invoice_number, max_ackno, date, invoice_start_date,
                                            invoice_end_date,irn_no,ack_date,sac_code,status,taxable_amount,
                                            maintanence,tax_percentage,bank,company,created_on,login_id)

            # Create the invoice object
            Invoices.objects.create(**invoice_data)
