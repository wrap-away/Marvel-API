import os
import pytest
from marvel import Marvel

PUB_KEY = os.environ.get("PUB_KEY")
PRIV_KEY = os.environ.get("PRIV_KEY")

m = Marvel(PUB_KEY, PRIV_KEY)

def test_characters():
    character = m.characters.get(1009610)

    name = character['data']['results'][0]['name']
    comics = character['data']['results'][0]['comics']
    series = character['data']['results'][0]['series']
    events = character['data']['results'][0]['events']
    stories = character['data']['results'][0]['stories']
    assert name == "Spider-Man"
    assert type(comics) is dict
    assert type(series) is dict
    assert type(events) is dict
    assert type(stories) is dict

def test_comics():
    comic = m.comics.get(62304)

    title = comic['data']['results'][0]['title']
    comic_format = comic['data']['results'][0]['format']
    assert title == "Spider-Man: 101 Ways to End the Clone Saga (1997) #1"
    assert comic_format == "Comic"