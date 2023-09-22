drive = "C: \\"
folder = "scripts\\python\\"
file = "myscript.py"
path = drive + folder + file
print(path)

newText = "text with\nnewline"
print(newText)
newText = r"text with\\nnewline"
print(newText)

justText = "Mc Donald's"
print(justText)
#justText = 'Mc Donald's --> error syntax


justText = 'Mc Donald\'s'
print(justText)