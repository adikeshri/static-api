import asyncio

import sys; import os;from pathlib import Path



path_root = Path(os.path.realpath('__file__')).parents[2]
sys.path.append(str(path_root))
from Application.Abstraction.IGithubFiles import IGithubFiles
from Application.Abstraction.IGithubService import IGithubService


class UpdateGithubDetails:
    def __init__(self, githubService: IGithubService,
                 githubFiles: IGithubFiles):
        self._githubService = githubService
        self._githubFiles = githubFiles

    def updateGithubDetails(self):
        contributors, repos = asyncio.gather(
            self._githubService.getContributorsOnRepo(),
            self._githubService.getRepos())
    async def updateRepos(self):

        try:
            resp=await self._githubService.getRepos()

            return resp

        except Exception as  e:

            raise Exception(e)


