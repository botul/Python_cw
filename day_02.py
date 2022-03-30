def switch_case(strng):
    result = ""
    for ch in strng:
        if ch.islower():
            result += (ch.upper())
        else:
            result += (ch.lower())
    return result

print(switch_case("bOtUl"))


#List comperhension

def switch_case2(strng1):
    return ''.join(ch.lower() if ch.isupper() else ch.upper() for ch in strng1)

print(switch_case2("2-bOtUl"))