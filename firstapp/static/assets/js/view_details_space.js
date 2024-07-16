var ID = document.getElementById("data-json").value;
var body = document.getElementById("cardbody");

// Contract details....... api..................

function create_table() {
  document.getElementById("customergrid").classList.remove("gridcolor");
  document.getElementById("invoicegrid").classList.remove("gridcolor");
  document.getElementById("paymentgrid").classList.remove("gridcolor");
  document.getElementById("contractgrid").classList.add("gridcolor");
  var ID = document.getElementById("data-json").value;
  body.innerHTML = "";
  body.innerHTML =
    '<div class="table-responsive"> <table class="table table-stripped table-hover datatable" id="datatable1"> <thead class="thead-light"> <tr> <th>Sl No</th> <th>Contract Number</th> <th>Customer Name</th> <th>Agreement date</th> <th>Contract Period</th> <th>Invoice Date</th> <th>Status</th> <th>Actions</th> </tr> </thead> <tbody id="tbody">  </tbody> </table> </div>';

  var tbody = document.getElementById("tbody");
  $.ajax({
    method: "GET",
    url: "/space_details_contract/" + ID,
    datatype: "json",

    success: function (response) {
      var data = "";
      for (i = 0; i < response.length; i++) {
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
          '<h2 class="table-avatar">' +
          '<div class="avatar avatar-md me-2">' +
          '<img class="avatar-img rounded-circle" src="/static/assets/img/profiles/avatar-07.jpg" alt="User Image">' +
          "</div>" +
          response[i].customer_contact.customer.customer_name +
          "</h2>" +
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
            '<span class="badge bg-green-light text-success">Active</span>';
        } else {
          html +=
            '<span class="badge bg-danger-light text-danger">Inactive</span>';
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

create_table();

// customer details -Api

function customer_details(Id) {
  document.getElementById("contractgrid").classList.remove("gridcolor");
  document.getElementById("invoicegrid").classList.remove("gridcolor");
  document.getElementById("paymentgrid").classList.remove("gridcolor");
  document.getElementById("customergrid").classList.add("gridcolor");

  body.innerHTML = "";
  body.innerHTML =
    '<div class="table-responsive"> <table class="table table-stripped table-hover datatable "> <thead class="thead-light"> <tr> <th>Sl No</th> <th>Name</th> <th>Phone</th> <th>Business Name</th> <th>Business Type</th> <th>Status</th> <th>Actions</th> </tr> </thead> <tbody id="tbody">  </tbody> </table> </div>';

  var tbody = document.getElementById("tbody");
  $.ajax({
    method: "GET",
    url: "/space_details_contract/" + ID,
    datatype: "json",

    success: function (response) {
      var data = "";
      for (i = 0; i < response.length; i++) {
        var count = i + 1;
        var html =
          "<tr>" +
          "<td>" +
          count +
          "</td>" +
          "<td>" +
          '<h2 class="table-avatar">' +
          '<p class="avatar avatar-md me-2">' +
          '<img class="avatar-img rounded-circle" src="/static/assets/img/profiles/avatar-07.jpg" alt="User Image">' +
          "</p>" +
          response[i].customer_contact.customer.customer_name +
          "</h2>" +
          "</td>" +
          "<td>" +
          response[i].customer_contact.phone_number +
          "</td>" +
          "<td>" +
          response[i].customer_contact.customer.business_name +
          "</td>" +
          "<td>" +
          response[i].customer_contact.customer.business_type +
          "</td>" +
          "<td>";

        if (response[i].status == 1) {
          html +=
            '<span class="badge bg-green-light text-success">Active</span>';
        } else {
          html +=
            '<span class="badge bg-danger-light text-danger">Inactive</span>';
        }

        html +=
          "</td>" +
          "<td>" +
          '<a href="/customer_details/' +
          response[i].customer_contact.id +
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

//invoice api
function invoice_details(Id) {
  document.getElementById("contractgrid").classList.remove("gridcolor");
  document.getElementById("customergrid").classList.remove("gridcolor");
  document.getElementById("invoicegrid").classList.add("gridcolor");
  document.getElementById("paymentgrid").classList.remove("gridcolor");

  body.innerHTML = "";
  body.innerHTML =
    '<div class="table-responsive"> <table class="table table-stripped table-hover datatable" id="datatable1"> <thead class="thead-light"> <tr> <th>Sl No</th> <th>Invoice Number</th> <th>Customer</th> <th>Total Amount</th>  <th>Invoice Start date</th><th>Due date</th> <th>Status</th> <th>Actions</th> </tr> </thead> <tbody id="tbody">  </tbody> </table> </div>';

  fetch("/space_details_customer/" + ID)
    .then((response) => response.json())
    .then((data) => {
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
          '<h2 class="table-avatar">' +
          '<div class="avatar avatar-md me-2">' +
          '<img class="avatar-img rounded-circle" src="/static/assets/img/profiles/avatar-07.jpg" alt="User Image">' +
          "</div>" +
          reponse.customer_contact.customer.customer_name +
          "</h2>" +
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

function Payment_details(Id) {
  document.getElementById("contractgrid").classList.remove("gridcolor");
  document.getElementById("customergrid").classList.remove("gridcolor");
  document.getElementById("invoicegrid").classList.remove("gridcolor");
  document.getElementById("paymentgrid").classList.add("gridcolor");

  body.innerHTML = "";
  body.innerHTML =
    '<div class="table-responsive"> <table class="table table-stripped table-hover datatable" id="datatable1"> <thead class="thead-light"> <tr> <th>Sl No</th> <th>Customer</th> <th>Transaction Id</th> <th> Amount</th>   <th>Date</th> <th>Status</th> </tr> </thead> <tbody id="tbody">  </tbody> </table> </div>';

  fetch("/space_details_payments/" + ID)
    .then((response) => response.json())
    .then((data) => {
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
          '<h2 class="table-avatar">' +
          '<div class="avatar avatar-md me-2">' +
          '<img class="avatar-img rounded-circle" src="/static/assets/img/profiles/avatar-07.jpg" alt="User Image">' +
          "</div>" +
          reponse.customer.customer.customer_name +
          "</h2>" +
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
