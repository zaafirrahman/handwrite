import random
import os

letter_color = "blue"
letter_set = "set0"
trcolor = False
totalset = len(os.listdir("font-scanned/letters")) + 1

htmlc = [
    "<html><head><style>.lines{width:100%;height:auto;float:left;}#paper{border: 10px solid black;background-image:url('font-scanned/texture.png');height:297mm;float:left;padding-top:76.5px;padding-left:116px;padding-right:76.5px;padding-bottom:76.5px;width:210mm;}img,span{height:45px;float:left;margin-bottom:1px;}.clblack{filter:brightness(30%);}.clblue{filter:brightness(100%);}</style></head><body><div id='paper'>"
]

with open("draft.txt", "r") as textfile:
    for line in textfile:
        curst = line.strip()
        htmlc.append('<div class="lines">')
        for ch in curst:
            chcode = ord(ch)

            random_letter = random.randrange(1, totalset)
            letter_set = "set{}".format(random_letter)

            if chcode == 35:
                if trcolor:
                    letter_color = "blue"
                    trcolor = False
                else:
                    letter_color = "black"
                    trcolor = True
            elif chcode == 36:
                htmlc.append("<span></span>")

            if chcode != 35 and chcode != 36:
                htmlc.append(
                    "<img src='font-scanned/letters/{}/{}/{}.png'/>".format(
                        letter_set, letter_color, chcode
                    )
                )
        htmlc.append("</div>")

htmlc.append("</div></body></html>")

with open("sheet.html", "w") as page_html:
    page_html.writelines(htmlc)
