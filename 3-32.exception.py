l = [1, 2, 3]
i = 5

try:
    l[i]
except:
    print("Don't worry")

print("keep proccessing")
"""
Don't worry
keep proccessing
"""


try:
    l[i]
except IndexError:
    print("IndexError catch")

print("keep proccessing 2")
"""
IndexError catch
keep proccessing 2
"""


try:
    l[i]
except IndexError as exc:
    print("IndexError catch: {}".format(exc))

print("keep proccessing 3")
"""
IndexError catch: list index out of range
keep proccessing 3
"""


del l

try:
    l[i]
except IndexError as ex:
    print('Error: {}'.format(ex))
except NameError as ex:
    print('Error: {}'.format(ex))

print("keep proccessing 4")
"""
Error: name 'l' is not defined
keep proccessing 4
"""

l = [1, 2]

try:
    () + l
except IndexError as ex:
    print('Error: {}'.format(ex))
except NameError as ex:
    print('Error: {}'.format(ex))
except Exception as ex:
    print('Other Error: {}'.format(ex))
finally:
    print('clean up')

print("keep proccessing 5")
"""
Other Error: can only concatenate tuple (not "list") to tuple
clean up
keep proccessing 5
"""


try:
    l[1]
except IndexError as ex:
    print('Error: {}'.format(ex))
except NameError as ex:
    print('Error: {}'.format(ex))
except Exception as ex:
    print('Other Error: {}'.format(ex))
else:
    print('done')
finally:
    print('clean up')

print("keep proccessing 6")
"""
done
clean up
keep proccessing 6
"""
