import sys
data = open(sys.argv[1], 'rb').read()
pub = data[-32:]
alpha = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
payload = b"\xed\x01" + pub
n = int.from_bytes(payload, 'big')
enc = ""
while n:
    n, r = divmod(n, 58)
    enc = alpha[r] + enc
print("did:key:z" + enc)
