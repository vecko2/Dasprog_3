string = (input())
def encode_string(S):
    seen = set()
    result = []

    for str in S:
        if str != " ":
            if str not in seen:
                seen.add(str)
                result.append(str)

    return "".join(result)

print(encode_string(string))
    