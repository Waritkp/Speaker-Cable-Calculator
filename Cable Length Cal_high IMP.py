##

v=100
Size = int(input("AWG size (12,14,16,18): "))
Z =(v**2)/(float(input("Power [W]: ")))

##

if Size == 12:
    A = 4.0
elif Size == 14:
    A = 2.5
elif Size == 16:
    A = 1.5
elif Size == 18:
    A = 0.75
else:
    print("Unsupported AWG size")
    exit()

L = Z * A
print(f"{L} [m]")
input("Press Enter to exit...")
