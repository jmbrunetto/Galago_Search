#TODO
# Read a XML file - Done
# Extract number, title and text - Done
# Tokenizer the query
# Remove Stopwords - Done
# Remove duplicates - Not Needed


import xml.dom.minidom as minidom
from nltk.corpus import stopwords

# You will have to download the set of stop words the first time
import nltk
nltk.download('stopwords')

# Load stop words
stop_words = stopwords.words('spanish')

title = []
final = []
queryDict = {"number": 0, "text": ""}

doc = minidom.parse('/home/brunetto/PycharmProjects/Galago_Search/queries/Topicos_UTF8.xml')

for element in doc.childNodes:
    for query in element.getElementsByTagName('top'):
        queryModificada = []
        queryNumber = query.getElementsByTagName('num')[0].childNodes[0].data.lower()
        queryText = query.getElementsByTagName('desc')[0].childNodes[0].data.lower()
        queryTitle = query.getElementsByTagName('title')[0].childNodes[0].data.lower()
        queryModificada.append(queryNumber.split(' '))
        queryModificada.extend(queryTitle.split(' '))
        queryModificada.extend(queryText.split(' '))

        for word in queryModificada:
            if word not in stop_words:
                if isinstance(word, list):
                    for item in word:
                        if len(item) > 0:
                            title.append(item)
                            queryDict["number"] = item
                else:
                    if len(word) > 0:
                        title.append(word)
                        queryDict["text"] = queryDict["text"]+' '+ word
        final.append(queryDict)
        queryDict = {"number": 0, "text": ""}

print(final)




