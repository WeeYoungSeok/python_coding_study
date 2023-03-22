w, h, b = map(int, input().split())
print("{:.1f}".format(w * h * b / 8 / 1024 / 1024), "MB")