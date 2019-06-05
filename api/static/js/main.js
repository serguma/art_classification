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

                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#datos').fadeIn(800);
                $('#result').text(' Es:  ' + data[0]);
                $('#datos').html('Artista: ' + info['artistName']
                                + '<br/>Título: ' + info['title']
                                + '<br/>Año:' + info['year']
                                + '<br/>Estilo:<span>' + info['estilo'] +'</span>' )
                console.log(data[0])
                console.log(jQuery.parseJSON(data[1]))
                console.log('Success!');
            },
        });
    });

});