$(document).ready(function () {
    $("#search-form").submit(function (event) {
        event.preventDefault();
        let query = $("#search-input").val().trim();

        if (query === "") {
            $("#search-input").val("").focus();
            return;
        }

        window.location.href = "/search?q=" + encodeURIComponent(query);
    });
});
