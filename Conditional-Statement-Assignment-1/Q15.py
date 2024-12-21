"""Write a Python program to give advice based on the temperature:
Temperature > 30°C: "It's hot, stay hydrated!"
Temperature between 15-30°C: "Enjoy the weather!"
Temperature < 15°C: "It's cold, wear warm clothes!" """

Temperature=int(input('Enter the temperature:'))
print(f'Tmperature:{Temperature}°C')
if Temperature>30:
    print("It's hot, stay hydrated!") 
elif Temperature>=15 and Temperature<=30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear wear warm clothes!")