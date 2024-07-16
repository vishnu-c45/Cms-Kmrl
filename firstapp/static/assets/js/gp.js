

$(function () {

  //insert metrostation

  $('#submitbutton').click(function () {

    $("#gp_postform").validate({
      rules: {
        gptype: 'required',
        gpvalue: 'required',

      },
      messages: {
        gptype: 'Please enter GP type ',
        gpvalue: 'Please enter GP value ',

      },
      submitHandler: function () {
        var formdata = $('#gp_postform').serialize();
        // alert(formdata);    
        $.ajax({
          method: 'POST',
          url: '/general_parameter/post',
          datatype: 'json',
          data: formdata,

          success: function () {
            showSuccessMessage();
            // window.location='/view_spaces'

          }

        })
      }
    });

  });

})

function showSuccessMessage(message) {
  Swal.fire({
    icon: 'success',
    title: 'GP Added Successful',
    text: message,
  }).then((result) => {

    window.location.href = '/general_parameter';
  });
}

//EDIT GP

function edit_gp(ID) {
  // alert(ID)
  fetch(`/general_parameter/get/${ID}`) // Replace with your API endpoint URL
    .then((response) => response.json())
    .then((data) => {

      $('#gptype').val(data.gp_type)
      $('#gpvalue').val(data.gp_value)
      $('#edit_button').val(data.id)
    })
    .catch((error) => {
      console.error("Error:", error);
    });
  $('#edit_tax').modal('show');

  //FORM SUBMIT 
  $('#edit_gpform').submit(function (event) {
    event.preventDefault();
    // alert(ID)

    $("#edit_gpform").validate({
      rules: {
        gptype: 'required',
        gp_value: 'required',

      },
      submitHandler: function () {
        var formData = $('#edit_gpform').serialize();
        $.ajax({
          method: 'POST',
          url: 'general_parameter/edit/' + ID,
          datatype: 'json',
          data: formData,
          success: function () {
            showUpdateMessage();

          }

        })
      }
    });

  })
}

function showUpdateMessage(message) {
  Swal.fire({
    icon: 'success',
    title: 'GP Updated Successful',
    text: message,
  }).then((result) => {

    window.location.href = '/general_parameter';
  });
}


