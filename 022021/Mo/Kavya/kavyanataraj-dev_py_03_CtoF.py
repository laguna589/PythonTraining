#Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

Celsius = int(input("Enter a temp in Celsius(integers only): ")) # input() is used take user input & int is used so that Celsius value(string) entered by user is converted to int and can be multiplied by 9/5
Farenheit = ((9/5)*Celsius)+32 #formula used for converting celsius to farneheit
print("Temp in Farenheit", Farenheit) #final output
