# A music recommendation system using fuzzy logic and Last.fm tags

## Running the programs
1. Download & extract the dataset
2. run `python get_tags_from_albums.py <path-to-data>`
TODO:
3. Cluster data using the example in `example_clustering.py`
4. Make a script for processing a new user and returning a new album
5. Calculate the performance of recommendation(evaluation)

`FLS/` contains a basic implemenation of fuzzification, which we're not using. It's just a try-out, and can be disregarded

-----
Dataset:
- http://www.dtic.upf.edu/~ocelma/MusicRecommendationDataset/lastfm-1K.html

Useful links:
- Last.fm API in Python: [pylast](https://github.com/pylast/pylast)
- Last.fm API documentation: [last.fm/api](http://www.last.fm/api)
- cmeans clustering(from [scikit-fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy))
- [ishibuchi classification maybe?](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.294.6338&rep=rep1&type=pdf)

-----
### The .api_key file should look like a json file:
```
{
  "application_name": "Fuzzy Logic Music Recommendation",
  "key": <GET FROM LAST.FM>,
  "shared_secret": <GET FROM LAST.FM>,
  "username": <INSERT USERNAME HERE>,
  "password": <INSERT PASSWORD HERE>
}
```
