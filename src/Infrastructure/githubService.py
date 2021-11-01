from typing import Any
import requests
import json
from Application.Abstraction.IGithubService import IGithubService
from Domain.Exceptions.APICallFailed import APICallFailed


class GithubService(IGithubService):
    def __init__(self):
        self._hostUrl = "https://api.github.com"
        self._endPoints = {
            "repos": "/users/techhub-community/repos",
            "contributors": "/repos/techhub-community/{repoName}/contributors"
        }

    async def getRepos(self):
        try:
            response = await self.__callGetAPI(self._hostUrl +
                                               self._endPoints["repos"])
            return response
        except Exception as e:
            raise Exception(e)

    async def getContributorsOnRepo(self, repoName):
        try:
            response = await self.__callGetAPI(self._hostUrl +
                                               self._endPoints["contributors"].
                                               replace("{repoName}", repoName))
            return response
        except Exception as e:
            raise Exception(e)

    async def __callGetAPI(self, url, headers={}) -> Any:
        try:
            response = await requests.get(url, headers=headers)
            if response.status_code != 200:
                raise APICallFailed(response.status_code)
            jsonResponse = json.loads(response.text)
            return jsonResponse
        except:
            raise Exception("Exception occured when parsing json response")