import requests
import json
import os

CLOUDRUN_TARGET = os.environ['CLOUDRUN_TARGET']

payload = {'text' : 'I’d like to be a shrine, so I can learn from peoples’ prayers the story of hearts. I’d like to be a scarf so I can place it over my hair and understand other worlds. I’d like to be the voice of a soprano singer so I can move through all borders and see them vanish with every spell-­binding note. I’d like to be light so I illuminate the dark. I’d like to be water to fill bodies so we can gently float together indefinitely. I’d like to be a lemon, to be zest all the time, or an olive tree to shimmer silver on the earth. Most of all, I’d like to be a poem, to reach your heart and stay.'}
r = requests.post(CLOUDRUN_TARGET + "/emotion", json = payload)

print(r.text)