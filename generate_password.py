import random
import string


def generate_password(length):
    if length < 4:
        return "Your password is too short. It must be at least 4 characters long. "

    # حروف کوچک، بزرگ، اعداد و نمادها
    letters = string.ascii_lowercase  # a-z
    letters1 = string.ascii_uppercase  # A-Z
    digits = string.digits  # 0-9
    symbols = string.punctuation  # !@#$%^&*()_+...

    # ترکیب همه موارد
    all = letters + digits + symbols + letters1

    # ساخت رمز با انتخاب تصادفی
    password = "".join(random.choice(all) for _ in range(length))
    return password


# گرفتن طول رمز از کاربر
try:
    user_length = int(input("How many characters are in your password? "))
    result = generate_password(user_length)
    print(f"your password: (  {result}  )")
except ValueError:
    print("pleace enter just number")
