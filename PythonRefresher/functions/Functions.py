"""
Functions

"""

def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate

"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""

def user_dictionary(firstname, lastname, age):
    #1. strip khoảng trắng hai đầu 
    firstname = firstname.strip()
    lastname = lastname.strip()

    #2. age phải là số nguyên và >= 0
    if not isinstance(age, int) or age < 0:
        raise ValueError ("age phai la so nguyen int va lon hon 0")
    create_user_dictionary = {
        "firstname":firstname,
        "lastname" :lastname,
        "full name": firstname + " " + lastname,
        "age"      : age,
        "is_adult": age >= 18
    }
    return create_user_dictionary

solution_dictionary = user_dictionary(firstname= "Hieu    ", lastname="Nguyen", age= 1)    
print(solution_dictionary)

# final_cost = buy_item(50)
# print(final_cost)

# # def my_function(*kids): # dấu * như 1 tuple khi không chắc trong tương lai sẽ truyền bao nhiêu tham số → dùng * để nhận “bao nhiêu cũng được”.
# #   print("The youngest child is " + kids[2])

# # my_function("Emil", "Tobias", )

# def log(*items):
#     # ghép lại thành 1 dòng log
#     line = " | ".join(str(i) for i in items)
#     print(line)

# log("user_id=10", "action=click", "page=home")
# log("user_id=10", "action=scroll")
