from confi import *
from home import *
from orderby import *
from cart import *
from order import *
from product import *
from filter import *
from login import *

'''TC_001: Verify Visibility of Company Logo on Home Page'''
logo_visible()

'''TC_006: Verify Total number of products on Home Page'''
count_total_number_of_products_on_home_page()

'''TC_009: Verify filter product by Brand (Samsung) and validate'''
filter_samsung_products_and_validate()

'''TC_014: verify visibility of Order by section'''
order_by_is_visible()

'''TC_016: verify items in Low to High order'''
order_items_from_low_to_high()

'''TC_017: verify items in High to Low order'''
order_items_from_high_to_low()

'''TC_020: Verify signin functionality with invalid credentials'''
signin_with_invalid_credentials()

'''TC_021: Verify signin functionality with invalid username and valid password'''
signin_with_invalid_username_valid_password()

'''TC_022: Verify signin functionality with valid username and invalid password'''
signin_with_valid_username_invalid_password()

'''TC_024: Verify signin functionality with both valid credentials'''
signin_with_valid_credentials()

'''TC_025: Verify item is added to cart'''
add_item_to_cart()

'''TC_026: Verify adding same item to cart'''
increase_same_item()


'''TC_027: Verify removing same item from cart'''
decrease_same_item()

'''TC_035: Verify Price Updates When Increasing Quantity of the Same Product in Cart'''
price_calculation()

'''TC_037: verify the visibility and clickability of Orders section'''
Orders_is_clickable_on_nav_menu()

'''TC_055: Verify adding product  to favoutites'''
verify_fav_functionality()


'''
scenario:
1.Add product to cart and validate whether same product is added or not
2.Validate same product is shown on checkout page.
3.From fill up (First name, Last name, Address, State/Province, Postal Code) on Checkout page
4.Successfull Statement Validation
5.After successfull order, check whether same item is shown on order history
'''
successfully_order_single_product_and_verify_on_order_page()

'''TC_057: verify copyright section'''
verify_copyright()
