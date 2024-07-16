$().ready(function() {

    $('#submitbutton').click(function(){
        var Id=$('#submitbutton').val();
        
        $("#contractform").validate({
            rules:{
                contractno:'required',
                customername:'required',
                masterspace:'required',
                agreementno: 'required',
                agreementdate: 'required',
                auctionno:'required',
                auctiondate: 'required',
                auctionnoticeno: 'required',
                auctionnoticenodate: 'required',
                finalallotmentorderno: 'required',
                finalallotmentordernodate: 'required',
                auctionnoticerefno:'required',
                auctionnoticerefnodate: 'required',
                fitment: 'required',
                lockin: 'required',
                contract_period: 'required',
                rfp_number:'required',
                rfp_date:'required',
                rfp_ref_number:'required',
                rfp_ref_date: 'required',
                loa_number: 'required',
                loa_date:'required',
                invoice_start_date: 'required',
                job_card_issue: 'required',
                tenure_start_date: 'required',
                tenure_end_date: 'required',
                bill_start_date: 'required',
                rent_amount:'required',
                utility_charges: 'required',
                cam_charges: 'required',
                security_deposit: 'required',
                hikes: 'required',
                auth_sign: 'required',
                desiginations: 'required',
                sq_ft_rate: 'required',
            },
            submitHandler: function(){
                // var formdata=$('#contractform').serialize();
                var form = $('#contractform')[0];
                var formData = new FormData(form);
                $.ajax({
                    method:'POST',
                    url:'/update_contracts/'+Id,
                    datatype:'json',
                    data: formData,
                    processData: false,
                    contentType: false,
                    success:function(){
                        showSuccessMessage();

                    }
                
                })
            }
        });

    });

    
});

function showSuccessMessage(message) {
    Swal.fire({
      icon: 'success',
      title: 'Contract Updated Successfully',
      text: message,
    }).then((result) => {
      window.location.href = '/view_contracts'; 
    });
  }

