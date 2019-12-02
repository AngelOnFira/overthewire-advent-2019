lookup = {
    0: " 0",
    1: ".,'?!\"1-()@/:",
    2: "abc2",
    3: "def3",
    4: "ghi4",
    5: "jkl5",
    6: "mno6",
    7: "pqrs7",
    8: "tuv8",
    9: "wxyz9",
    10: "@/:_;+&%*[]{}"
}

with open('sms4.csv') as f:
    lines = f.read().splitlines()

cursor = 0
last_command = -1
same_command_count = 0
last_output = ""
last_time = -1

out = []

for tup in lines:
    timing = int(tup.split(",")[0])
    print(timing - last_time)
    command = int(tup.split(",")[1])

    if timing - last_time > 1000 and last_time != -1:
        last_command = -1
        same_command_count = 0


    last_time = timing

    if command == last_command:
        same_command_count += 1
    else:
        last_command = command
        same_command_count = 0
        out.insert(cursor, last_output)
        cursor += 1

    if command <= 10:
        this_lookup = lookup[command]
        last_output = this_lookup[same_command_count % len(this_lookup)]

    if command == 100:
        pass
    if command == 101:
        out.pop()

for letter in out:
    print(letter, end="")