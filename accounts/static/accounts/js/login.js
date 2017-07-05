$(document).ready(function() {

    $("#my_form").submit(function(event) {
        event.preventDefault(); //prevent default action
        var post_url = $(this).attr("action"); //get form action url
        var request_method = $(this).attr("method"); //get form GET/POST method
        var form_data = $(this).serialize(); //Encode form elements for submission

        $.ajax({
            url: post_url,
            type: request_method,
            data: form_data,
            success: function(data) {
                console.log(data.message);
                var x = data.message
                if (x === "Invalid credentials") {
                    $(".alert").text("Invalid credentials");
                    $(".alert").removeAttr("hidden");

                }
                if (x === "Account disabled") {
                    $(".alert").text("Your account has been disabled");
                    $(".alert").removeAttr("hidden");
                }
                 if (x === "Login successful") {
                    window.location = "/welcome/";
                }

            },
            error: function(xhr, errmsg, err) {
                console.log('xhr -> ', xhr);
                console.log('errmsg -> ', errmsg);
                console.log('err -> ', err.url);


            }


        });


    });

});
