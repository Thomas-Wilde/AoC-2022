##--------------------------------------------------------------------------##
# file = open("example.data", "r")
file = open("input.data", "r")
lines = file.readlines()

# --- remove linebreak
for idx in range(len(lines)):
    lines[idx] = lines[idx].replace("\n", "")

dir_stack = []
mem_stack = []
# --- evaluate data
idx = 0
total_sum = 0
while idx < len(lines):
    line = lines[idx]
    # print("line: " + line)
    # --- check $ ls
    if line.startswith("$ ls"):
        # --- estimate directory
        dir = lines[idx - 1].split(" ")[2]
        dir_stack.append(dir)
        mem_stack.append(int(0))
        # print("ls in directory " + dir)
        # ---
        idx += 1
        line = lines[idx]
        # print(line)
        while not line.startswith("$"):
            idx += 1
            # --- skip "dir" entry
            if line.startswith("dir"):
                line = lines[idx]
                continue
            # --- extract number
            # print(line)
            number = line.split(" ")[0]
            # print(number)
            line = lines[idx]
            mem_stack[-1] += int(number)
    # --- check $ ls
    if line.startswith("$ cd .."):
        # print(str(mem_stack[-1]) + " " + str(dir_stack[-1]))
        tmp_mem = mem_stack.pop()
        mem_stack[-1] += tmp_mem
        dir_stack.pop()
        if tmp_mem <= 100000:
            # print(tmp_mem)
            total_sum += tmp_mem
    idx += 1
    cd_line = line

while len(dir_stack) > 1:
    # print(str(mem_stack[-1]) + " " + str(dir_stack[-1]))
    tmp_mem = mem_stack.pop()
    mem_stack[-1] += tmp_mem
    if tmp_mem <= 100000:
        # print(tmp_mem)
        total_sum += tmp_mem
    dir_stack.pop()


print("result for task 1: " + str(total_sum))
used_mem = mem_stack[-1]
unused = 70000000 - used_mem
to_free = 30000000 - unused
print("use this for task to: " + str(to_free))
