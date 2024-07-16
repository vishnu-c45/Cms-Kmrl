$("#submitbutton").click(function () {
  $("#powerform").validate({
    rules: {
      station: "required",
      power: "required",
      photo: "required",
    },
    messages: {
      station: "Please select your station",
      power: "Please enter the meter reading ",
      photo: "Please upload the meter photo",
    },
    submitHandler: function () {
      document.getElementById("submitbutton").disabled = true;
      var form = $("#powerform")[0];
      var formData = new FormData(form);
      $.ajax({
        method: "POST",
        url: "/add_power",
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
    title: "Electricity added succesfully ",
    text: message,
  }).then((result) => {
    window.location.href = "/power";
  });
}
