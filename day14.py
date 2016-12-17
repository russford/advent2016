import hashlib

def check_rep (string):
    for i in range(len(string)-3):
        if string[i:i+3] == string[i]*3:
            return string[i]
    return None

def get_hash (salt, num, reps):
    hash = hashlib.md5((salt+str(num)).encode("utf-8")).hexdigest()
    for i in range(reps):
        hash = hashlib.md5(hash.encode("utf-8")).hexdigest()
    return hash


def get_keys(key, n, reps):
    keys = []
    hashes = [get_hash(key, i+1, reps) for i in range(1000)]
    hash = get_hash (key, 0, reps)
    for i in range(100000):
        for j in range(len(hash)):
            if hash[j:j+3] == hash[j] * 3:
                if any([hash[j] * 5 in h for h in hashes]):
                    keys.append (i)
                    print("got {} key: {}".format(len(keys), i))
                break
        if len(keys) == 64: break
        hash = hashes[i%1000]
        hashes[i % 1000] = get_hash(key, i+1001, reps)
    return keys


key = "yjdafjpo"

keys = get_keys(key, 64, 2016)
print(keys)
