ab = {
    'Rivers': 'rivers@lau.com',
    'Tsing': 'tsing_hua@ma.com',
    'Python': 'byte-of-python@python.com',
    'Java': 'core_java@java.com'
}

print("Python's address is", ab['Python'])
del ab['Tsing']

print('\nThere are {} contacts in the address book'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

ab['Go'] = 'go@go.com'
if 'Go' in ab:
    print("\nGo's address is", ab['Go'])
