import turtle as t
# alg workebnch ch3

# 1.
x = 105
if x > 100:
    y = 20
    z = 40

# 2.
a = 9
if a < 10:
    b = 0
    c = 1

# 3. 
if a < 10:
   b = 0
else:
    b = 99

# 4.
score = 91
A_score = 90
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')


# 5.
amount1 = 11
amount2 = 12
if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print(amount1)
    elif amount2 > amount1:
        print(amount2)
    else:
        print("they are the same amount")

# 6.
speed = 57
if speed in range(24, 57):
    print("speed is normal")
else:
    print("speed is abnormal")


# 7.
points = 8
if points not in range(9, 52):
    print("invalid points")
else:
    print("valid points")

# 8. 
heading = t.pos()
print(heading)