
s = 'hello'
d = {}
#f = open('123.txt')
try:
    1/0
except (KeyError, IndexError):
    print('LookupError')
except ZeroDivisionError:
    print('ZeroDivisionError')
else:
    print('Good')
# except LookupError:
#     print('error LookupError')
# except KeyError:
#     print('error KeyError')
# except ValueError:
#     print('error ValuerError')
# except ZeroDivisionError:
#     print('error ZeroDivisionError')

finally:
    print('end')
