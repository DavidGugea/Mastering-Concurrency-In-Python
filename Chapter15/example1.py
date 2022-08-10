import sys

print("Reference count when direct-referencing: {0}".format(sys.getrefcount([7])))

a = [7]
print("Reference count when reference once: {0}".format(sys.getrefcount(a)))

b = a
print("Reference count when reference twice: {0}".format(sys.getrefcount(a)))

a[0] = 8
print("Variable a after a is changed: {0}".format(a))
print("Variable b after a is changed: {0}".format(b))

print("Finished.")
