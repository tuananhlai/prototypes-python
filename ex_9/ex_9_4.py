class OopsException(Exception):
    pass
try:
    raise OopsException()
except OopsException:
    print('Caugh an oops')