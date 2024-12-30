"""removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n". 
Expected output = pythonpython"""

bad_char=[';',':','!','*']
strings="py;th*o:n!;py*t*h:o!n"
for i in bad_char:
    if i in strings:
        strings=strings.replace(i,'')
print(strings)