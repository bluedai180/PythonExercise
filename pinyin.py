# coding = utf-8
result = []
pinyin = []

data = open("Files/rawdict_utf16_65105_freq.txt", 'r', encoding='utf-8')

for x in data.readlines():
    result.append(x.split(' '))

for y in result:
    if len(y) == 5:
        pinyin.append((y[0], "xx_%s_%s" % (y[3], y[4])))
    elif len(y) == 6:
        pinyin.append((y[0], "xx_%s_%s_%s" % (y[3], y[4], y[5])))
    elif len(y) == 7:
        pinyin.append((y[0], "xx_%s_%s_%s_%s" % (y[3], y[4], y[5], y[6])))
    elif len(y) == 4:
        pinyin.append((y[0], "xx_%s" % y[3]))

str_text = []
str_pinyin = ''
i = len(pinyin)
f = open("pinyin.txt", 'w')
for index in range(i):
    if index < i - 1 and pinyin[index][1] == pinyin[index + 1][1]:
        str_text.append(pinyin[index][0])
    else:
        str_text.append(pinyin[index][0])
        str_pinyin = pinyin[index][1]
        f.write("%s = {\"%s\"}\n" % (str_pinyin.replace('\n', ''), "".join(str_text)))
        str_text.clear()

f.close()
data.close()
