import re
def testcompile():
  regex = r"(\d{3})-\d{7}"

  regexobject = re.compile(regex)
  # print(regexobject.search("aaa 027-4567892  dd 111-222").group())
  print(regexobject.findall("aaa 027-4567892  dd 111-2222222"))
  # print(regexobject.search("aaa 027-4567892  dd 111-222").groups())
  # print(regexobject.search("bbb 021-1234567").group())

  # print(regexobject.search("ccc 010-123456"))

def testignorecase():
  print(re.search('world', "hello world !").group())
  print(re.search('world', "hello world !").group())
  print(re.search('world', "hello world !"))

testcompile()
testignorecase()
