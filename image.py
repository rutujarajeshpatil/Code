#read image and write new image

f1=open("ganesh.jpg","rb")
f2=open("newganesh.jpg","wb")
bytes=f1.read()
f2.write(bytes)
print(bytes)
print("New image is available")