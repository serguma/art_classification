$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    // Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').attr('src', e.target.result);
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        $('#datos').text('');
        $('#datos').hide();        
        readURL(this);
    });

    // Predice
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        
        $(this).hide();
        $('.loader').show();
        
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                
                info = jQuery.parseJSON(data[1]);
                    
                if(info['estilo'] == data[0]){
                    $('#result').addClass('c-si')
                    $('#result').removeClass('c-no')
                }else{
                    $('#result').removeClass('c-si')
                    $('#result').addClass('c-no')
                }

                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#datos').fadeIn(800);
                $('#result').text('Estilo: ' + data[0]);
                $('#datos').html('Datos de la obra: <br/><span>Artista:</span> ' + info['artistName']
                                + '<br/><span>Título:</span> ' + info['title']
                                + '<br/><span>Año:</span> ' + info['year']
                                + '<br/><span>Estilo:</span> ' + info['estilo'] )
                console.log(data[0])
                console.log(jQuery.parseJSON(data[1]))
                console.log('Success!');
            },
        });
    });

});