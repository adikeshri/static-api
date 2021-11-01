import os
import json
import sys; import os;from pathlib import Path



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
        self._githubRepos = {
            "repoCount": data["projects"],
            "totalStars": data["stars"]
        }

        await self.__updateDB("repos")

    async def injectIntoContributorsDB(self, data):
        self._githubContributors = data

        await self.__updateDB("repos")

    async def __updateDB(self, dbName):
        fileName = self.DatabaseFiles[dbName]

        data = self.Databases[dbName]

        try:
            with open(fileName, "w") as f:
                await json.dump(data, f, indent=2)

        except:

            raise Exception("Failed to write to DB")