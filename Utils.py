def get_code(message):
    while True:
        code = input(message).strip().upper()
        if code.isalpha():
            if len(code) == 2:
                return code
            else:
                print("Enter a two-letter country code.")
        else:
            print("Countries's code can only be in letters.")
