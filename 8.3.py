def password_check(passcheck):

    countNum = 0
    if len(passcheck) >= 8:
        if passcheck.isalnum():
            for i in range(len(passcheck)):
                if 48 <= ord(passcheck[i]) <= 57:
                    countNum += 1
            if countNum >= 2:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def main():
    password = input("Enter the password:").strip()

    result = password_check(password)

    if result:
        print("It's a valid password")
    else:
        print("Not a valid password")


main()