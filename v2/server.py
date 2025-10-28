# Sarah Rivera sjr2211 UI HW6

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Sample dataset
dataset = {
    "1": {
        "id": "1",
        "brand": "Parfum de Marly",
        "name": "Valaya",
        "image": "https://us.parfums-de-marly.com/cdn/shop/files/VALAYA_75ml_1.png?v=1728482260&width=493",
        "year": "2023",
        "summary": "A radiant aura and yet, an impalpable softness. This elegant floral-musky-woody fragrance created by Julien Sprecher is a unique play on codes, materials and subtle contrasts. An evocation of the skin caressed by a veil of cotton. Fresh top notes as bergamot, mandarin and sweet white peach, lead to a blend of white flowers, settling on musk and ambrofix sensual base notes.",
        "price": "$390",
        "notes": ["Bergamot, Mandarin, White Peach, Vetiver, Musk"],
        "similar": ["3", "5", "6"]
    },
    "2": {
        "id": "2",
        "brand": "Burberry",
        "name": "Goddess",
        "image": "https://assets.burberry.com/is/image/Burberryltd/69BD3315-EAFC-4CCB-9DA0-81C0D1F2D33D?$BBY_V3_SL_1$&wid=1501&hei=1500",
        "year": "2023",
        "summary": "Burberry Goddess is a timeless and classic fragrance that captures the essence of sophistication and elegance. Opening with a blend of fresh and fruity notes, it immediately intrigues the senses. The heart reveals a well-balanced combination of floral and woody accords, creating a sense of depth and complexity. As the scent settles, a warm and comforting base of musk and vanilla emerges, leaving a lingering trail of refinement. ",
        "price": "$135",
        "notes": ["Vanilla", "Lavender", "Cacao", "Amber", "Wood"],
        "similar": ["5", "6", "9"]
    },
    "3": {
        "id": "3",
        "brand": "Burberry",
        "name": "Her",
        "image": "https://assets.burberry.com/is/image/Burberryltd/170DBE43-9B00-40B1-A766-F1482E6F263D?$BBY_V3_SL_1$&wid=1501&hei=1500",
        "year": "2018",
        "summary": "Burberry Her is an artful, classic blend of long-wearing feminine scents. A fruity gourmand scent opening with a trio of dark and red berries lightened by white woody accord. A blend of jasmine and violet unfurl, illuminated by a bright accord of white woods. Amber and musk envelop this long lasting scent, further elevating the fusion of floral and fruity facets.",
        "price": "$168",
        "notes": ["Blackcurrant", "Blueberry", "Raspberry", "Jasmine Accord", "Violet", "Musk", "Dry Amber"],
        "similar": ["1", "5", "10"]
    },
    "4": {
        "id": "4",
        "brand": "Le Labo",
        "name": "Jasmin 17",
        "image": "https://6bygeebeauty.com/cdn/shop/products/jasmin17_50ml.gif?crop=center&height=1080&v=1548878900&width=1080",
        "year": "2006",
        "summary": "This natural jasmine is the floral perfume par excellence, and was created as a modern alternative to the old-fashioned traditional floral signatures. Its short formula gives it such a distinctive character that once you wear it, you’ll never forget it. A unique floral impact whose sensuality and lure is amplified by a majestically harmonious chord of musk, sandalwood, and vanilla. We refuse all responsibility for any havoc this perfume might create in your circle of friends...",
        "price": "$107",
        "notes": ["Bitter Orange", "Jasmine", "Musk", "Sandalwood", "Amber", "Vanilla"],
        "similar": ["6", "8", "10"]
    },
    "5": {
        "id": "5",
        "brand": "Byredo",
        "name": "Bal d'Afrique",
        "image": "https://www.byredo.com/cdn-cgi/image/format=auto,quality=70/https://www.byredo.com/media/catalog/product/cache/c5a89872cc52c0f5e6106953800b3b5c/m/o/mob_baldafrique_edp-100_d_1.jpg",
        "year": "2009",
        "summary": "Bal d'Afrique by Byredo is a warm and radiant fragrance inspired by the vibrant cultures of Africa and Parisian avant-garde. This perfume blends bright citrus notes with floral and woody accords, creating a scent that feels both fresh and deep. The top notes include African marigold, bergamot, and bucchu, which give way to a floral heart of violet and cyclamen. The base notes of Moroccan cedarwood, vetiver, and musk add a sophisticated, lingering depth. Bal d'Afrique is a tribute to romance, adventure, and artistic expression.",
        "price": "$320",
        "notes": ["Marigold", "Bergamot", "Violet", "Cedar"],
        "similar": ["1", "3", "9"]
    },
    "6": {
        "id": "6",
        "brand": "YSL",
        "name": "Libre",
        "image": "https://www.yslbeautyus.com/dw/image/v2/AANG_PRD/on/demandware.static/-/Sites-ysl-master-catalog/default/dw3cedbd53/Images2019/Libre%20Eau%20De%20Parfum/90mL/3614272648425.jpg",
        "year": "2019",
        "summary": "Light and unobtrusive, with a synthetic soft-fruity opening. Libre Eau de Parfum is a sophisticated, floral perfume for women. Lavender essence from France combines with the sensuality of Moroccan orange blossom. As it dries down, daring notes of musk accord and warm vanilla create a contrast between freshness and warmth. This unique, long-lasting perfume can be worn year-round.",
        "price": "$140",
        "notes": ["Orange Blossom", "Lavender", "Vanilla", "Cedar"],
        "similar": ["1", "2", "4"]
    },
    "7": {
        "id": "7",
        "brand": "Jo Malone",
        "name": "Red Roses",
        "image": "https://media.johnlewiscontent.com/i/JohnLewis/231745632?fmt=auto&$background-off-white$",
        "year": "2001",
        "summary": "The timeless essence of modern romance. Inspired by a voluptuous blend of seven of the world's most exquisite roses. With crushed violet leaves and a hint of lemon, it unfolds like a bouquet of freshly cut flowers. Subtle notes of spearmint add a touch of vibrancy and freshness. Clear and romantic.",
        "price": "$168",
        "notes": ["Lemon", "Mint", "Rose", "Violet", "Honey"],
        "similar": ["3", "5", "10"]
    },
    "8": {
        "id": "8",
        "brand": "Givenchy",
        "name": "L'Interdit",
        "image": "https://ohbeauty.com/cdn/shop/files/Givenchy_L_Interdit_EDT_750x.png?v=1726855650",
        "year": "1957",
        "summary": "With its forbidden blend of white flowers and a dark accord, L'Interdit Eau de Parfum is a resolutely underground flower. It unveils a sensual bouquet of orange blossom, jasmine, and tuberose. In contrast, earthy dark tones emanate from vetiver and patchouli to create a daringly addictive and sensual fragrance. L'Interdit is ideal for a night out in the city, a romantic dinner, or an intimate gathering where you want to leave a lasting impression. Its intoxicating depth makes it especially fitting for cooler evenings and special occasions.",
        "price": "$154",
        "notes": ["Floral", "Wood", "Ginger", "Bergamot", "Patchouli", "Vetiver"],
        "similar": ["4", "6", "9"]
    },
    "9": {
        "id": "9",
        "brand": "Maison Margiela",
        "name": "'REPLICA' Beach Walk",
        "image": "https://kith.com/cdn/shop/products/MM-L3687100_1.jpg?v=1655298366",
        "year": "2012",
        "summary": "'REPLICA' Beach Walk captures the vibrant memory of a stroll by the sea on a warm summer day. Pure, sunny and blissful, it reminds you of the ocean breeze under the heat of the sun as your feet sink into the hot sand, with the taste of salt and the scent of sunscreen. This unisex fragrance is ideal for casual daytime wear, vacations by the ocean, or any moment when you want to bring the feeling of summery, sunkissed-skin with you.",
        "price": "$165",
        "notes": ["Floral", "Bergamot", "Pink Pepper", "Ylang Ylang", "Coconut Milk", "Cedarwood"],
        "similar": ["2", "5", "8"]
    },
    "10": {
        "id": "10",
        "brand": "Maison Margiela",
        "name": "'REPLICA' On a Date",
        "image": "https://perfumelovemanila.com/cdn/shop/files/ph-11134207-7r98x-lmzq8odw8htr0b_1200x1200.jpg?v=1709349657",
        "year": "2022",
        "summary": "A date overlooking the magnificent vineyards of Provence, enveloped in the golden glow of a late summer’s sunset. The scent of ripe grapes and fresh roses filling the air... The perfect rendez-vous. 'REPLICA' On a Date is a new thrilling scent inspired by a magical date on a late summer’s evening overlooking the magnificent vineyards of Provence at sunset. It captures the sparkling and addictive fruitiness of ripe grapes soaked in warm sunshine, and the delicate yet decisive character of wild roses. 'REPLICA' On a Date sets the senses on high with memories of dating and falling in love that are unique and profound. This perfume is perfect for a cozy autumn evening, a candlelit dinner, or a weekend getaway where romance and relaxation blend effortlessly.",
        "price": "$165",
        "notes": ["Fruity", "Black Currant", "Bergamot", "Rose", "Patchouli", "Musk"],
        "similar": ["3", "4", "7"]
    }
}


@app.route("/")
def home():
    featured = random.sample(list(dataset.keys()), 3)
    featured = {key: dataset[key] for key in featured}
    return render_template("home.html", featured=featured)


@app.route("/view/<id>")
def perfume_view(id):
    referrer = request.referrer
    item = dataset.get(id)

    if item:
        return render_template("perfume_view.html", perfume=item, dataset=dataset, referrer=referrer)
    else:
        return "Perfume not found", 404

@app.route("/search")
def search_page():
    query = request.args.get("q", "").strip().lower()
    results = {id: perfume for id, perfume in dataset.items() if query in perfume['brand'].lower()
               or query in perfume['name'].lower()
               or query in perfume['summary'].lower()
               or any(query in note.lower() for note in perfume['notes'])}
    return render_template("search_results.html", query=query, results=results)

@app.route("/api/search", methods=["GET"])
def api_search():
    query = request.args.get("q", "").strip().lower()
    if not query:
        return render_template("search_results.html", query="", results={})
    results = {id: perfume for id, perfume in dataset.items() 
               if query in perfume['brand'].lower() 
               or query in perfume['name'].lower() 
               or query in perfume['summary'].lower() 
               or any(query in note.lower() for note in perfume['notes'])}
    
    return render_template("search_results.html", query=query, results=results)


@app.template_filter('highlight')
def highlight(content, query):
    query_lower = query.lower()

    if isinstance(content, list):
         return ', '.join([
            item if query_lower not in item.lower() else 
            item.replace(query, f'<span class="highlight">{query}</span>')
                .replace(query_lower.capitalize(), f'<span class="highlight">{query_lower.capitalize()}</span>')
                .replace(query_lower.upper(), f'<span class="highlight">{query_lower.upper()}</span>')
                .replace(query_lower, f'<span class="highlight">{query_lower}</span>')
            for item in content
        ])
    
    return content if query_lower not in content.lower() else \
        content.replace(query, f'<span class="highlight">{query}</span>') \
               .replace(query_lower.capitalize(), f'<span class="highlight">{query_lower.capitalize()}</span>') \
               .replace(query_lower.upper(), f'<span class="highlight">{query_lower.upper()}</span>') \
               .replace(query_lower, f'<span class="highlight">{query_lower}</span>')

@app.route("/add", methods=["GET"])
def add_page():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def add_perfume():
    data = request.get_json()
    errors = {}
    required = ["brand", "name", "price", "year", "notes", "summary", "image"]

    for field in required:
        if not data.get(field) or str(data[field]).strip() == "":
            errors[field] = f"{field.capitalize()} is required."
    
    if "year" in data and data["year"].strip():
        try:
            year = int(data["year"])
            if not (1800 <= year <= 2100):
                errors["year"] = "Year must be between 1800 and 2100."
        except ValueError:
            errors["year"] = "Year must be a valid number."

    if "price" in data and data["price"].strip():
        price = data["price"].strip()
        if not price.startswith("$"):
            price = f"${price}"
        try:
            float(price.replace("$", ""))
        except ValueError:
            errors["price"] = "Price must be a valid number."

    if "notes" in data:
        if not isinstance(data["notes"], list) or not all(isinstance(note, str) for note in data["notes"]):
            errors["notes"] = "Notes must be a list of words (e.g., ['vanilla', 'jasmine'])."

    if "image" in data and data["image"].strip():
        if not (data["image"].startswith("http") and any(ext in data["image"] for ext in [".png", ".jpg", ".jpeg", ".gif", ".webp"])):
            errors["image"] = "Image must be a valid URL ending in .jpg, .png, etc."

    if errors:
        return jsonify(errors=errors), 400

    brand = data["brand"].strip()
    name = data["name"].strip()
    price = data["price"].strip()
    year = data["year"].strip()
    image = data["image"].strip()
    summary = data["summary"].strip()
    notes = ", ".join(data["notes"]) if isinstance(data["notes"], list) else data["notes"].strip()

    # generate similar perfumes
    similarity = {}
    for idx, perfume in dataset.items():
        shared_notes = set(notes) & set(map(str.lower, perfume["notes"]))  # Count shared notes
        similarity[idx] = len(shared_notes)

    # top 3 similar
    similar_perfumes = sorted(similarity, key=similarity.get, reverse=True)[:3]

    

    id = str(max(map(int, dataset.keys())) + 1)
    # similar = list(dataset.keys())[-3:] if len(dataset) >= 3 else list(dataset.keys())

    dataset[id] = {
        "id": id,
        "brand": brand,
        "name": name,
        "image": image,
        "year": year,
        "summary": summary,
        "price": price,
        "notes": notes,
        "similar": similar_perfumes
    }

    return jsonify({"success": True, "id": id, "message": "New item successfully created."}), 201

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_perfume(id):
    perfume = dataset.get(id)

    if not perfume:
        return "Perfume not found", 404

    if request.method == "POST":
        data = request.json
        perfume.update({
            "brand": data.get("brand", perfume["brand"]),
            "name": data.get("name", perfume["name"]),
            "image": data.get("image", perfume["image"]),
            "year": data.get("year", perfume["year"]),
            "summary": data.get("summary", perfume["summary"]),
            "price": data.get("price", perfume["price"]),
            "notes": data.get("notes", perfume["notes"]),
            "similar": data.get("similar", perfume["similar"]),
        })

        return jsonify(success=True)

    return render_template("edit.html", perfume=perfume)



if __name__ == "__main__":
    app.run(debug=True, port=5001)
