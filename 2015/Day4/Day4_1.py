import hashlib
file= open("Day4/Day4.txt")
code=file.readline()
count=1
while True:
    codeFull=code+str(count)
    hash=hashlib.md5(codeFull.encode()).hexdigest()
    if str(hash).startswith('000000'):
        break
    count+=1
print(count)