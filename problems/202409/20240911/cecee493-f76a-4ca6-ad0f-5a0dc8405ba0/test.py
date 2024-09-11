text1 = 'b1651c307aa6263ecf94fed58b44d90bba293a0944bl02e52528bac139f4b9e5'
text2 = 'b1651c307aa6263ecf94fed58b44d90bba293a0944b102e52528bac139f4b9e5'

for i in range(len(text1)):
    if (text1[i] == text2[i]):
        print(text1[i])
    else:
        print(text1[i], text2[i])