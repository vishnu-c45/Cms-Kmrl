# Create your models here.
from django.db import models


class Notification(models.Model):
    message = models.TextField()
    profile_pic=models.CharField(max_length=225,null=True)
    name=models.CharField(max_length=225,null=True)
    invoice_no=models.CharField(max_length=225,null=True)
    time = models.DateTimeField(auto_now_add=True)
    type=models.IntegerField(null=True)
    status=models.IntegerField(null=True)
    color = models.CharField(max_length=20,null=True)
    customer = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.message    


class login_table(models.Model):
    login_name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255)
    profile_pic = models.FileField( upload_to="media/uploadedimages/",null=True,blank=True,default='')
    password = models.CharField(max_length=255)
    usertype = models.IntegerField(null=True)
    phno = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=255,null=True)
    otp = models.IntegerField(null=True)
    customer_id=models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    created_on = models.DateTimeField(null=True)
    created_by = models.IntegerField(null=True)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)
    notifications = models.ManyToManyField('Notification')


    def __str__(self):
        return self.username


class Metrostation(models.Model):
    station_name = models.CharField(max_length=255, null=True)
    s_name = models.CharField(max_length=255, null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    status = models.IntegerField(null=True)
    created_on = models.DateTimeField(null=True)
    created_by = models.IntegerField(null=True)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)


class MetroStationContact(models.Model):
    metrostation = models.ForeignKey(Metrostation, null=True, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, null=True)
    district = models.CharField(max_length=255, null=True)
    pincode = models.IntegerField(null=True)
    email = models.CharField(max_length=255, null=True)
    phone_number = models.BigIntegerField(null=True)
    status = models.IntegerField(null=True)
    created_on = models.DateTimeField(null=True)
    created_by = models.IntegerField(null=True)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)


class Space(models.Model):
    metrostation = models.ForeignKey(MetroStationContact, null=True, on_delete=models.CASCADE)
    space_name = models.CharField(max_length=255, null=True)
    master_space = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,related_name='sub_spaces')
    space_type = models.CharField(max_length=255, null=True)
    area_type = models.CharField(max_length=255, null=True)
    area_side = models.CharField(max_length=255, null=True)
    area_level = models.CharField(max_length=255, null=True)
    area = models.BigIntegerField(null=True)
    vacancy_status = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    created_on = models.DateTimeField(null=True)
    created_by = models.ForeignKey(login_table, null=True, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)


class Customer(models.Model):
    customer_number = models.BigIntegerField(null=True)
    customer_name = models.CharField(max_length=250, null=True)
    business_type = models.CharField(max_length=250, null=True)
    business_name = models.CharField(max_length=250, null=True)
    status = models.IntegerField(null=True)
    created_on = models.DateTimeField(null=True)
    created_by = models.ForeignKey(login_table, null=True, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)


class Customer_contact(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=225, null=True)
    phone_number = models.BigIntegerField(null=True)
    password= models.CharField(max_length=255,null=True)
    username = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=225, null=True)
    district = models.CharField(max_length=225, null=True)
    pincode = models.IntegerField(null=True)
    address = models.CharField(max_length=225, null=True)
    gst_no = models.CharField(max_length=225, null=True)
    pan_no = models.CharField(max_length=225, null=True)
    state_code = models.IntegerField(null=True)
    state = models.CharField(max_length=225, null=True)
    status = models.IntegerField(null=True)
    created_on = models.DateTimeField(null=True)
    created_by = models.ForeignKey(login_table, null=True, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)
    customer_notifications = models.ManyToManyField


class Contract(models.Model):
    customer_contact = models.ForeignKey(
        Customer_contact, null=True, on_delete=models.CASCADE)
    master_space = models.ForeignKey(
        Space, null=True, on_delete=models.CASCADE)
    contract_no = models.CharField(max_length=225, null=True)
    agreement_number = models.CharField(max_length=225, null=True)
    agreement_date = models.DateField(null=True)
    auction_number = models.CharField(max_length=225, null=True)
    auction_date = models.DateField(null=True)
    auction_notice_number = models.CharField(max_length=225, null=True)
    auction_notice_date = models.DateField(null=True)
    auction_notice_ref_number = models.CharField(max_length=225, null=True)
    auction_notice_ref_date = models.DateField(null=True)
    final_allotment_order_number = models.CharField(max_length=225, null=True)
    final_allotment_order_date = models.DateField(null=True)
    rfp_number = models.CharField(max_length=225, null=True)
    rfp_date = models.DateField(null=True)
    rfp_ref_number = models.CharField(max_length=225, null=True)
    rfp_ref_date = models.DateField(null=True)
    loa_number = models.CharField(max_length=225, null=True)
    loa_date = models.DateField(null=True)
    invoice_start_date = models.DateField(null=True)
    termination_date = models.DateField(null=True)
    tenure_start_date = models.DateField(null=True)
    tenure_end_date = models.DateField(null=True)
    contract_period = models.IntegerField(null=True)
    fitment_period = models.IntegerField(null=True)
    lock_in_period = models.IntegerField(null=True)
    bill_start_date = models.DateField(null=True)
    rent_amount = models.BigIntegerField(null=True)
    utility_charges = models.BigIntegerField(null=True)
    cam_charges = models.IntegerField(null=True)
    security_deposit = models.BigIntegerField(null=True)
    hikes = models.IntegerField(null=True)
    sq_ft_rate = models.IntegerField(null=True)
    auth_sign = models.CharField(max_length=225, null=True)
    desiginations = models.CharField(max_length=225, null=True)
    status = models.IntegerField(null=True)
    created_on = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        login_table, null=True, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)


class Company_details(models.Model):
    company_name = models.CharField(max_length=225, null=True)
    city = models.CharField(max_length=225, null=True)
    district = models.CharField(max_length=225, null=True)
    state = models.CharField(max_length=225, null=True)
    pincode = models.IntegerField(null=True)
    address = models.CharField(max_length=225, null=True)
    gst_no = models.CharField(max_length=225, null=True)
    pan_no = models.CharField(max_length=225, null=True)
    cin = models.CharField(max_length=225, null=True)
    phno1 = models.CharField(max_length=225,null=True)
    phno2 = models.CharField(max_length=225,null=True)
    fax = models.CharField(max_length=225,null=True)
    email = models.CharField(max_length=225, null=True)
    website = models.CharField(max_length=225, null=True)
    state_code = models.IntegerField(null=True)
    signature = models.FileField( upload_to="media/uploadedimages/",null=True,blank=True,default='')
    created_on = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        login_table, null=True, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)

class Bank(models.Model):
    bank_name = models.CharField(max_length=225, null=True)
    branch_name = models.CharField(max_length=225, null=True)
    acc_no = models.BigIntegerField(null=True)
    ifsc_code = models.CharField(max_length=225, null=True)
    upi_id = models.CharField(max_length=225, null=True)
    status = models.IntegerField(null=True)
    created_on = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        login_table, null=True, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)

class Invoices(models.Model):
    bank = models.ForeignKey(
        Bank, null=True, on_delete=models.CASCADE)
    customer_contact = models.ForeignKey(
        Customer_contact, related_name='invoices',related_query_name='invoice', null=True, on_delete=models.CASCADE)
    master_space = models.ForeignKey(
        Space, null=True, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, null=True, on_delete=models.CASCADE)
    company = models.ForeignKey(Company_details,null=True, on_delete=models.CASCADE)
    invoice_no = models.BigIntegerField(null=True)
    invoice_issue_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    irn_no = models.CharField(max_length=225, null=True)
    ack_no = models.BigIntegerField(null=True)
    ack_date = models.DateField(null=True)
    invoice_start_date = models.DateField(null=True)
    invoice_end_date = models.DateField(null=True)
    sac_code = models.BigIntegerField(null=True)
    taxable_amount = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    maintanence = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    tax_percentage = models.IntegerField(null=True)
    sgst = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    cgst = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    tax_amount_sum = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    status = models.IntegerField(null=True)
    created_on = models.DateField(null=True)
    created_by = models.ForeignKey(
        login_table, null=True, on_delete=models.CASCADE)
    updated_on = models.DateField(null=True)
    updated_by = models.IntegerField(null=True)

class Customer_grievance(models.Model):
    customer_contact = models.ForeignKey(
        Customer_contact, null=True, on_delete=models.CASCADE)
    master_space = models.ForeignKey(
        Space, null=True, on_delete=models.CASCADE)
    complaint_pic = models.FileField( upload_to="media/uploadedimages/",null=True,blank=True,default='')
    reason = models.CharField(max_length=225, null=True)
    complaint = models.CharField(max_length=225, null=True)
    reply = models.CharField(max_length=225, null=True)
    status = models.IntegerField(null=True)
    created_on = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        login_table, null=True, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)

class Payments_Data(models.Model): 
    customer=models.ForeignKey(Customer_contact, related_name='payments_data', related_query_name='payment',null=True,on_delete=models.CASCADE)
    invoice=models.ForeignKey(Invoices,null=True,on_delete=models.CASCADE)
    master_space = models.ForeignKey(
        Space, null=True, on_delete=models.CASCADE)
    transaction_id=models.CharField(max_length=225,null=True)
    payment_amount=models.DecimalField(null=True,max_digits=10, decimal_places=2)
    payment_method=models.CharField(max_length=225,null=True)
    payment_order_id=models.CharField(max_length=225,null=True)
    payment_signature=models.CharField(max_length=225,null=True)
    reciept_no=models.CharField(max_length=225,null=True)
    notification=models.CharField(max_length=225,null=True)  
    notification_status=models.IntegerField(null=True)
    status=models.IntegerField(null=True)
    created_on = models.DateField(null=True)
    created_by = models.ForeignKey(
        login_table, null=True, on_delete=models.CASCADE)


class CreditNote(models.Model):
    credit_note_number = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    invoice=models.ForeignKey(Invoices, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer_contact, on_delete=models.CASCADE, related_name='credit_notes')
    reference_invoice_number = models.CharField(max_length=50)
    reference_invoice_date = models.DateField()
    reason = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    terms_and_conditions = models.TextField()
    contact_info = models.TextField()

    def __str__(self):
        return self.credit_note_number
    

class General_parameter(models.Model):
    gp_type =models.CharField(max_length=225,null=True)
    gp_value=models.CharField(max_length=225,null=True)
    status = models.IntegerField(null=True)

class ContractUpload(models.Model):
    contract = models.ForeignKey(Contract, null=True, on_delete=models.CASCADE)
    file = models.FileField( upload_to="media/uploadedimages/",null=True,blank=True,default='')
    contracttype = models.IntegerField(null=True)
    created_on = models.DateField(null=True)
    created_by = models.ForeignKey(login_table, null=True, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)

class Utility(models.Model):
    power = models.IntegerField(null=True)
    water = models.BigIntegerField(null=True)
    powerpic = models.FileField( upload_to="media/uploadedimages/",null=True,blank=True,default='')
    waterpic = models.FileField( upload_to="media/uploadedimages/",null=True,blank=True,default='')
    metrostation = models.ForeignKey(MetroStationContact, null=True, on_delete=models.CASCADE)
    created_on = models.DateField(null=True)
    created_by = models.ForeignKey(login_table, null=True, on_delete=models.CASCADE)
    status = models.BigIntegerField(null=True)


class IntrestSpace(models.Model):
    space_id = models.ForeignKey(Space, null=True, on_delete=models.CASCADE)
    login_id =models.ForeignKey(login_table, null=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField(null=True)