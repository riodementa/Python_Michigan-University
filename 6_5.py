# Exercise 6.5
text = "X-DSPAM-Confidence:    0.8475";

spacePos = text.find(" ")
number = text[spacePos::1]

result = float(number.lstrip())
print result

# option 2
index=text.find(".")
print text[index-1:]
