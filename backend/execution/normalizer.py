KNOWN_BRANDS = [ "2E", "AGM", "ALCATEL", "Apple", "Archos", "Assistant", "Astro", "ASUS", "BlackBerry", "Blackview", "Bluboo", "Bravis", "CAT", "Coolpad", "Crosscall", "Cubot", "DOOGEE", "Elephone", "ERGO", "Fly", "General", "Globex", "Google", "Honor", "HTC", "HUAWEI", "iOutdoor", "Jinga", "KENEKSI", "Land", "LEAGOO", "Lenovo", "LG", "MAFAM", "Maxcom", "Meizu", "Microsoft", "Motorola", "myPhone", "Nokia", "Nomi", "NUU", "OnePlus", "OPPO", "Oukitel", "Philips", "Prestigio", "realme", "Rezone", "Samsung", "Sharp", "Sigma mobile", "Smartex", "Sony", "S-TELL", "Tecno", "Ulefone", "UMIDIGI", "Vernee", "Viaan", "vivo", "Vodafone", "Xiaomi", "ZTE" ]

def extract_brand_and_model(text):
    text_l = text.lower()
    for brand in KNOWN_BRANDS:
        brand_l = brand.lower()
        if brand_l in text_l:
            # FIX: Find the start and end position of the brand regardless of case
            start_idx = text_l.find(brand_l)
            end_idx = start_idx + len(brand_l)
            
            # Slice the string to remove the brand part
            model = (text[:start_idx] + text[end_idx:]).strip()
            return brand, model
            
    return None, text

def normalize_intent(intent):
    for f in intent.get("filters", []):
        if f["column"] == "model_name":
            brand, model = extract_brand_and_model(f["value"])

            # overwrite value with model only
            f["value"] = model

            # inject brand filter if detected
            if brand:
                intent["filters"].append({
                    "column": "brand_name",
                    "op": "=",
                    "value": brand
                })
                
    intent["limit"] = 5
    return intent
