$("#submitbutton").click(function () {
  $("#waterform").validate({
    rules: {
      station: "required",
      photo: "required",
      water: "required",
    },
    messages: {
      station: "Please select your station",
      water: "Please enter the meter reading ",
      photo: "Please upload the meter photo",
    },
    submitHandler: function () {
      document.getElementById("submitbutton").disabled = true;
      var form = $("#waterform")[0];
      var formData = new FormData(form);
      $.ajax({
        method: "POST",
        url: "/add_water",
        datatype: "json",
        data: formData,
        processData: false,
        contentType: false,
        success: function () {
          showSuccMessage();
        },
      });
    },
  });
});

function showSuccMessage(message) {
  Swal.fire({
    icon: "success",
    title: "Water added succesfully ",
    text: message,
  }).then((result) => {
    window.location.href = "/water";
  });
}
