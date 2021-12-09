dict_test = {'Name': 'Runoob', 'num':{'first_num': '66', 'second_num': '70'}, 'age': '15'}

print(dict_test.get('first_num')) # None

print(dict_test.get('num').get('first_num')) # 66
