import re

entity_patterns = {
    "full_name": r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b",
    "email": r"[\w\.-]+@[\w\.-]+",
    "phone_number": r"\b\d{10}\b",
    "dob": r"\b\d{2}/\d{2}/\d{4}\b",
    "aadhar_num": r"\b\d{4}-\d{4}-\d{4}\b",
    "credit_debit_no": r"\b\d{16}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b\d{2}/\d{2}\b"
}

def mask_pii(text):
    entities = []
    for entity, pattern in entity_patterns.items():
        for match in re.finditer(pattern, text):
            start, end = match.span()
            matched_text = match.group()
            entities.append({
                "position": [start, end],
                "classification": entity,
                "entity": matched_text
            })
            text = text.replace(matched_text, f"[{entity}]")
    return text, entities

def demask_pii(text, entities):
    for ent in entities:
        text = text.replace(f"[{ent['classification']}]", ent['entity'])
    return text
