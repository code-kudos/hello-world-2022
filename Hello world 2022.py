# Hi, I'm code kudos, Are you Bored of Traditional Hello World.
## Try this new way to print message of your choice
### Hope you like it!!!!
#### To see more like this Subscribe to 
##### Youtube: @codekudos
###### Instagram: @codekudos
####### Twitter: @code_kudos

import random
import time

target = 'hello world'
alphabet = list('abcdefghijklmnopqrsuvwxyz ')
word=''

for i in range(0,len(target)):
    while(target!=word):
        x = random.randint(0,len(alphabet)-1)
        word = word+alphabet[x]
        print(word)
        time.sleep(0.15)
        if(target[i]!=word[i]):
            word = word[:-1]
        elif(target[i]==word[i]):
            break