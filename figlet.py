from pyfiglet import Figlet
figlet = Figlet()
import sys
import random
text = input("input a text: ")
if len(sys.argv) == 1:
    fonts = figlet.getFonts()
    figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(text))
elif len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[3])
    print(figlet.renderText(text))
else: sys.exit("argument typing error")