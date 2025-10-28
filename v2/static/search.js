$(document).ready(function () {
    $("#search-form").submit(function (event) {
        event.preventDefault();
        let query = $("#search-input").val().trim();

        console.log("Search query:", query);

        if (query === "") {
            $("#search-input").val("").focus();
            return;
        }

        window.location.href = "/search?q=" + encodeURIComponent(query);
    });

    $(document).on("click", ".perfume-card", function () {
        window.location.href = $(this).data("url");
    });
});
