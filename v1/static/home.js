$(document).ready(function () {
    let container = $("#featured-perfumes");

    container.empty();
    $.each(perfumes, function (id, perfume) {
        console.log("Perfume ID:", id);
        let perfumeCard = `
            <div class="col-12 col-md-6 col-lg-4 mb-4">
                <div class="card h-100 perfume-card">
                    <img class="card-img-top" src="${perfume.image}" alt="${perfume.brand}, ${perfume.name}">
                    <div class="card-body">
                        <h5 class="card-title">${perfume.brand}, <span class="perfume-name">${perfume.name}</span></h5>
                        <p><strong>Price:</strong> ${perfume.price}</p>
                        <p><strong>Notes:</strong> ${perfume.notes.join(", ")}</p>
                        <a href="/view/${id}" class="btn btn-primary">View Details</a>
                    </div>
                </div>
            </div>
        `;
        container.append(perfumeCard);
    });
});
