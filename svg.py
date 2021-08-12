def define_class(text):
    if text == "0":
        svg_class = "st0"
    else:
        svg_class = "st1"
    return svg_class

def get_header(w, h):
    # print(w)
    # w = 420
    w = w*10
    h = h+30
    header = """<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 22.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
    viewBox="0 0 """ + str(w) + """ """ + str(h) + """" style="enable-background:new 0 0 """ + str(w) + """ """ + str(h) + """;" xml:space="preserve">
<style type="text/css">
    .st0{fill:#FFFFFF;padding: 0;margin: 0;border: 0;stroke: 0}
    .st1{padding: 0;margin: 0;border: 0;stroke: 0}
</style>"""
    return header

def get_footer():
    footer = """</svg>"""

    return footer
