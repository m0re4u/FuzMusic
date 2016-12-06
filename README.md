# A music recommendation system using fuzzy logic and Last.fm tags

-----
Future stuff:
- Last.fm API in Python: [pylast](https://github.com/pylast/pylast)
- cmeans clustering(from [scikit-fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy))
- ichibuchi clustering
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
