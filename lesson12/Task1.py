import re

user_phone = "+375-29-7776655"

regex_phone_pattern = r"(\++[\d]{1,3})-([\d]{2})-([\d]{5,7})"

regex_phone = re.compile(regex_phone_pattern)


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
        assert res.group() == n


result = re.fullmatch(user_phone)

print(result)
