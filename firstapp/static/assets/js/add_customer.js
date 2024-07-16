$(function () {
    var ID =$("#submit").val();
  
    //insert contract
  
    $("#submit").click(function () {
      $("#userform").validate({
        rules: {
        city:'required',
        district:'required',
        pincode:'required',
        address:'required',
        gst_no:'required',
        pan_no:'required',
        state_code:'required',
        state:'required',
        business_type:'required',
        business_name:'required',

        },
        messages:{
          city:'Please enter your city',
          district:'Please enter your district',
          pincode:'Please enter your pincode',
          address:'Please enter your address',
          gst_no:'Please enter your gst number',
          pan_no:'Please enter your pan number',
          state_code:'Please enter your state code',
          state:'Please enter your state',
          business_type:'Please enter your business type',
          business_name:'Please enter your business name',
        },
        submitHandler: function () {
            var form = $("#userform")[0];
            var formData = new FormData(form);
            $.ajax({
              method: "POST",
              url: "/edit_customer/" +ID,
              datatype: "json",
              data: formData,
              processData: false,
              contentType: false,
    
              success:function(response){
                if(response=='true'){
                   showSuccessMessage();
                }
                else if(response='exists'){
                    Warning();
                }
            }
            });
          },
      });
    });
  });
  
  function showSuccessMessage(message) {
    Swal.fire({
      icon: 'success',
      title: 'Customer Updated Successfully',
      text: message,
    }).then((result) => {
      
      window.location.href = '/customers'; 
    });
  }

  function Warning(message) {
    Swal.fire({
      icon: 'warning',
      title: 'Username Already Exists',
      text: message,
    })
 }