import re

regex_phone_pattern = r"\+\d{1,3}-\d{2}-\d{5,7}"
regex_compiled = re.compile(regex_phone_pattern)


def test_valid_phone_numbers(regex_compiled):
    valid = (
        "+375-29-7776655",
        "+37-29-7776655",
        "+3-29-7776655",
        "+375-44-777665",
        "+375-44-77766",
    )
    for n in valid:
        res = regex_compiled.fullmatch(n)
        if res:
            print(f"The phone number {n} is valid \n")
        else:
            print(f"The phone number {n} is not valid")


def test_invalid_phone_numbers(regex_compiled):
    invalid = (
        "",
        "test12345test"
        "375-29-7776655",
        "+-29-7776655",
        "+3a5-29-7776655",
        "+3756-29-7776655",
        "+375--7776655",
        "+375-4-7776655",
        "+375-444-7776655",
        "+375-c4-7776655",
        "+375-33-",
        "+375-33-7",
        "+375-33-7776",
        "+375-33-77766554",
        "+375-29-7776e55",
    )

    for n2 in invalid:
        res = regex_compiled.fullmatch(n2)
        if res:
            print(f"The phone number {n2} is valid")
        else:
            print(f"The phone number {n2} is not valid \n")


test_valid_phone_numbers(regex_compiled)
test_invalid_phone_numbers(regex_compiled)
