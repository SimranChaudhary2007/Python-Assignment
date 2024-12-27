"""Accept the price of an item from the user:
If the price is greater than 1000, apply a 20% discount and print the new price.
If between 500 and 1000, apply a 10% discount.
If less than 500, no discount."""

price=int(input("Enter the price of food:"))
if price>1000:
    print('Discount:20%')
    discount_amount=20/100*price
    new_price=price-discount_amount
    print(F'New price:{new_price}')
elif 500<= price <=1000:
    print('Discount:10%')
    discount_amount=10/100*price
    new_price=price-discount_amount
    print(F'New price:{new_price}')
else:
    print("No discount")