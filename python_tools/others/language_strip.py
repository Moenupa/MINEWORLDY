string = "\n\t000030141200123322211013210103130000"
print(string.strip("0"))
print(string.strip("12"))
print(string.strip("4"))
print(string.strip("03"))
print(string.strip().strip("03"))
#strip will delete the string from both two ends
#so that two ends will show none of the letters inside '___'
#rstrip\lstrip do starts\ends strip
