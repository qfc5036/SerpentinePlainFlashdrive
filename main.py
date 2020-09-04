# Author: Qiaoxu Cui qfc5036@psu.edu
# Collaborator: Zhili Bu zjh5625@psu.edu
# Collaborator: Shufang Huang sbh5655@psu.edu
# Collaborator: Isabel Vera ikv5018@psu.edu
temperature = input("Enter temperature: ")
temperature = float(temperature)
unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  Celsius = float((temperature - 32 )/1.8)
  print(f"{str(temperature)}{chr(176)} in Fahrenheit is equivalent to {str(Celsius)}{chr(176)} Celsius.")
elif unit == "C" or unit == "c":
  Fahrenheit = float((temperature *1.8 + 32))
  print(f"{str(temperature)}{chr(176)} in Celsius is equivalent to {str(Fahrenheit)}{chr(176)} Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")