import base64

encrypted = input("Encrypted message:")
username = input("username")
MESSAGE = '''
EUYQGhMMSx0cU0FIU1MCFAQPG01NQ0gTAEICChUGBxZTRVxBSQoZFQYKHQpKSUNURhcVEgoUFR1I
SltDSBkBTRwKEAgQHxFCSkFJDgkJCgoGCkMLAQBGUklUQhMPAgAJCgYLV0MOSR0VAxAaABZBQVRP
TRICCRVIAk5IEg4dVFRfRkYZBgRARBI=
'''

KEY = 'jacopo.notarstefano'
#KEY = username
decoded = base64.b64decode(encrypted)


result = []
for i, c in enumerate(decoded):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))


print(''.join(result))
