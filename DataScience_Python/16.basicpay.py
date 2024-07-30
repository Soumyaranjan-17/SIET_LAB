#basic pay, da, ta, hra
bp = int(input("Enter the BP: "))
if(bp > 50000):
    da = 0.7 * bp
    ta = 0.5 * bp
    hra = 0.1 * bp
elif(bp > 30000):
    da = 0.7 * bp
    ta = 0.3 * bp
    hra = 0.05 * bp
else:
    da = 0.7 * bp
    ta = 0.15 * bp
    hra = 0.03 * bp

np = bp+da+ta+hra
print(f"Net Pay: {np}")