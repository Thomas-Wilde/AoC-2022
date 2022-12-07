##--------------------------------------------------------------------------##
# file = open("example.data", "r")
file = open("input.data", "r")
data = file.readlines()[0]
signal = [*data]
print(signal)
## --- fill buffer with start data
buffer = []
for i in range(14):
    buffer.append(signal[i])

## --- iterate over data to find marker
idx = 14
while True:
    buffer.append(signal[idx])
    buffer.pop(0)
    check = [*set(buffer)]
    if len(check) == 14:  # --- if True we found the marker
        print("found marker at position")
        print(buffer)
        print(idx + 1)
        break
    idx += 1
