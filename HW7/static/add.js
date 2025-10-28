$(document).ready(function () {
    $("#add-form").on("submit", function (event) {
        event.preventDefault();

        $(".error-message").text("");
        $("#success-message").addClass("d-none").text("");


        let perfumeData = {
            brand: $("#brand").val().trim(),
            name: $("#name").val().trim(),
            image: $("#image").val().trim(),
            year: $("#year").val().trim(),
            summary: $("#summary").val().trim(),
            price: $("#price").val().trim(),
            notes: $("#notes").val().trim().split(",").map(note => note.trim())
        };

        let isValid = true;
        if (!perfumeData.brand) {
            $("#brand-error").text("Brand name is required.");
            isValid = false;
        }

        if (!perfumeData.name) {
            $("#name-error").text("Perfume name is required.");
            isValid = false;
        }

        if (!perfumeData.notes[0]) {
            $("#notes-error").text("At least one note is required.");
            isValid = false;
        }

        if (!perfumeData.summary) {
            $("#summary-error").text("Summary is required.");
            isValid = false;
        }

        if (!perfumeData.image) {
            $("#image-error").text("Image URL is required.");
            isValid = false;
        }

        if (!isValid) {
            return;
        }

        $.ajax({
            type: "POST",
            url: "/add",
            contentType: "application/json",
            data: JSON.stringify(perfumeData),
            success: function (response) {
                $("#success-message").removeClass("d-none").text(response.message);
                $("#options").removeClass("d-none");
                $("#view-item-link").attr("href", "/view/" + response.id);

                $("#add-form")[0].reset();
                $("#brand").focus();
            },
            error: function (xhr) {
                let responseText = xhr.responseText;  // Capture response text
                try {
                    let response = JSON.parse(responseText);
                    if (response.errors) {
                        for (let field in response.errors) {
                            $("#" + field + "-error").text(response.errors[field]);
                        }
                    } else {
                        alert("An unexpected error occurred: " + response.error);
                    }
                } catch (e) {
                    console.error("Error parsing response:", responseText);
                    alert("Server error: Could not parse response. Check console logs.");
                }
            }
        });
    });

    $("#add-another").on("click", function () {
        $("#options").addClass("d-none");
        $("#success-message").addClass("d-none");
        $("#add-perfume-form")[0].reset();
        $("#brand").focus();
    });
});
