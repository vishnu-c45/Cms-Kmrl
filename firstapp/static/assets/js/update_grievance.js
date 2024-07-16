
function editgrievance(ID){

    
    fetch(`/view_grievance/${ID}`) // Replace with your API endpoint URL
    .then((response) => response.json())
    .then((data) => {
      
      $('#space').val(data[0].master_space.id)
      $('#reason').val(data[0].reason)
      $('#complaintdetails').val(data[0].complaint)
      $('#editsubmit').val(data[0].id)
    })
    .catch((error) => {
      console.error("Error:", error);
    });
    $('#editgrievance').modal('show');



}


$('#editsubmit').click(function(){
    var Id=$('#editsubmit').val();

    $("#editgrievanceform").validate({
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
            var form = $('#editgrievanceform')[0];
            var formData = new FormData(form);
            $.ajax({
                method:'POST',
                url:'/edit_grievance/'+Id
                ,
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
      title: 'Grievance Updated Successfully',
      text: message,
    }).then((result) => {
      
      window.location.href = '/grievances'; 
    });
  }