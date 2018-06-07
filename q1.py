'''
Q.1- Extract the user id, domain name and suffix from the following email addresses.
emails = "zuck26@facebook.com" "page33@google.com"
"jeff42@amazon.com"
desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]
'''
import re
emails=["zuck26@facebook.com","page33@google.com","jeff42@amazon.com"]
desired_outputs=[]

for i in range(len(emails)):
    l = re.split('\W',emails[i])
    desired_outputs.append(l)

print(desired_outputs)
