# For each click variable, calculate the temperature and print it as shown
# in the instructions

thermo_0 = 40      # The 'zero' point on the thermostat is 40 degrees
thermo_range = 50  # The thermostat measures 50 degrees above the zero point

click_1 = 0

temp_1 = thermo_0 + click_1 % thermo_range   # calculate the temperature
print('The temperature is ' + str(temp_1))   # report it back to the user

click_2 = 49

temp_2 = thermo_0 + click_2 % thermo_range   # calculate the temperature
print('The temperature is ' + str(temp_2))   # report it back to the user

click_3 = 74

temp_3 = thermo_0 + click_3 % thermo_range   # calculate the temperature
print('The temperature is ' + str(temp_3))   # report it back to the user

click_4 = 51

temp_4 = thermo_0 + click_4 % thermo_range   # calculate the temperature
print('The temperature is ' + str(temp_4))   # report it back to the user

click_5 = -1

temp_5 = thermo_0 + click_5 % thermo_range   # calculate the temperature
print('The temperature is ' + str(temp_5))   # report it back to the user

click_6 = 200

temp_6 = thermo_0 + click_6 % thermo_range   # calculate the temperature
print('The temperature is ' + str(temp_6))   # report it back to the user
