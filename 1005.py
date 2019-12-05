n = input()
count = 0
for i in n:
    count += int(i)
output = []
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
count = str(count)
for i in count:
    output.append(words[int(i)])
print(" ".join(output))
