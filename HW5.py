import colorama
from colorama import Fore, Back, Style

print(Fore.GREEN + "colorama version: " + colorama.__version__)
print()

print(Fore.GREEN + "What is inside colorama:")
print(Fore.GREEN + str(dir(colorama)))
print()

print(Fore.GREEN + "Text colors (Fore):")
print(Fore.GREEN + str(dir(Fore)))
print()

print(Fore.GREEN + "Background colors (Back):")
print(Fore.GREEN + str(dir(Back)))
print()

print(Fore.GREEN + "Styles (Style):")
print(Fore.GREEN + str(dir(Style)))
print()

print(Fore.GREEN + "What a color code looks like:")
print(Fore.GREEN + repr(Fore.RED))
print()

print(Fore.GREEN + "This is green text")
print(Fore.GREEN + Back.YELLOW + "This is green text on a yellow background")
print(Fore.GREEN + Style.BRIGHT + "This is bright green text")
print(Style.RESET_ALL + "And this is normal text again")