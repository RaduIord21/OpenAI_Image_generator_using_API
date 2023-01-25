import openai

from key import key
from WriteJson import WriteJson

openai.api_key = key
openai.organization = "org-ifAS8guKPb96SIApGtNAy6Y1"

header = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {key}'
}

#codul incepe de aici


#pana aici
while True:
    prompt = input("Alegeti ce vreti sa vedeti ")
    image = openai.Image.create(
        prompt=prompt,
        n=10,
        size="1024x1024"
    )
    json_file = openai.Model.list()
    WriteJson(image)

    for i in range(10):
        print(image["data"][i]["url"] + "\n")
    if(not input("Continue ?").lower().startswith("y")):
        break


