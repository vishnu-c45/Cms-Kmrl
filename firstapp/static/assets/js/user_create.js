$().ready(function () {
  $("#submitbutton").click(function (event) {
    // event.preventDefault();
    $("#usercreateform").validate({
      rules: {
        usertype: "required",
        loginname: "required",
        username: "required",
        password: {
          required: true,
          minlength: 8,
        },
        confirm_password: {
          required: true,
          equalTo: "#password",
        },
      },
      messages: {
        usertype: "Please select the role",
        loginname: "Please enter the name",
        username: "Please enter username",
        password: "Please enter the password",
        confirm_password: {
          required: "Please enter confirmation password",
          equalTo: "Please make sure passwords match",
        },
      },
      submitHandler: function () {
        var formdata = $("#usercreateform").serialize();
        //alert(formdata);
        $.ajax({
          method: "POST",
          url: "/user_create",
          datatype: "json",
          data: formdata,

          success: function (response) {
            if (response == "true") {
              showSuccessMessage();
            } else if ((response = "exists")) {
              Warning();
            }
          },
        });
      },
    });
  });
});

function showSuccessMessage(message) {
  Swal.fire({
    icon: "success",
    title: "User Created Successfully ",
    text: message,
  }).then((result) => {
    window.location.href = "/manage_users";
  });
}

function Warning(message) {
  Swal.fire({
    icon: "warning",
    title: "Username Already Exists",
    text: message,
  });
}
