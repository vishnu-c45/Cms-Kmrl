



$('#submit').click(function(){
    // var Id=$('#submit').val();
    $("#companyform").validate({
        rules:{
            companyname:'required',
            city:'required',
            state:'required',
            district: 'required',
            state_code: 'required',
            address:'required',
            pincode: 'required',
            fax: 'required',
            phno1: 'required',
            phno2: 'required',
            cin: 'required',
            gst_no:'required',
            pan_no: 'required',
            email: 'required',
            website:'required',
            authsign: 'required',
           
        },
        messages:{
            companyname:'Please enter your company name',
            city:'Please enter your city',
            state:'Please enter your state',
            district: 'Please enter your district',
            state_code: 'Please enter your state code',
            address:'Please enter your address',
            pincode: 'Please enter your pincode',
            fax: 'Please enter your fax number',
            phno1: 'Please enter your phone number',
            phno2: 'Please enter your phone number',
            cin: 'Please enter your cin',
            gst_no:'Please enter your gst number',
            pan_no: 'Please enter your pan number',
            email: 'Please enter your email',
            website:'Please enter your website',
            authsign: 'Please upload signature',
           
        },
        submitHandler: function(){
            // var formdata=$('#companyform').serialize();
            var form = $('#companyform')[0];
            var formData = new FormData(form);
            $.ajax({
                method:'POST',
                url:'/add_company_details',
                datatype:'json',
                data: formData,
                processData: false,
                contentType: false,
                    

                success:function(){
                    showSuccessMessage();

                }
            
            })
        }
    });

});

function showSuccessMessage(message) {
    Swal.fire({
      icon: 'success',
      title: 'Company Details Added Successfully',
      text: message,
    }).then((result) => {
      
      window.location.href = '/view_company_details'; 
    });
  }
  
