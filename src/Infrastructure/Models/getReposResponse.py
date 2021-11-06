from typing import List
from dataclasses  import  dataclass


@dataclass
class GetReposResponse:
    id: int
    name: str
    stargazers_count: int
