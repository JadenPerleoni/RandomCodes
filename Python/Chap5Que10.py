rate = int(input("Enter rate for first year as whole number:"))
rate = (rate/100)
tuition = 20000


for x in range (10):
    
    tuition = (tuition+ (tuition*(rate)))
    rate = (rate + (rate*.5))
    print(f"The tuition for this year is {tuition}")
