"""Accept any city from the user and display monument of that city.
City        Monument
Delhi       Red Fort
Agra        Taj Mahal
Jaipur      Jal Mahal  """

city=input('Enter name of city:')
if city=='Delhi':
    print('Monument:Red Fort')
elif city=='Agra':
    print('Monument:Taj Mahal')
elif city=='Jaipur':
    print('Monument:Jal Mahal')
else:
    print('Invalid input')