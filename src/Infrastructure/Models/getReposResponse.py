from typing import List


class RepoDetails:
    def __init__(self, **kwargs):

        self.id = kwargs["id"]
class GetReposResponse:
    def __init__(self, repoDetails:List[RepoDetails]):
        self.repoDetails: List[RepoDetails] = repoDetails











