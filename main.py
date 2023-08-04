from checking_password import Checking
from generating_password import generate_password


p = generate_password(8,True,True,True,True)

cp = Checking(p)

print(p)
# print(cp.get_detailes())
# print(cp.get_result())


if __name__ == '__main__':
    pass