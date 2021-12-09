import re

content = 'Extra string Hello 1234567 World_This is a Regex Demo Extra stings'
#result = re.match('Hello.*?(\d+).*?Demo', content)
result1 = re.search('Hello.*?(\d+).*?Demo', content)

#print(result.group())
print(result1.group())
