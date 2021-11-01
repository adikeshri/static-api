import asyncio
from Application.Abstraction.IGithubFiles import IGithubFiles
from Application.Abstraction.IGithubService import IGithubService


class UpdateGithubDetails:
    def __init__(self, githubService: IGithubService,
                 githubRepository: IGithubFiles):
        self._githubService = githubService
        self._githubRepository = githubRepository

    def updateGithubDetails(self):
        contributors, repos = asyncio.gather(
            self._githubService.getContributorsOnRepo(),
            self._githubService.getRepos())
    def updateRepos(self):

        try:
            resp=self._githubService.getRepos()


