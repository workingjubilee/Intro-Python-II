import time

print("\033[?1049h\033[H")
print("Text!")
time.sleep(1)

print("Returning in 5 seconds!")
time.sleep(5)

print("\033[?1049l")
