'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''

# def func1(name):
#     if not isinstance(name, str):
#         return 'The name is not str'
#     elif str.isupper(name[0]):
#         return name
#     else:
#         x = str.upper(name[0])
#         return x + name[1:]
#
# print(func('name'))

"""
2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"

"""
# def func(name, callback=None):
#     if callback == str.lower:
#         return str.lower(name)
#     elif callback == str.upper:
#         return str.upper(name)
#     elif callback is None:
#         if not isinstance(name, str):
#             return 'The name is not str'
#         elif str.isupper(name[0]):
#             return name
#         else:
#             x = str.upper(name[0])
#             return x + name[1:]
#     else:
#         return "The callback is not right"
#
# print(func('name', callback=str.upper))

"""
3.定义一个func(*kargs),效果如下。

l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
	print i
#输出 5 3 4 5 6


"""
# 黑人问号.jpg
# def func(*kargs):
#     return kargs
#
# l = func(1,2,3,4,5)
# for i in l:
# 	print (i)

"""
4.定义一个func(*kargs)，该函数效果如下。

assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None

"""

# def func(*kargs):
#     for x in kargs:
#         if isinstance(x, str):
#             return x
# print(func(222,1111))


"""
5.定义一个func(name=None,**kargs),该函数效果如下。

assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"

"""
a = []
def func(name=None, **kargs):
    if kargs is None:
        return name
    else:
        a.append(name)
        for x, y in kargs.items():
            a.append(str(x) + ":" + str(y))
        return ",".join(a)

#assert func("lilei",years=4) == "lilei,years:4"
print(func("lilei",years=4,body_weight=20, abc=40))
#assert func("lilei",years=4,body_weight=20) == "lilei,years:4,body_weight:20"

