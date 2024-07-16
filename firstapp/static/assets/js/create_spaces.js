$(function () {

  //insert metrostation

  $("#submitbutton").click(function () {
    $("#spaceform").validate({
      rules: {
        stationname: "required",
        spacename: "required",
        spacetype: "required",
        areatype: "required",
        areaside: "required",
        arealevel: "required",
        area: "required",
      },
      messages: {
        stationname: "Please select station",
        spacename: "Please enter space name",
        spacetype: "Please select space type",
        areatype: "Please select area type",
        areaside: "Please select area side",
        arealevel: "Please select area level",
        area: "Please enter area ",
      },
      submitHandler: function () {
        var formdata = $("#spaceform").serialize();
        $.ajax({
          method: "POST",
          url: "/add_spaces",
          datatype: "json",
          data: formdata,

          success: function () {
            showSuccessMessage();
            // window.location='/view_spaces'
          },
        });
      },
    });
  });
});
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function showSuccessMessage(message) {
  Swal.fire({
    icon: "success",
    title: "Space Added Successfully",
    text: message,
  }).then(function (result) {
    if (result.isConfirmed) {

      // Send email to the registered customer
      const csrftoken = getCookie("csrftoken");

      $.ajax({
        method: "POST",
        url: "/send-email",
        dataType: "json",
        data: {
          email: $('#spaceform input[name="spacename"]').val(),
          Area: $('#spaceform input[name="area"]').val(),
          station: $('#spaceform select[name="stationname"] option:selected').text(),

          type: 2,
        },
        beforeSend: function (xhr) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function () {
          // Handle the response from the email sending process if needed
        },
      });

      // Redirect to the desired page
      window.location.href = "/view_spaces";
    }
  });
}