import json

# Opening JSON file
f = open('unicode-emoji.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
tsWrite = []
for i in data['emojis']:
    upperCasedName = i['description'].upper().replace(" ", "_")
    tsWrite.append("export const %s = '%s';\n" % (upperCasedName, i['emoji']))

wf = open('emojis.consts.ts', 'w')
wf.writelines([str(i) for i in tsWrite])
# print(tsWrite[0])
# wf.writelines(tsWrite)

# filehandle.writelines("%s\n" % place for place in places_list)
#     fileHandle.writelines("%s\n" % place for place in tsWrite)

# with open('emojis.consts.ts', 'w') as fileHandle:
#     fileHandle.writelines("%s\n" % place for place in tsWrite)


# Closing file
f.close()
wf.close()
