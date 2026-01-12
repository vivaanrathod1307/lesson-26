s1=[1,2,3]
s2=[4,5,6]
s3=list(zip(s1,s2))
s4=dict(zip(s1,s2))
print(s3,s4)
s5=list(zip(s1,s2[::-1]))
print(s5)