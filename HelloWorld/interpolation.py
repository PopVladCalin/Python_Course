# PY 2 String Interpolation
age = 24
print("My age is %d years" % age)   # %d will be replaced by on integer value that's provided after the string
                                    # following another %


major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))    # all% will be changed with
print("Pi is approximately %f" % (22/7))                    # floating point results
print("Pi is approximately %60.50f" % (22/7))               # floating point results

# could be also % d (dec), s (string), f (float), x (hexa), o (octo), e (scientific notification)