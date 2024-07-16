var ID = document.getElementById("data-json").value;
var tablebody = document.getElementById("tablebody");

// var $j = jQuery.noConflict();

// var dataTable = $('#datatable1').DataTable();

var $j = jQuery.noConflict();
$j(document).ready(function () {
  document.getElementById("contract_body").classList.add("contract-body");

  tablebody.innerHTML = "";
  tablebody.innerHTML =
    '<div class="table-responsive"> <table class="table table-stripped table-hover" id="datatable1"> <thead class="thead-light"> <tr> <th>Sl No</th> <th>Contract Number</th>  <th>Agreement date</th> <th>Contract Period</th> <th>Invoice Date</th> <th>Status</th> <th>Actions</th> </tr> </thead> <tbody id="tbody">  </tbody> </table> </div>';

  $.ajax({
    method: "GET",
    url: "/Customer_detais_contract/" + ID,
    datatype: "json",

    success: function (response) {
      var tbody = document.getElementById("tbody");
      for (var i = 0; i < response.length; i++) {
        var count = i + 1;
        var html =
          "<tr>" +
          "<td>" +
          count +
          "</td>" +
          "<td>" +
          response[i].contract_no +
          "</td>" +
          "<td>" +
          response[i].agreement_date +
          "</td>" +
          "<td>" +
          response[i].contract_period +
          "yr" +
          "</td>" +
          "<td>" +
          response[i].invoice_start_date +
          "</td>" +
          "<td>";

        if (response[i].status == 1) {
          html +=
            '<span class="badge badge-pill bg-green-light text-success">Active</span>';
        } else {
          html +=
            '<span class="badge badge-pill bg-danger-light text-danger">Inactive</span>';
        }

        html +=
          "</td>" +
          "<td>" +
          '<a href="/contract_details/' +
          response[i].id +
          '" class="btn btn-greys me-2">' +
          '<i class="fa fa-plus-circle me-1"></i> Details' +
          "</a>" +
          "</td>" +
          "</tr>";

        tbody.innerHTML += html;
      }
    },
  });
});

//fetch contract details
function contract_data() {
  document.getElementById("contract_body").classList.add("contract-body");
  document.getElementById("invoice_body").classList.remove("invoice-body");
  document.getElementById("payment_body").classList.remove("payment-body");

  if ($.fn.DataTable.isDataTable("#datatable1")) {
    $("#datatable1").DataTable().destroy();
  }
  tablebody.innerHTML = "";
  tablebody.innerHTML =
    '<div class="table-responsive"> <table class="table table-stripped table-hover datatable" id="datatable1"> <thead class="thead-light"> <tr> <th>Sl No</th> <th>Contract Number</th>  <th>Agreement date</th> <th>Contract Period</th> <th>Invoice Date</th> <th>Status</th> <th>Actions</th> </tr> </thead> <tbody id="tbody">  </tbody> </table> </div>';

  $.ajax({
    method: "GET",
    url: "/Customer_detais_contract/" + ID,
    datatype: "json",

    success: function (response) {
      var tbody = document.getElementById("tbody");
      for (var i = 0; i < response.length; i++) {
        var count = i + 1;
        var html =
          "<tr>" +
          "<td>" +
          count +
          "</td>" +
          "<td>" +
          response[i].contract_no +
          "</td>" +
          "<td>" +
          response[i].agreement_date +
          "</td>" +
          "<td>" +
          response[i].contract_period +
          "yr" +
          "</td>" +
          "<td>" +
          response[i].invoice_start_date +
          "</td>" +
          "<td>";

        if (response[i].status == 1) {
          html +=
            '<span class="badge badge-pill bg-green-light text-success">Active</span>';
        } else {
          html +=
            '<span class="badge badge-pill bg-danger-light text-danger">Inactive</span>';
        }

        html +=
          "</td>" +
          "<td>" +
          '<a href="/contract_details/' +
          response[i].id +
          '" class="btn btn-greys me-2">' +
          '<i class="fa fa-plus-circle me-1"></i> Details' +
          "</a>" +
          "</td>" +
          "</tr>";

        tbody.innerHTML += html;
      }
    },
  });
}

//fetch invoice details
function invoice_data() {
  document.getElementById("contract_body").classList.remove("contract-body");
  document.getElementById("payment_body").classList.remove("payment-body");
  document.getElementById("invoice_body").classList.add("invoice-body");
  tablebody.innerHTML = "";
  tablebody.innerHTML =
    '<div class="table-responsive"> <table class="table table-stripped table-hover datatable" id="datatable1"> <thead class="thead-light"> <tr> <th>Sl No</th> <th>Invoice Number</th> <th>Master Space</th> <th>Total Amount</th>  <th>Invoice Start date</th><th>Due date</th> <th>Status</th> <th>Actions</th> </tr> </thead> <tbody id="tbody">  </tbody> </table> </div>';

  fetch("/Customer_details_invoice/" + ID)
    .then((response) => response.json())
    .then((data) => {
      var tbody = document.getElementById("tbody");
      var count = 0;
      data.forEach((reponse) => {
        count++;
        var html =
          "<tr>" +
          "<td>" +
          count +
          "</td>" +
          "<td>" +
          reponse.invoice_no +
          "</td>" +
          "<td>" +
          reponse.master_space.space_name +
          "</td>" +
          "<td>" +
          reponse.total_amount +
          "</td>" +
          "<td>" +
          reponse.invoice_start_date +
          "</td>" +
          "<td>" +
          reponse.due_date +
          "</td>" +
          "<td>";

        if (reponse.status == 1) {
          html += '<span class="badge bg-light-gray text-primary">Draft</span>';
        } else if (reponse.status == 2) {
          html +=
            '<span class="badge bg-warning-light text-warning">Pending</span>';
        } else if (reponse.status == 3) {
          html += '<span class="badge bg-green-light text-success">Paid</span>';
        } else if (reponse.status == 4) {
          html +=
            '<span class="badge bg-danger-light text-danger">Overdue</span>';
        } else if (reponse.status == 5) {
          html +=
            '<span class="badge bg-light-gray text-gray-light">Cancelled</span>';
        }

        html +=
          "</td>" +
          "<td>" +
          '<a target="_blank" href="/invoice_details/' +
          reponse.id +
          '" class="btn btn-greys me-2">' +
          '<i class="fa fa-plus-circle me-1"></i> Details' +
          "</a>" +
          "</td>" +
          "</tr>";

        tbody.innerHTML += html;
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function Payment_data() {
  document.getElementById("contract_body").classList.remove("contract-body");
  document.getElementById("invoice_body").classList.remove("invoice-body");
  document.getElementById("payment_body").classList.add("payment-body");

  tablebody.innerHTML = "";
  tablebody.innerHTML =
    '<div class="table-responsive"> <table class="table table-stripped table-hover datatable" id="datatable1"> <thead class="thead-light"> <tr> <th>Sl No</th> <th>Payment ID</th> <th> Amount</th>  <th> Date</th> <th>Status</th> </tr> </thead> <tbody id="tbody">  </tbody> </table> </div>';

  fetch("/Customer_details_payment/" + ID)
    .then((response) => response.json())
    .then((data) => {
      var tbody = document.getElementById("tbody");
      var count = 0;
      data.forEach((reponse) => {
        count++;
        const isoDate = reponse.created_on;
        const dateObj = new Date(isoDate);
        const PaymentDate = dateObj.toISOString().split("T")[0];

        var html =
          "<tr>" +
          "<td>" +
          count +
          "</td>" +
          "<td>" +
          reponse.transaction_id +
          "</td>" +
          "<td>" +
          reponse.payment_amount +
          "</td>" +
          "<td>" +
          PaymentDate +
          "</td>" +
          "<td>";

        if (reponse.status == 1) {
          html +=
            '<span class="badge bg-success-light text-success-light">Paid</span>';
        } else if (reponse.status == 3) {
          html +=
            '<span class="badge bg-danger-light text-danger-light">Declined</span>';
        } else {
          html +=
            '<span class="badge bg-warning-light text-warning-light">Pending</span>';
        }
        tbody.innerHTML += html;
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
