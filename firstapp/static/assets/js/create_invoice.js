$(function () {



  $("#submitbutton").click(function () {
    var Total_amount=document.getElementById('totalAmount').innerHTML
    var Taxamount=document.getElementById('taxableAmount').innerHTML
    var CGST_sum=document.getElementById('cgstsum').innerHTML
    var SGST_sum=document.getElementById('sgstsum').innerHTML

    

    $("#invoiceform").validate({
      rules: {
        customername: "required",
        invoiceno: "required",
        invoicedate: "required",
        duedate: "required",
        irnno: "required",
        ackno: "required",
        ackdate: "required",
        invoicestart: "required",
        invoiceend: "required",
        sac: "required",
        taxamnt: "required",
        taxpercent: "required",
        bank: "required",
        spaces: "required",
        maintanence: "required",
      },
      submitHandler: function () {
        var formdata = $("#invoiceform").serialize();
        formdata += "&totalamount="+Total_amount+'&cgstsum='+CGST_sum+'&sgstsum='+SGST_sum+'&taxableAmount='+Taxamount
        $.ajax({
          method: "POST",
          url: "/add_invoice",
          datatype: "json",
          data: formdata,

          success: function () {
            showSuccessMessage();
          },
        });
      },
    });
  });
});

function handleOptionChange(ID) {


  const customerSelect = document.getElementById("customer-select");
  const spacesSelect = document.getElementById("spaces-select");
  fetch(`/select_masterspaces/${ID}`) // Replace with your API endpoint URL
    .then((response) => response.json())
    .then((data) => {
      
      spacesSelect.innerHTML = "<option value=''>Select Space</option>";
  
      // Populate the spaces dropdown with the retrieved options
      data.forEach((space) => {
        const option = document.createElement("option");
        option.value = space.master_space.id;
        option.textContent = space.master_space.space_name;
        spacesSelect.appendChild(option);
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function showSuccessMessage(message) {
  Swal.fire({
    icon: 'success',
    title: 'Successfully Inserted',
    text: message,
  }).then((result) => {
    
    window.location.href = '/customer_invoices'; 
  });
}
