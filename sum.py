# Edit the code below

theSum = 0.0
theAve = 0.0
count = 1
data = input("Enter a number: ")
while data != "":
    number = float(data)
    theSum += number
    count += count
    theAve = theSum / count
    data = input("Enter the next number: ")
print("The sum is", theSum)
print("the average is", theAve)
