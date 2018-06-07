'''
Q.1- Clean up the following tweet so that it contains only the user's message.
That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
tweet = Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats
desired_output = 'Good advice What I would do differently if I was learning to code today'

'''

import re
tweet= "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
desired_output = "Good advice What I would do differently if I was learning to code today"

print("Tweet:\n",tweet)
print('Desired Output:\n',desired_output)

#removing URLs
s=re.sub('http[\S]*','',tweet)

#removing hashtags
s=re.sub('#[\w]*','',s)

#removing mentions
s=re.sub('@[\w]*','',s)

#removing puntuations
s=re.sub('[,.;:\'!?]','',s)

#removing RTs
s=re.sub('RT','',s)

#removing CCs
s=re.sub('cc','',s)
s=re.sub('CC','',s)



l= re.split(' ',s)


result=''
for i in range(len(l)):
    if l[i]!='':
        result+=l[i]+' '
                   


print("Output:\n",result)
