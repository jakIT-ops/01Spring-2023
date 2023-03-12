import re

text = "Here are some example emails: jawhaabayr255@gmail.com, jawhaacs@gmail.com, and jakkitsama@gmail.com"

# regex ashiglaj emailvvdiig shuuj harah
email_regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
emails = email_regex.findall(text)
# replace hiih
new_text = re.sub("gmail.com", "yahoo.com", text)

for email in emails:
    print(email)
# email regex tailbar

# [a-zA-Z0-9._%+-]: Үсэг, тоо, ., _, %, +, эсвэл - гэсэн тэмдэгтүүдийн дурын хослолтой тохирно.
# +: Өмнөх загваруудын нэг буюу хэд хэдэн загвартай таарах
# @: тэмдэгтэй таарах.
# [a-zA-Z0-9.-]: Үсэг, тоо, ., эсвэл - гэсэн тэмдэгтүүдийн дурын хослолтой тохирно.
# [a-zA-Z]{2,}: Хоёр ба түүнээс дээш үсэгтэй тохирно.