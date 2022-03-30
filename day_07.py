def capital_indexes(strng: str) -> list[int]:
    # [ch.find() for ch in strng if ch.isupper()]
    return [i for i, ch in enumerate(strng) if ch.isupper()]

print(capital_indexes("PawEloS"))
