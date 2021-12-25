import platform
import multiprocessing

print('uname:', platform.uname())
print('system   :', platform.system())
print('node     :', platform.node())
print('release  :', platform.release())
print('version  :', platform.version())
print('machine  :', platform.machine())
print('processor:', platform.processor())

print('No Of Thread:', multiprocessing.cpu_count())
