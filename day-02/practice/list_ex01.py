a = [100, 200, 5.0, True] # LIST banane ka 1st tarika

print(type(a))
a.append(500)
print(a)

clouds = list () # LIST banane ka 2nd tarika
print(type(clouds))

clouds.append ("aws")
clouds.append ("azure")
clouds.append ("gcp")
clouds.append ("ibm")
clouds.append ("alibaba")
clouds.append ("utho")
print(clouds)
print("Length of list is:", len(clouds))
print("The leader for cloud service provider is:", clouds[0])
print("Indian cloud service provider is:", clouds[-1])

print(dir(clouds))
print(clouds.extend.__doc__)

# [aws, azure, gcp, ibm, alibaba, utho]
# range 0, 1, 2, 3, 4

# iterate list
for cloud in clouds:
    if cloud == "aws":
        print(f"{cloud} Market Leader + covered in course")
    elif cloud == "utho":
        print(f"{cloud} Indian cloud")
    elif cloud == "azure" or cloud == "gcp":
        print(f"{cloud} Devops - Zero to Hero me wo bhi cover kara dunga")
    else:
        print(f"{cloud} baaki nahi honge")
