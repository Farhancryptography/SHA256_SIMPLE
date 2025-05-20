import numpy
import hashlib 
a = str(input (""))

yourpassword  = a

sha256_hash = hashlib.sha256()


hashed_valued =  sha256_hash.hexdigest()

sha256_hash.update(yourpassword.encode("utf-8"))
print("Its ready to use you'r encrypted pass for your app", hashed_valued)