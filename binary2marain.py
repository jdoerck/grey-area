#!python3
import time
import convert, svg, options

print("Starting Text to Marain Converter")

raw_data = options.get_data()
data = convert.textToBinary(raw_data)

# Options
byte_rows = 2
byte_size = 10

l = len(data)
bufferbits = 0
byte_length = 7
word_constant = 3
x = 0
y = 0
text = ""

letter_size = byte_size * word_constant
row_length = byte_rows * byte_length
i = 0

print(f"Data: {len(data)}")

while len(data) % 9 != 0:
    data = " " + data
    bufferbits += 1

b = l-byte_length
for z in range(0, b):

    i = i + 1
    text = text + "<rect x=\"" + str(x) + "\" y=\"" + str(y) + "\" class=\"" + svg.define_class(data[z]) + "\" width=\"" + str(byte_size) + "\" height=\"" + str(byte_size) + "\"/>\r"
    text = text + "<rect x=\"" + str(x+10) + "\" y=\"" + str(y) + "\" class=\"" + svg.define_class(
        data[z+1]) + "\" width=\"" + str(byte_size) + "\" height=\"" + str(byte_size) + "\"/>\r"
    text = text + "<rect x=\"" + str(x+20) + "\" y=\"" + str(y) + "\" class=\"" + svg.define_class(
        data[z+2]) + "\" width=\"" + str(byte_size) + "\" height=\"" + str(byte_size) + "\"/>\r"
    text = text + "<rect x=\"" + str(x) + "\" y=\"" + str(y+10) + "\" class=\"" + svg.define_class(
        data[z+3]) + "\" width=\"" + str(byte_size) + "\" height=\"" + str(byte_size) + "\"/>\r"
    text = text + "<rect x=\"" + str(x+10) + "\" y=\"" + str(y+10) + "\" class=\"" + svg.define_class(
        data[z+4]) + "\" width=\"" + str(byte_size) + "\" height=\"" + str(byte_size) + "\"/>\r"
    text = text + "<rect x=\"" + str(x+20) + "\" y=\"" + str(y+10) + "\" class=\"" + svg.define_class(
        data[z+5]) + "\" width=\"" + str(byte_size) + "\" height=\"" + str(byte_size) + "\"/>\r"
    text = text + "<rect x=\"" + str(x) + "\" y=\"" + str(y+20) + "\" class=\"" + svg.define_class(
        data[z+6]) + "\" width=\"" + str(byte_size) + "\" height=\"" + str(byte_size) + "\"/>\r"
    text = text + "<rect x=\"" + str(x+10) + "\" y=\"" + str(y+20) + "\" class=\"" + svg.define_class(
        data[z+7]) + "\" width=\"" + str(byte_size) + "\" height=\"" + str(byte_size) + "\"/>\r"
    text = text + "<rect x=\"" + str(x+20) + "\" y=\"" + str(y+20) + "\" class=\"" + svg.define_class(
        data[z+8]) + "\" width=\"" + str(byte_size) + "\" height=\"" + str(byte_size) + "\"/>\r"
    x = x+letter_size

    if (i == row_length):
        i = 0
        x = 0
        y = y + letter_size


now = time.localtime()
timestamp = str(time.strftime("%Y%m%d%H%M%S", now))
filename = timestamp + '-' + raw_data[0:10] + ".svg";

file = open(filename, "w")
file.write(svg.get_header((row_length*word_constant), y))
file.write(text)
file.write(svg.get_footer())
file.close()
print("File has been created named " + filename)
