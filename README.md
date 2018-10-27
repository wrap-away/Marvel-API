# Marvel API

Installation
============

Using ``pip``:



	pip install marvel

This is an API wrapper for [Marvel](https://developer.marvel.com/docs).

Usage
=====

Usage is as simple as it gets:

    from marvel import Marvel
    m = Marvel(PUBLIC_KEY, PRIVATE_KEY)

Now there are six objects presented namely, `characters`, `comics`, `creators`, `events`, `series` and `stories`
as listed at [Developers](https://developer.marvel.com/documentation/entity_types)

    characters = m.characters
    comics = m.comics
    creators = m.creators
    events = m.events
    series = m.series
    stories = m.stories

Each of the above object returns back the appropriate response (json) as mentioned in official [docs](https://developer.marvel.com/docs)


Module Examples
===============


Module Examples:

    m = Marvel(PUBLIC_KEY, PRIVATE_KEY)
    characters = m.characters

Get All Characters:

    all_characters = characters.all()

Get Single Character:

    character = characters.get(1011334)

Get Some Character's Comics:

    comics = characters.comics(1011334)

Similarly, you could apply the same logic to different objects, an example:

    m = Marvel(PUBLIC_KEY, PRIVATE_KEY)
    stories = m.stories
    all_stores = stories.all()
    story = stories.get(id)
    events = stories.events(id)

Finally, the sub resources that each object has are as follows:

- Characters
    - `all`, `get`, `comics`, `events`, `series`, `stories`
- Comics
    - `all`, `get`, `characters`, `creators`, `events`, `stories`
- Creators
    - `all`, `get`, `comics`, `events`, `series`, `stories`
- Events
    - `all`, `get`, `characters`, `comics`, `creators`, `series`, `stories`
- Series
    - `all`, `get`, `characters`, `comics`, `creators`, `events`, `stories`
- Stories
    - `all`, `get`, `characters`, `comics`, `creators`, `events`, `series`

# Exception Handling

You can catch any exception caused by Marvel API such as authentication error, bad input error, server down error, etc by handling the `MarvelException` at `marvel/exceptions.py`.

# Running Tests

`python -m pytest tests/`
