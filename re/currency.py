import re

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^He.*mo$', content)
#result = re.match('^Hello.*Demo$', content) 用注释的这行也行
print(result)
print(result.group())
print(result.span())
