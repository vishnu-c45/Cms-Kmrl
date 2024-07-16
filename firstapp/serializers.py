from rest_framework import serializers
from .models import *


class CustomerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model=Customer
        fields=['customer_name','business_type','business_name']
        


class MetrotationSerailizer(serializers.ModelSerializer):
    customer=CustomerModelSerializer()
    class Meta:
        model = Customer_contact
        fields=['customer','email','phone_number','id']

class MyModelSerializer(serializers.ModelSerializer):
    customer_contact=MetrotationSerailizer()
    class Meta:
        model = Contract
        fields = ['contract_no','customer_contact','contract_period','invoice_start_date','agreement_date','id','status']

class Space_serializer(serializers.ModelSerializer):
    class Meta:
        model=Space
        fields=['id','space_name']

class InvoiceSerializer(serializers.ModelSerializer):
    master_space=Space_serializer()
    customer_contact=MetrotationSerailizer()
    class Meta:
        model=Invoices
        fields= ('__all__')

class ViewSpaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields=['id','space_name']

class SpaceModelSerializer(serializers.ModelSerializer):
    master_space=ViewSpaceModelSerializer()
    class Meta:
        model=Contract
        fields=['master_space']


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
        
class GrievanceSerializer(serializers.ModelSerializer):
    master_space=Space_serializer()
    class Meta:
        model = Customer_grievance
        fields = '__all__'

#space_view_details -Payment Data
class PaymentSerializer(serializers.ModelSerializer):
    customer=MetrotationSerailizer()
    class Meta:
        model=Payments_Data
        fields =('__all__')



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = login_table
        fields = '__all__'    


class GenralParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = General_parameter
        fields = ['gp_type','gp_value','id']        