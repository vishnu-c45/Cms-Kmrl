$().ready(function () {

  $("#submit").click(function () {
    $("#passform").validate({
      rules: {
        current_password: "required",

        new_password: {
          required: true,
          minlength: 8,
        },
        confirm_password: {
          required: true,
          equalTo: "#password",
        },
      },
      messages:{
        new_password: 'Please enter your new password',
        current_password: 'Please enter your current password',
        confirm_password: {
          required: 'Please enter confirmation password',
          equalTo: 'Please make sure your passwords match'
        }

      },
      submitHandler: function () {
        var formdata = $("#passform").serialize();
        $.ajax({
          method: "POST",
          url: "/change_password",
          datatype: "json",
          data: formdata,

          success: function (reponse) {
            if (reponse == "true") {
              showSuccessMessage();
            }else {
              Incorrect();
            }
          },
        });
      },
    });
  });
});


function showSuccessMessage(message) {
  Swal.fire({
    icon: 'success',
    title: 'Password Changed Successfully',
    text: message,
  }).then((result) => {
    
    window.location.href = '/logout'; 
  });
}

function Incorrect(message) {
  Swal.fire({
    icon: 'error',
    title: 'Current Password Does Not Match',
    text: message,
  })
}
