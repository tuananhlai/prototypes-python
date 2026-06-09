# Mini Project: Password Policy Checker

In this project, you will build a command-line tool that checks whether a password meets a set of security rules.

## Rules to implement

1. At least 8 characters long
2. Contains at least one lower-case letter
3. Contains at least one upper-case letter
4. Contains at least one numeric character (0–9)
5. Contains at least one special character (anything that is not a letter or digit)
6. Is not one of the top 10 most common passwords:
   `123456`, `123456789`, `111111`, `password`, `qwerty`,
   `abc123`, `12345678`, `password1`, `1234567`, `123123`

## Your tasks

- Complete each of the checker functions in `password_policy_checker.py` so they return `True` when the password satisfies the rule, and `False` otherwise.
- Run the script from the terminal to test your work:
  ```
  python3 password_policy_checker.py <password>
  ```
- Try a weak password like `password` and a strong one like `Tr0ub4dor&3` to verify the output looks correct.

## Expected output

A strong password — passes all rules:

```
$ python3 password_policy_checker.py Tr0ub4dor&3
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters
✅ Contains special characters
✅ Is not common
```

A common password — fails multiple rules:

```
$ python3 password_policy_checker.py password
✅ Has 8 or more characters
✅ Contains lower-case characters
❌ Contains upper-case characters
❌ Contains numeric characters
❌ Contains special characters
❌ Is not common
```

A short password — fails on length and more:

```
$ python3 password_policy_checker.py Hi5!
❌ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters
✅ Contains special characters
✅ Is not common
```

Almost there — missing only a special character:

```
$ python3 password_policy_checker.py MyPassword1
✅ Has 8 or more characters
✅ Contains lower-case characters
✅ Contains upper-case characters
✅ Contains numeric characters
❌ Contains special characters
✅ Is not common
```

## Hints

- A special character is any character that is **not** upper-case, lower-case, or numeric.
