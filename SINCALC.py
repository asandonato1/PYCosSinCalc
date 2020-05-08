import math

#angle B = x, angle A = y, revert later in code tho. in this case, we have a very simple calculator that just calculates de sin cos tan of x and applies them to Y, read later in code.

hp = input("Hypotenuse = ")
co = input("Oposing side = ")
ca = input("Adjacente side = ")
cosX = (int(ca) / int(hp)) 
sinX = (int(co) / int(hp))
tgX = (int(co) / int(ca))

cosY = sinX #here, instead of calculating the cosY itself, just applied sinX = cosY
sinY = cosX #the same thing
tgY = tgX ** -1 #in this case, the tg is just equal to tgX^-1, see the fraction for the result

print(hp)
print(co)
print(ca)
answer = None
while answer not in ("yes", "no"):
    answer = input("Are these sides correct? Answer yes or no: ")
    if answer == "yes":
        print(cosX, sinX, tgX)
        print(cosY, sinY, tgY)

    elif answer =="no":
        quit

    else:
        print("Please enter yes or no")
#ezpz
