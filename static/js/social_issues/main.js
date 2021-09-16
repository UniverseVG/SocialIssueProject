$(document).ready(function() {

    // click event for lement with like-icon class

    function getCookie(name) {
        var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g,
            '\\$1') + "=([^;]*)"));
        return matches ? decodeURIComponent(matches[1]) : undefined;
    }
    const csrftoken = getCookie("csrftoken")

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        // xhrFields: { withCredentials:true }
        // crossdomain: true,
    });


    $(".like-icon").click(function(e) {
        const el = $(e.currentTarget)
        issue_id = el.data("id")
        mydata = {
            "issue_id": issue_id
        }
        $.post({
            url: "/api/like",
            data: mydata,
            success: function(data, textStatus, jqXHR) {
                if (textStatus === "success") {
                    const count = $(el).find(".like_count")
                        // parseint for conversion  "0" == > 0
                    let incCounter = parseInt(count.text())
                    incCounter = incCounter + 1
                    count.text(incCounter)
                }
            },
            error: function(err) {
                let error = JSON.parse(err.responseText)
                if (error.hasOwnProperty("message")) {
                    const count = $(el).find(".like_count")
                    count.html(`<span class="text-danger" >` + error["message"] + ` </span>`)
                }

            },
        });

    });

});