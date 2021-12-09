import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^(Hello)\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.span())

#两个（），默认输出第一个（）中的字符串，我们输入两次，打印两个（）