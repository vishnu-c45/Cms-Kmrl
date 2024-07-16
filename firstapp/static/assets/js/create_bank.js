$(function(){

    //insert contract

    $('#submitbutton').click(function(){
        $("#bankform").validate({
            rules:{
                bank_name:'required',
                branch_name:'required',
                upi_id:'required',
                acc_no: 'required',
                ifsc_code: 'required',
               
            },
            messages:{
                bank_name:'Please enter your bank name',
                branch_name:'Please enter your branch name',
                upi_id:'Please enter your UPI id',
                acc_no: 'Please enter your account number',
                ifsc_code: 'Please enter your IFSC code',
               
            },
            submitHandler: function(){
                var formdata=$('#bankform').serialize();
                $.ajax({
                    method:'POST',
                    url:'/add_bank',
                    datatype:'json',
                    data:formdata,

                    success:function(){
                        showSuccMessage();
                    }
                
                })
            }
        });

    });

})

function showSuccMessage(message) {
    Swal.fire({
      icon: 'success',
      title: 'Bank Added Successfully ',
      text: message,
    }).then((result) => {
      
      window.location.href = '/bank_details'; 
    });
  }