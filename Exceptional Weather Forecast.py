#Task 1: Begin by asking the user to enter the temperature in Fahrenheit 
#set up a variable that will be used for user input and initiate the following while loop
temp_input = input("What is the temperature in Fahrenheit? ")

#Task 2: Temperature Conversion
#define a function that will take in our temperature variable and convert it into celsius
def Celsius_Conversion(temperature):
    temp_in_celsius = (temperature - 32) * (5/9)
    temp_in_celsius = round(temp_in_celsius, 1)

    return temp_in_celsius

#convert the user input inside a try block to test for non-digit input
try:
    #convert the input to a float
    temp_input = float(temp_input)
#if the user input are non-digits, prompt the user to use numbers only
except (ValueError):
    print("Please use numbers only.")
#Task 3: User Experience
#if the user input is in a numbered format, use the celsius conversion function to convert the user input to celsius
else:
    print("The tempurature in celsius is", end = " ")
    print(Celsius_Conversion(temp_input), end = " ")
    print("degrees.")
#Task 4: Add a 'finally' block that thanks the user for using the forecast application
#Thank the user for using the application regardless of whether or not the exception was raised
finally:
    print("Thank you for using our weather conversion app!")