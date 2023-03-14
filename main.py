string1 = """
Hello World!
"""

string2 = """
Hello Earth!
"""

if string1 == string2:
    print("Strings are the same")
else:
    output = ""
    for i in range(min(len(string1), len(string2))):
        if string1[i] != string2[i] and string2[i] != "\n":
            output += "[" + string2[i] + "]"
        else:
            output += string1[i]
    if len(string1) > len(string2):
        output += "[" + string1[len(string2):] + "]"
    elif len(string2) > len(string1):
        output += "[" + string2[len(string1):] + "]"
    if output != string1:
        print("Strings are different")
    else:
        print("Strings are mostly the same")
    print(output)
