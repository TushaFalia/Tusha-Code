
# Final assingnment 1 encrypt :

def encrypt(x,y):
    
    l=''

    for i in range(len(x)):
        b= ord(x[i])+y
        d=(chr(b))
        l+=d
    return l
    #print('Cipher:',l)
    

if __name__ == '__main__':

    a= input("Please Enter the Text:")
    c= int(input("Please Enter The Key Number:"))
    print("Cipher:" ,(encrypt(a,c)))
    #encrypt(a,c)


# Final assingnment 1 decrypt :

def decrypt(x,y):

    l=''

    for i in range(len(x)):
        b= ord(x[i])-y
        d=(chr(b))
        l+=d
    return l
    #print('Decipher:',l)


if __name__ == '__main__':

    a= input("Please Enter the Encrypt Text:")
    c= int(input("Please Enter The Key Number:"))
    print("Decipher:" ,(decrypt(a,c)))
    #decrypt(a,c)