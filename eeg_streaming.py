from muselsl import stream, list_muses, record
#import pywhatkit

muses = list_muses()
print(len(muses))

for key, value in muses[0].items():
    print(key, ' : ', value)

stream(muses[0]['address'])

