def normalize_text(text):

    text = text.lower()

    replacements = {
        "gehu": "wheat",
        "chawal": "rice",
        "makka": "maize",
        "kheti": "farming",
        "paani": "water"
    }

    for word, replacement in replacements.items():
        text = text.replace(word, replacement)

    return text