$().ready(function() {

    $('#submitbutton').click(function(){
        var Id=$('#submitbutton').val();
        
        $("#spaceform").validate({
            rules:{
                stationname:'required',
                spacename:'required',
                spacetype:'required',
                areatype:'required',
                areaside:'required',
                arealevel:'required',
                area:'required',
            },
            messages:{
                stationname:'Please select station',
                spacename:'Please enter space name',
                spacetype:'Please select space type',
                areatype:'Please select area type',
                areaside:'Please select area side',
                arealevel:'Please select area level',
                area:'Please enter area ',
           },
            submitHandler: function(){
                var formdata=$('#spaceform').serialize();
                $.ajax({
                    method:'POST',
                    url:'/update_space/'+Id,
                    datatype:'json',
                    data:formdata,

                    success:function(){
                        showSuccessMessage();
                        // window.location='/view_spaces'

                    }
                
                })
            }
        });

    });

    
});

function showSuccessMessage(message) {
    Swal.fire({
      icon: 'success',
      title: 'Space Updated Successfully',
      text: message,
    }).then((result) => {
      
      window.location.href = '/view_spaces'; 
    });
  }

