# your_app/utils.py

def generate_invoice(contract, invoice_number, ack_number, issue_date, start_date, end_date,irn,ackdate,sac,draft,taxamnt,main,tax,bank,company,created,login):
    # Retrieve relevant information from the contract object
    customer_contact_id = contract.customer_contact_id
    master_space_id = contract.master_space_id
    # Calculate tax amounts and total amount based on rent_amount
    rent_amount = contract.rent_amount
    tax_percentage = 9  # Example tax percentage
    cgst = round(rent_amount * (tax_percentage / 100), 2)
    sgst = round(rent_amount * (tax_percentage / 100), 2)
    total_amount = round(rent_amount + cgst + sgst, 2)

    # Construct the invoice data dictionary
    invoice_data = {
        'invoice_no': invoice_number,
        'customer_contact_id': customer_contact_id,
        'master_space_id': master_space_id,
        'contract_id': contract.id,
        'invoice_issue_date': issue_date,
        'ack_no': ack_number,
        'irn_no': irn,
        'tax_percentage':tax,
        'maintanence':main,
        'taxable_amount':taxamnt,
        'status':draft,
        'ack_date':ackdate,
        'sac_code':sac,
        'invoice_start_date': start_date,
        'invoice_end_date': end_date,
        'tax_amount_sum': rent_amount,
        'cgst': cgst,
        'sgst': sgst,
        'total_amount': total_amount,
        'due_date': end_date,
        'bank_id':bank.id,
        'company_id':company.id,
        'created_on':created,
        'created_by_id':login,
        # Include any other necessary fields for your invoice model
    }

    return invoice_data
