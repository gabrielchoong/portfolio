from dataclasses import dataclass


@dataclass
class Project:
    name: str
    description: str
    language: str
    readme: str
    url: str
