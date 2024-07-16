$(function(){
})

function editbank(ID){
    var BankID=ID
    
    fetch(`/view_bank/${ID}`) // Replace with your API endpoint URL
    .then((response) => response.json())
    .then((data) => {
      
      $('#bank_name').val(data[0].bank_name)
      $('#branch_name').val(data[0].branch_name)
      $('#acc_no').val(data[0].acc_no)
      $('#ifsc_code').val(data[0].ifsc_code)
      $('#upi_id').val(data[0].upi_id)
      $('#editsubmit').val(data[0].id)
    })
    .catch((error) => {
      console.error("Error:", error);
    });
    $('#edit_bank').modal('show');



}

$('#editsubmit').click(function(){
   
    var Id=$('#editsubmit').val();
    $("#editbankform").validate({
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
            var formdata=$('#editbankform').serialize();
            $.ajax({
                method:'POST',
                url:'/edit_bank/' +Id,
                datatype:'json',
                data:formdata,

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
      title: 'Bank Updated Successfully',
      text: message,
    }).then((result) => {
      
      window.location.href = '/bank_details'; 
    });
  }