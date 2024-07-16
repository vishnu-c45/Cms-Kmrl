$(function () {
  
    $("#submit").click(function () {
      $("#userform").validate({
        rules: {
          name: "required",
          phone: "required",
          email: "required",
        },
        messages:{
          name: "Please enter your name",
          phone: "Please enter your phone number",
          email: "Please enter your email",
        },
        submitHandler: function () {
            var form = $("#userform")[0];
            var formData = new FormData(form);
            $.ajax({
              method: "POST",
              url: "/profile_settings",
              datatype: "json",
              data: formData,
              processData: false,
              contentType: false,
    
              success:function(){
                showSuccessMessage();

            },
            });
          },
      });
    });
  });
  
  function showSuccessMessage(message) {
    Swal.fire({
      icon: 'success',
      title: 'User Updated Successfully',
      text: message,
    }).then((result) => {
      
      window.location.href = '/profile_settings'; 
    });
  }