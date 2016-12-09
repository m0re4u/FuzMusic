# A music recommendation system using fuzzy logic and Last.fm tags

-----
Dataset:
- http://www.dtic.upf.edu/~ocelma/MusicRecommendationDataset/lastfm-1K.html
Future stuff:
- Last.fm API in Python: [pylast](https://github.com/pylast/pylast)
- cmeans clustering(from [scikit-fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy))
- [ichibuchi classification](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.294.6338&rep=rep1&type=pdf)
- word2vec for tags


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
