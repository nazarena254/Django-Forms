$(document).ready(function(){
    $('form').submit(function(event){
        event.preventDefault()
        form = $('form')

        $.ajax({
            'url':'/ajax/newsletter/',
            'type':'POST',
            'data':form.serialize(),
            'dataType':'json',
            'success': function(data){
              alert(data['success'])
            },
          })// END of Ajax method
          // used to get values for user details
          $('#id_your_name').val('')
          $('#id_your_lastname').val('')
          $("#id_email").val('')

    }) // End of submit event

}) // End of document ready function
