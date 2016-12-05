import hashlib


def gen_code_1(key):
    hash = 1
    code = ""
    while len(code) < 8:
        digest = hashlib.md5("{}{}".format(key, hash).encode("utf-8")).hexdigest()
        if digest.startswith("00000"):
            code += digest[5]
            print(code)
        hash += 1
    return code


def gen_code_2(key):
    hash = 1
    code = ['-'] * 8
    while '-' in code:
        digest = hashlib.md5("{}{}".format(key, hash).encode("utf-8")).hexdigest()
        if digest.startswith("00000"):
            if '0' <= digest[5] <= '7':
                if code[int(digest[5])] == "-":
                    code[int(digest[5])] = digest[6]
            print("".join(code))
        hash += 1
    return "".join(code)


input_key = "reyedfim"
print(gen_code_1(input_key))
print(gen_code_2(input_key))



