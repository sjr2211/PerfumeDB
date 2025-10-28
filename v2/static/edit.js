$(document).ready(function () {
    $("#edit-form").submit(function (event) {
        event.preventDefault();
        $(".error-message").remove();

        let isValid = true;

        let perfumeId = window.location.pathname.split("/").pop(); // Extract ID from URL

        let formData = {
            brand: $("#brand").val().trim(),
            name: $("#name").val().trim(),
            price: $("#price").val().trim(),
            year: $("#year").val().trim(),
            notes: $("#notes").val().split(',').map(n => n.trim()).filter(n => n), 
            summary: $("#summary").val().trim()
        };




        $.ajax({
            url: "/edit/" + perfumeId,
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(formData),
            success: function (response) {
                window.location.href = "/view/" + perfumeId;
            },
            error: function () {
                alert("Failed to update perfume.");
            }
        });
    });

    $("#discard-msg").dialog({
        autoOpen: false,
        modal: true,
        resizable: false,
        width: 400,
        classes: {
            "ui-dialog": "custom-dialog",
            "ui-dialog-titlebar-close": "btn-close"
        },
        buttons: [
            {
                text: "Discard",
                class: "btn btn-discard",
                click: function () {
                    let perfumeId = window.location.pathname.split("/").pop();
                    window.location.href = "/view/" + perfumeId;
                }
            },
            {
                text: "Keep Editing",
                class: "btn btn-secondary",
                click: function () {
                    $(this).dialog("close");
                }
            }
        ],
        closeText: ""
    });

    $("#discard-btn").click(function () {
        $("#discard-msg").dialog("open");
    });

    $("#discard-btn").click(function () {
        $("#discard-msg").removeClass("d-none");
    });

});
