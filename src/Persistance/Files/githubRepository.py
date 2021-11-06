import os
import json
import sys
import os
from pathlib import Path

import dataclasses

path_root = Path(os.path.realpath('__file__')).parents[2]
sys.path.append(str(path_root))
from Application.Abstraction.IGithubFiles import IGithubFiles


class GithubFiles(IGithubFiles):
    def __init__(self):

        dirname = os.path.dirname(__file__)
        self._reposDataFile = "../../Data/githubRepos.json"
        with open(self._reposDataFile, "r") as f:
            self._githubRepos = json.load(f)

        self._contributorsDataFile = "../../Data/githubContributors.json"
        with open(self._contributorsDataFile, "r") as f:
            self._githubContributors = json.load(f)

        self.DatabaseFiles = {
            "repos": self._reposDataFile,
            "contributors": self._contributorsDataFile
        }

        self.DataBases = {
            "repos": self._githubRepos,
            "contributors": self._githubContributors
        }

    async def getGithubReposData(self):
        return self._githubRepos

    async def getGithubContributorsData(self):
        return self._githubContributors

    async def injectIntoReposDB(self, data):
        self._githubRepos = data

        await self.__updateDB("repos")

    async def injectIntoContributorsDB(self, data):
        self._githubContributors = data

        await self.__updateDB("repos")

    async def __updateDB(self, dbName):
        fileName = self.DatabaseFiles[dbName]

        data = None

        if dbName == "repos":



            print(self._githubRepos)
            data = self._githubRepos

        else:

            data = self._githubContributors

        try:
            with open(fileName, "w") as f:
                json.dump(dataclasses.asdict  (data), f, indent=2)

        except Exception as e:

            print(e)
            raise Exception("Failed to write to DB")