$(document).ready(function () {
    let container = $("#featured-perfumes");

    container.empty();
    $.each(perfumes, function (id, perfume) {
        console.log("Perfume ID:", id);
        let perfumeCard = `
            <div class="col-12 col-md-6 col-lg-4 mb-4">
                <div class="card h-100 perfume-card" data-url="/view/${id}">
                    <div class="row card-head">
                        <h5 class="card-title">${perfume.brand}, <span class="perfume-name">${perfume.name}</span></h5>
                        <p class="price">${perfume.price}</p>
                    </div>
                    <div class="card-body">
                        <img class="card-img-top" src="${perfume.image}" alt="${perfume.brand}, ${perfume.name}">
                        <br>
                        <p class="notes"><strong>Notes:</strong> ${perfume.notes.join(", ")}</p>
                    </div>
                </div>
            </div>
        `;
        container.append(perfumeCard);
    });
    $(document).on("click", ".perfume-card", function () {
        window.location.href = $(this).data("url");
    });
});
