#!python3

data=""

header = """<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 22.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 612 792" style="enable-background:new 0 0 612 792;" xml:space="preserve">
<style type="text/css">
	.st0{fill:#FFFFFF;stroke:#000000;stroke-miterlimit:10;}
	.st1{stroke:#000000;stroke-miterlimit:10;}
</style>"""

footer = """</svg>"""

def svg_class(text):
    if text == "0":
        svg_class = "st0"
    else:
        svg_class = "st1"
    return svg_class

def remove_blank(data):
    data_prime = ""
    for x in data:
        if x == " ":
            print(" pow! \r")
        else:
            data_prime += x
    print(" blank spaces have been powed away! ")
    return data_prime

def get_data():
    print("--------------please pase in your binary data here:")
    print("https://www.rapidtables.com/convert/number/ascii-to-binary.html")
    print("                  -use above site")
    data = str(input())
    data = remove_blank(data)
    return data

data = get_data()

l = len(data)
bufferbits = 0

while len(data) % 9 != 0:
    data = " " + data
    bufferbits += 1


print(l, len(data))
print("buffer Bits Prepended: ", bufferbits)
i = l-1
x = 0
y = 0
text = ""
for z in range(0,49):
    text = text + "<rect x=\"" + str(x) + "\" y=\"0\" class=\"" + svg_class(data[z]) + "\" width=\"10\" height=\"10\"/>\r"
    text = text + "<rect x=\"" + str(x+10) + "\" y=\"0\" class=\"" + svg_class(data[z+1]) + "\" width=\"10\" height=\"10\"/>\r"
    text = text + "<rect x=\"" + str(x+20) + "\" y=\"0\" class=\"" + svg_class(data[z+2]) + "\" width=\"10\" height=\"10\"/>\r"
    text = text + "<rect x=\"" + str(x) + "\" y=\"10\" class=\"" + svg_class(data[z+3]) + "\" width=\"10\" height=\"10\"/>\r"
    text = text + "<rect x=\"" + str(x+10) + "\" y=\"10\" class=\"" + svg_class(data[z+4]) + "\" width=\"10\" height=\"10\"/>\r"
    text = text + "<rect x=\"" + str(x+20) + "\" y=\"10\" class=\"" + svg_class(data[z+5]) + "\" width=\"10\" height=\"10\"/>\r"
    text = text + "<rect x=\"" + str(x) + "\" y=\"20\" class=\"" + svg_class(data[z+6]) + "\" width=\"10\" height=\"10\"/>\r"
    text = text + "<rect x=\"" + str(x+10) + "\" y=\"20\" class=\"" + svg_class(data[z+7]) + "\" width=\"10\" height=\"10\"/>\r"
    text = text + "<rect x=\"" + str(x+20) + "\" y=\"20\" class=\"" + svg_class(data[z+8]) + "\" width=\"10\" height=\"10\"/>\r"
    x = x + 30
#print(text)


file = open("marainbinary.svg","w")
file.write(header)
file.write(text)
file.write(footer)
file.close()
print(" file has been created named marainbinary.svg ")
    
    
    

    
    
