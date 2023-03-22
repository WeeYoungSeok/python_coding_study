s = input()
hex_s = int(s, 16)
for i in range(1, 16):
    print("%X"%hex_s,"*","%X"%i,"=","%X"%(hex_s*i), sep = "")