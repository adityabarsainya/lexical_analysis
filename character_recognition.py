from textblob import TextBlob


def char_rec(filename):
    file=open(filename,"r")
    lines=file.readlines()

    characters=[]
    for l in lines:
        obj=TextBlob(l)
        for i in obj.tags:
            if('NNP' in obj.tags):
                characters.append(obj.tags[0])

    return characters
