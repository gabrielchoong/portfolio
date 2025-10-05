from typing_extensions import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import dotenv_values

from dataclasses import asdict
from .helpers import (
    get_repo_url,
    github_auth,
    repo_is_fork,
    get_repo_name,
    get_repo_description,
    get_repo_language,
    get_repo_readme,
)
from .Project import Project


import os

app = FastAPI()

origins = [
    "http://localhost:5173",
]

if os.getenv("VERCEL_URL"):
    origins.append(f"https://{os.getenv('VERCEL_URL')}")


# it doesn't work without this
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/projects")
def get_projects() -> list[dict[str, Any] | Any]:
    """Exposes the projects from a GitHub account on `/api/projects` to be stylised and used by a frontend library"""
    try:
        auth_token = dotenv_values()["GITHUB_ACCESS_TOKEN"]
        user = github_auth(auth_token).get_user()
        project_list = []

        for repo in user.get_repos(sort="pushed", direction="desc"):
            if repo_is_fork(repo):
                continue

            project = Project(
                name=get_repo_name(repo),
                description=get_repo_description(repo),
                language=get_repo_language(repo),
                readme=get_repo_readme(repo),
                url=get_repo_url(repo),
            )

            project_list.append(asdict(project))

        return project_list
    except Exception as e:
        print(f"An error occured at GitHub: {e}")
        return []
