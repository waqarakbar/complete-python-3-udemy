$(document).ready(function(){

    $(document).on('submit','#register-form', function(e){
        // console.log('form submitted')
        e.preventDefault()
        
        var form = $("#register-form").serialize();
        $.ajax({
            url: '/register-post',
            type: 'POST',
            data: form,
            success: function(data){
                window.location.href = '/login'
            }
        })
    })

    $(document).on('submit','#login-form', function(e){
        // console.log('form submitted')
        e.preventDefault()

        var form = $("#login-form").serialize();
        $.ajax({
            url: '/login-authenticate',
            type: 'POST',
            data: form,
            success: function(data){
                if(data == "error"){
                    alert("could not login")
                }else{
                    // console.log(data)
                    window.location.href = "/"
                }
            }
        })
    })

    $(document).on('click', '#logout-link', function(e){
        e.preventDefault()
        $.ajax({
            type: "GET",
            url: "/logout",
            success: function(res){
                if(res == 'success'){
                    window.location.href = "/"
                }else{
                    alert('Something went wrong')
                }
            }
        })
    })


})