import rsa 

public_key ,private_key = rsa.newkeys(1024)

with open("public_key.pem","wb") as f :
    f.write(public_key.save_pkcs1("PEM"))
    
with open("private_key.pem","wb") as f :
    f.write(private_key.save_pkcs1("PEM"))
    
