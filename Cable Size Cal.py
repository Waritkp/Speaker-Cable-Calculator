##

L = float(input("Cable Lenght : "))
Z = float(input("Impedance [Ohms]: "))

##

A = L/Z

##

if A <= 0.75 :
    AWG = 18
elif A <= 1.5 :
    AWG = 16
elif A <= 2.5 :
    AWG = 14
elif A <= 4.0 :
    AWG = 12
elif A < 0.5 :
    AWG = "AWG20 or above"
elif A > 4.0 :
    AWG = "BIGGER THAN AWG12"

print(f"Area = {A} [mm^2]")
print(f"Recommended AWG : {AWG}")
input("Press Enter to exit...")

