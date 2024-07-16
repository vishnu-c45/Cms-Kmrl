$('#submitbutton').click(function(){
    // var Id=$('#submit').val();
    $("#grievanceform").validate({
        rules:{
            space:'required',
            reason:'required',
            complaintdetails:'required',
           
        },
        messages:{
            space: 'Please select your space',
            reason: 'Please select your reason ',
            complaintdetails: 'Please enter the details',
    
          },
        submitHandler: function(){
            // var formdata=$('#companyform').serialize();
            var form = $('#grievanceform')[0];
            var formData = new FormData(form);
            $.ajax({
                method:'POST',
                url:'/add_grievance',
                datatype:'json',
                data: formData,
                processData: false,
                contentType: false,
                    

                success:function(){
                    showSuccMessage();

                }
            
            })
        }
    });

});

function showSuccMessage(message) {
    Swal.fire({
      icon: 'success',
      title: 'Grievance Sent Succesfully ',
      text: message,
    }).then((result) => {
      
      window.location.href = '/grievances'; 
    });
  }
  