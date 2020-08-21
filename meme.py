import requests
import os

def make_meme(top, bottom):
    url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"

    querystring = {"font":"Impact","font_size":"50","meme":"Condescending-Wonka","top":top,"bottom":bottom}

    headers = {
        'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com",
        'x-rapidapi-key': "5281cdbcb4msh2e671f652caacf7p16818cjsn3100f2cd4310"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    path = 'static/'
    filename = str(hash(response.content)) + '.jpg'
    try:
        f = open(os.path.join(path + filename), "wb")
        f.write(response.content)
        f.close()
    # if memes folder has been deleted, make it again
    except FileNotFoundError:
        os.mkdir(path)
        f = open(os.path.join(path + filename), "wb")
        f.write(response.content)
        f.close()
    return filename
