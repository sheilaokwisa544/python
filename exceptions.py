try: # for testing out errors
    x = 10
    print(x)
except:
    print("an error occurred")

finally:
    print("success")

try:
    num1 = 67
    num2 = 0
    print(num1 / num2)
except:
    print("zero division error occurred")

