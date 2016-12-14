#!/usr/bin/env python
"""Fetch list of all repos."""
import os
from github import Github
readonly_token = os.environ['READ_ONLY_TOKEN']
g = Github(readonly_token)
repos = [r.name for r in g.get_organization('warbyparker').get_repos()]

for r in sorted(repos):
    print(r)
