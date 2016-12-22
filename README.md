# A music recommendation system using fuzzy logic and Last.fm tags

## Running the programs
1. Download & extract the dataset
2. run `python split_tsv_per_user.py <path-to-tsv-file>`
3. run `run_all.sh <path-to-split/-directory>` and follow the instructions
4. Evaluation scripts are in `eval/`

`FLS/` contains a basic implemenation of fuzzification, which we're not using. It's just a try-out, and can be disregarded

-----
Dataset:
- http://www.dtic.upf.edu/~ocelma/MusicRecommendationDataset/lastfm-1K.html

Useful links:
- Last.fm API in Python: [pylast](https://github.com/pylast/pylast)
- Last.fm API documentation: [last.fm/api](http://www.last.fm/api)
- cmeans clustering(from [scikit-fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy))
- [~~ishibuchi classification maybe?~~](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.294.6338&rep=rep1&type=pdf)

Note that the Last.fm API is veeery slow, so be doing the preprocessing yourself would take a lot of time
It'd probably be wise to work with configuration files in the future..<sub><sup><sub><sup>also the code could be cleaned up a whole bunch</sup></sub></sup></sub>
-----
### Defuzzification (and returning albums based on clusters of tags)
- Get an album from other user in the same cluster(collaborative) - but then why cluster and not just lookup the closest user?
- Use the most frequent tag(s) with [tag.getTopAlbums](http://www.last.fm/api/show/tag.getTopAlbums). Will be very prone to music coming from the head of popularity
- Something with difference to closest cluster(weighted in case of fuzzy clusters)

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
