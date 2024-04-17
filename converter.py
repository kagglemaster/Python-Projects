with open("currencyrates.txt") as f:
    lines =f.readlines()

amount = int(input("Enter the amount in PKR to convert: "))
dic = {}
for line in lines:
    words = line.split()
    combine = ' '.join(words[:2])
    num = words[-1] 
    result_list = [combine, num]
    print(result_list[0])
    dic.update({result_list[0]:result_list[1]})


currency = input("Please enter the country for currency conversion:\n").title()
try:
    print(f"PKR {amount} is {round(amount*float(dic[currency]),2)} {currency}")
except KeyError:
    print("Error: Currency not found in the conversion rates file.")
