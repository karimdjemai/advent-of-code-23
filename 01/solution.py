import re

input = open('./input.txt', 'r')
lines = input.readlines()
sum = 0

for line in lines:
    digits = re.findall(r'\d', line)
    calibration_value = int(digits[0] + digits[-1])
    sum += calibration_value
    print(calibration_value)

print(sum)
