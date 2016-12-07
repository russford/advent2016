import re


def has_abba(s):
    return any([s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1] for i in range(len(s)-3)])


def break_ip_addr(ip_addr):
    text = re.split("[\[\]]", ip_addr)
    return text[::2], text[1::2]


def supports_tls(ip_addr):
    sequences, hypernets = break_ip_addr(ip_addr)
    if any([has_abba(s) for s in hypernets]):
        return False
    if any([has_abba(s) for s in sequences]):
        return True
    return False


def supports_sls(ip_addr):
    sequences, hypernets = break_ip_addr(ip_addr)
    for s in sequences:
        for i in range(len(s)-2):
            if s[i] == s[i+2] and s[i] != s[i+1]:
                if any([s[i+1] + s[i] + s[i+1] in h for h in hypernets]):
                    return True
    return False

with open("day07.txt", "r") as f:
    file_input = f.readlines()

print(sum(map(supports_tls, file_input)))
print(sum(map(supports_sls, file_input)))
