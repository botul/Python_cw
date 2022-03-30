def gerund_infinitive(strng: str) -> str:
    if strng[-3:] != 'ing':
        return "To nie jest rzeczownik odsłowny"
    else:
        return f"to {strng[:-3]}"

print(gerund_infinitive("doing"))
