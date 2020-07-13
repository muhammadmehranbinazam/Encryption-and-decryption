#!/usr/bin/python
class Solution:
    def __init__(self):
        self.key = ''
        self.plainText = ''
        self.decry=[]
        self.string=[]
        self.ci_key=[]
    def decrypt(self, cipherText):
        # //write your logic to decrypt the given cipherText
        #dictionary 
        keys={'a':'a', 'b':'z','c':'e','d':'r','e':'t','f':'y','g':'u','h':'i','i':'o','j':'p','k':'q','l':'s','m':'d',
        'n':'f','o':'g','p':'h','q':'j','r':'k','s':'l','t':'m','u':'w','v':'x','w':'c','x':'v','y':'b','z':'n',' ':' '}
        # hello
        for char in cipherText:
            self.ci_key.append(keys[char])
        self.key=''.join(self.ci_key)
        # // store recovered key to private member key
        # // store plain text to plainText member
        # this loop iterate through each character and append in the list
        for i in cipherText:
            self.string.append(i)
        # this loop iterate through string list and match each item with string list
        for i in self.string:
            for x,y in keys.items():
                if y==i:
                    self.decry.append(x)
        self.plainText=''.join(self.decry)
            
       
    # this method encrypt text and return key
    def getKey(self):
        return self.key
    #this method will decrypt out key and return plan text
    def getPlainText(self):
        return self.plainText
obj=Solution()
obj.decrypt("this is a cyber security course")
print(obj.getKey())
# print(obj.getPlainText())


