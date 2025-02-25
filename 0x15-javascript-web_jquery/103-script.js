$(document).ready(function() {
    // Handle button click
    $('#btn_translate').click(fetchTranslation);
    
    // Handle Enter key in input field
    $('#language_code').keypress(function(e) {
        if (e.which === 13) { // 13 is Enter key code
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        const langCode = $('#language_code').val();
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;
        
        $.get(apiUrl)
            .done(function(data) {
                $('#hello').text(data.hello);
            })
            .fail(function() {
                $('#hello').text('Error: Translation not found');
            });
    }
});
