hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

if(h <= 40):
    gross = h*r
    print(gross)
else:
    gross = h*r
    ir = (h-40.0)*(r*0.5)
    ngross = gross+ir
    print(ngross)
