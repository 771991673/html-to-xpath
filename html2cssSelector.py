import re

htmlString = '''
<html>
<head>
<title>Try jsoup</title>
</head>
<body>
'''


allTagsReg ='<\w[^>]*>|</\w[^>]*>'
allTagsMatch = re.findall(allTagsReg, htmlString)

if allTagsMatch:
    tags = [str(tag) for tag in allTagsMatch]
else:
    print("not tags found")

tagArray = []

for t in tags:
    if '/' not in t:
        tagArray.append(t)
    else:
        del tagArray[-1]




tagArray = [t[1:-1] for t in tagArray]

xPath = "/"+"/".join(tagArray)

print(xPath)