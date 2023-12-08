input_values = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

calibration_values = []
calibration_values_sum = 0
# For part 2
input_values = (
    input_values.replace('one', 'on1e')
    .replace('two', 'tw2o')
    .replace('three', 'thre3e')
    .replace('four', 'fou4r')
    .replace('five', 'fiv5e')
    .replace('six', 'si6x')
    .replace('seven', 'seve7n')
    .replace('eight', 'eigh8t')
    .replace('nine', 'nin9e')
)
for i in input_values.splitlines():
    digit_list = [d for d in i if d.isdigit()]
    calibration_value = int(''.join([digit_list[0],  digit_list[-1]]))
    calibration_values.append(calibration_value)
    calibration_values_sum += calibration_value

print(calibration_values)
print(calibration_values_sum)



