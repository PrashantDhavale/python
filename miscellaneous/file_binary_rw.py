from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


readIntoData = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(readIntoData)
    bf.close()

    for b in readIntoData:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


