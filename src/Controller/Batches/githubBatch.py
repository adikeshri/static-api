import asyncio
import os

import json
import sys
import os
from pathlib import Path

path_root = Path(os.path.realpath('__file__')).parents[2]
sys.path.append(str(path_root))
print(sys.path)

from Application.Command.updateGithubDetails import UpdateGithubDetails
from Infrastructure.githubService import GithubService

from Persistance.Files.githubRepository import GithubFiles


class GithubBatch:
    def __init__(self):
        self._application = UpdateGithubDetails(GithubService(), GithubFiles())

    async def initiate(self):

        await self._application.updateRepos()


async def main():
    x = GithubBatch()
    await x.initiate()


asyncio.run(main())