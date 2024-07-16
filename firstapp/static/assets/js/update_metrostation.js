$().ready(function() {

    $('#submitbutton').click(function(){
        var Id=$('#submitbutton').val();
        
        $("#metrostationform").validate({
            rules:{
                stationname:'required',
                s_name: 'required',
                start_time:'required',
                end_time:'required',
                city:'required',
                district:'required',
                pincode:'required',
                email:'required',
                phone:'required',
            },
            messages:{
                stationname:'Please enter station name',
                s_name: 'Please enter short name',
                start_time:'Please enter the start time',
                end_time:'Please enter the end time',
                city:'Please enter the city',
                district:'Please enter the district',
                pincode:'Please enter pincode',
                email:'Please enter email',
                phone:'Please enter phone number',
            },
            submitHandler: function(){
                var formdata=$('#metrostationform').serialize();
                $.ajax({
                    method:'POST',
                    url:'/Update_metrostation/'+Id,
                    datatype:'json',
                    data:formdata,

                    success:function(){
                        showSuccessMessage();
                        // window.location='/metrostaion'

                    }
                
                })
            }
        });

    });
 
});

function showSuccessMessage(message) {
    Swal.fire({
      icon: 'success',
      title: 'Metrostation Updated Successfully',
      text: message,
    }).then((result) => {
      
      window.location.href = '/metrostaion'; 
    });
  }
