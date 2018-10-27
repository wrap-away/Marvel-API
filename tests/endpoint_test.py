import os
import pytest
from marvel import Marvel
from marvel.exceptions import MarvelException

@pytest.fixture
def marvel():
    PUB_KEY = os.environ.get("PUB_KEY")
    PRIV_KEY = os.environ.get("PRIV_KEY")
    return Marvel(PUB_KEY, PRIV_KEY)

def test_characters(marvel):
    with pytest.raises(MarvelException):
        marvel.characters.all(just_some_bad_param="Iron Man")
        marvel.characters.get("")
        marvel.characters.get("♤🎅  xςא  😾🍪")
        marvel.characters.comics("XYZ")
        marvel.characters.events("")
        marvel.characters.series("")
        marvel.characters.stories("")

    character = marvel.characters.get(1009610)

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

def test_comics(marvel):
    with pytest.raises(MarvelException):
        marvel.comics.all(just_some_bad_param="The Incredible Hulk")
        marvel.comics.get("")
        marvel.comics.get("♤🎅  xςא  😾🍪")
        marvel.comics.characters("XYZ")
        marvel.comcis.events("")
        marvel.comics.creators("")
        marvel.comics.stories("")

    comic = marvel.comics.get(62304)

    title = comic['data']['results'][0]['title']
    comic_format = comic['data']['results'][0]['format']
    assert title == "Spider-Man: 101 Ways to End the Clone Saga (1997) #1"
    assert comic_format == "Comic"

def test_creators(marvel):
    with pytest.raises(MarvelException):
        marvel.creators.all(just_some_bad_param="Stan Lee")
        marvel.creators.get("Stan the Man Lee")
        marvel.creators.get("♤🎅  xςא  😾🍪")
        marvel.creators.comics("XYZ")
        marvel.creators.events("")
        marvel.creators.series("")
        marvel.creators.stories("")

    creator = marvel.creators.all(firstName="Stan", lastName="Lee")

    fullName = creator['data']['results'][0]['fullName']
    comics = creator['data']['results'][0]['comics']
    series = creator['data']['results'][0]['series']
    events = creator['data']['results'][0]['events']
    stories = creator['data']['results'][0]['stories']
    assert fullName == "Stan Lee"
    assert type(comics) is dict
    assert type(series) is dict
    assert type(events) is dict
    assert type(stories) is dict

def test_events(marvel):
    with pytest.raises(MarvelException):
        marvel.events.all(brrp="Infinity")
    
    event = marvel.events.all(name="Infinity")
    name = event['data']['results'][0]['title']
    comic_id = event['data']['results'][0]['id']
    comics = event['data']['results'][0]['comics']
    series = event['data']['results'][0]['series']
    characters = event['data']['results'][0]['characters']
    stories = event['data']['results'][0]['stories']
    creators = event['data']['results'][0]['creators']
    assert name == "Infinity"
    assert comic_id == 315
    assert type(comics) is dict
    assert type(series) is dict
    assert type(characters) is dict
    assert type(stories) is dict
    assert type(creators) is dict


def test_series(marvel):
    with pytest.raises(MarvelException):
        marvel.series.all(blah_blah="Incrudulous Hork")
    
    series = marvel.series.get(18454)

    title = series['data']['results'][0]['title']
    comics = series['data']['results'][0]['comics']
    events = series['data']['results'][0]['events']
    characters = series['data']['results'][0]['characters']
    stories = series['data']['results'][0]['stories']
    creators = series['data']['results'][0]['creators']
    assert title == "100th Anniversary Special (2014)"
    assert type(comics) is dict
    assert type(events) is dict
    assert type(characters) is dict
    assert type(stories) is dict
    assert type(creators) is dict

def test_stories(marvel):
    with pytest.raises(MarvelException):
        marvel.stories.all(characters="Iron Man")

    stories = marvel.stories.get(998)

    title = stories['data']['results'][0]['title']
    comics = stories['data']['results'][0]['comics']
    events = stories['data']['results'][0]['events']
    characters = stories['data']['results'][0]['characters']
    creators = stories['data']['results'][0]['creators']
    series = stories['data']['results'][0]['series']

    assert title == "Interior #998"
    assert type(comics) is dict
    assert type(events) is dict
    assert type(characters) is dict
    assert type(creators) is dict
    assert type(series) is dict    