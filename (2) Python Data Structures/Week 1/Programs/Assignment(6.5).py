text = "X-DSPAM-Confidence:    0.8475"

ind = text.find("0")

print(float(text[ind:]))