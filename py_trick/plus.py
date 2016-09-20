chars = ["a", "b", "c"]

# error: an only concatenate list (not "str") to list
# chars = chars + 'd'
# chars = chars + 'e',

chars += "d"
print chars

tmp = "e",
print tmp
