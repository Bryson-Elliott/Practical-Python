temperature = 50

if temperature > 80:
    print("It's too hot!")
    print("Stay inside!")
elif temperature < 60:
    print("It's too cold!")
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")


if temperature > 80 or temperature < 60: 
    print("Stay inside")
else:
    print("Enjoy the outdoors!")

forecast = "sunny"
if temperature < 80 and forecast != 'rain':
    print("Go outside")
else:
    print("stay inside")

raining = True

if not raining:
    print("go outside")
else:
    print("stay inside")



