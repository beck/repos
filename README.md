# Helper bins to work with all org repos

## Getting Started

Checkout this repo to the same directory where other repos should be cloned.

Generate a read-only token:  
https://github.com/settings/tokens

```
python -m venv vnev
source venv/bin/activate
pip install -r requirements.txt
cp secret.template secret
# add token to ./secret
```

Checkout all repos:
```
./bin/repos-checkout
```

Add bins to your `.bash_profile` `PATH` for easy access:
```
export PATH="$PATH:$HOME/projects/repos/bin"
```

## Available bins

* `repos-checkout` - clone all
* `repos-history-search` - search the log
* `repos-pull` - checkout master and pull
* `repos-search` - git grep
