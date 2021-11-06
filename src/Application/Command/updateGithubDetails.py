import asyncio

import sys
import os
from pathlib import Path
from Domain.Aggregates.updateReposAggregate import UpdateReposAggregate

from Infrastructure.Models.getReposResponse import GetReposResponse

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
            resp: GetReposResponse = await self._githubService.getRepos()

            aggregatedReponse = UpdateReposAggregate(resp).reposItemObject

            print(aggregatedReponse)

            await self._githubFiles.injectIntoReposDB(aggregatedReponse)

            return resp

        except Exception as e:

            raise Exception(e)
