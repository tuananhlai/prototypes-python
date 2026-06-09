import sys

MIN_CHAR = 8


def is_long_enough(p: str) -> bool:
    return len(p) >= MIN_CHAR


def contain_upper_case(p: str) -> bool:
    for c in p:
        if c.isupper():
            return True
    return False


def contain_lower_case(p: str) -> bool:
    for c in p:
        if c.islower():
            return True
    return False


def contain_numeric(p: str) -> bool:
    for c in p:
        if c.isnumeric():
            return True
    return False


def contain_special(p: str) -> bool:
    """
    Returns true if the given string contains a non-alphanumeric character.
    """
    for c in p:
        if not (c.isnumeric() or c.isupper() or c.islower()):
            return True
    return False


top_10_common_passwords = {
    "123456",
    "123456789",
    "111111",
    "password",
    "qwerty",
    "abc123",
    "12345678",
    "password1",
    "1234567",
    "123123",
}


def is_common(p: str) -> bool:
    return p in top_10_common_passwords


def format_bool(v: bool) -> str:
    return "✅" if v else "❌"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 password_policy_checker.py <password>")
        exit(1)

    password = sys.argv[1]
    print(f"{format_bool(is_long_enough(password))} Has 8 or more characters")
    print(
        f"{format_bool(contain_lower_case(password))} Contains lower-case characters"
    )
    print(
        f"{format_bool(contain_upper_case(password))} Contains upper-case characters"
    )
    print(f"{format_bool(contain_numeric(password))} Contains numeric characters")
    print(f"{format_bool(contain_special(password))} Contains special characters")
    print(f"{format_bool(not is_common(password))} Is not common")
