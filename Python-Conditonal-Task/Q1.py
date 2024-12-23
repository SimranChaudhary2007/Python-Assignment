"""Take the price of an item as input. If the price is more than 1000, apply a 10% discount. Otherwise, check if the price is more than 500 and apply a 5% discount.
Print the final price."""

price=int(input('Enter thr price of item:'))
if price>=1000:
    print('Discount:10%')
    discount_amount=10/100*price
    print(F'Discount amount:{discount_amount}')
    final_price=price-discount_amount
    print(F'Finalprice:{final_price}')
elif price>=500:
    print('Discount:5%')
    discount_amount=5/100*price
    print(F'Discount amount:{discount_amount}')
    final_price=price-discount_amount
    print(F'Finalprice:{final_price}')
else:
    print('No discount')