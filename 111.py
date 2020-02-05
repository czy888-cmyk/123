str1='12 中国45 abcdef!?AD'
import re
re1=re.sub('[a-zA-Z]','',str1)
print(re1)