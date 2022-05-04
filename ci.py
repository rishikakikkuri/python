p = int(input("enter the principal"))
t = int(input("enter the time period"))
r = float(input("enter the rate of interest"))
Amount = p * (pow((1 + r / 100), t))
ci = Amount - p
print("Compound interest is", ci)