$("#reply").click(function () {

  var Id = $("#replybutton").val();

  $("#replyform").validate({
    rules: {
      reply: "required",
    },
    submitHandler: function () {
      var formdata = $("#replyform").serialize();

      $.ajax({
        method: "POST",
        url: "/reply/" + Id,
        datatype: "json",
        data: formdata,
        success: function () {
          showSuccessMessage();
          
        },
      });
    },
  });
});

function showSuccessMessage(message) {
  var Id = $("#replybutton").val();
  Swal.fire({
    icon: 'success',
    title: 'Reply Sent',
    text: message,
  }).then((result) => {
    
    window.location.href = "/customer_grievance_form/"+Id;
  });
}