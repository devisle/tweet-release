# Tweet-Release

Posts a new tweet when [advanced-react-cli](https://github.com/devisle/advanced-react-cli) has a new version release.

Code works fine for one package, but needs to be rewritten when using multiple packages. Not finished by any means.

### Build:

Clone repository:

```
git clone https://github.com/devisle/tweet-release.git
```

Install requirements:

```
pip install -r requirements.txt
```

`OAuth`:

Add your keys and tokens in `config.py` file following `config.example.py` format after you have set-up in [developer.twitter.com](https://develper.twitter.com).

Run:

```
python tweet.py
```
