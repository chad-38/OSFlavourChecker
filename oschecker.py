import platform

print ('Version      :', platform.python_version())
print ('Version tuple:', platform.python_version_tuple())
print ('Compiler     :', platform.python_compiler())
print ('Build        :', platform.python_build())


print ('Normal :', platform.platform())
print ('Aliased:', platform.platform(aliased=True))
print ('Terse  :', platform.platform(terse=True))


if "Windows" in platform.platform():
    print("Windows System")
elif "redhat" in platform.platform():
    print("Redhat System")
elif "ubuntu" in platform.platform():
    print("Ubuntu system")
