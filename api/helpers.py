import logging
from github import Auth, Github, UnknownObjectException


def github_auth(auth_token: str | None) -> Github:
    """
    Authenticates the user.

    DO NOT pass in authentication tokens as string literals. Use the `dotenv` library to handle this securely:

    ```python
    from dotenv import dotenv_values
    personal_auth_token = dotenv_values()["YOUR_ENV_VAR"]
    github_user = github_auth(personal_auth_token).get_user()
    ```

    In your `.env` file, ensure an environment variable is created:

    ```
    # .env
    YOUR_ENV_VAR=generated_authentication_tokens
    ```

    Args:
        auth_token: The GitHub personal access tokens obtained via <https://github.com/settings/personal-access-tokens>

    Returns:
        A Github object if authentication is successful.

    Raises:
        A RuntimeError if authentication failed.
    """
    if auth_token is None:
        raise RuntimeError("Unable to authenticate to GitHub!")
    github = Github(auth=Auth.Token(auth_token))
    return github


def repo_is_fork(repo) -> bool:
    """Returns a truthy value whether a GitHub repo is a fork."""
    return repo.fork


def get_repo_name(repo) -> str:
    """It is impossible for a repository to not have a name on GitHub."""
    return repo.name


def _repo_val(value, log_info: str, fallback: str) -> str:
    """An abstraction layer to handle certain repository values."""
    if value is None:
        logging.info(log_info)
        return fallback
    return value


def get_repo_description(repo) -> str:
    """Returns the repository description if any."""
    log_info = f"There is no description for {get_repo_name(repo)}."
    fallback = "Description"
    return _repo_val(repo.description, log_info, fallback)


def get_repo_language(repo) -> str:
    """Returns the languages used in a repository if any."""
    log_info = f"There is not enough data for {get_repo_name(repo)} to generate languages used."
    fallback = "OwO"
    return _repo_val(repo.language, log_info, fallback)


def get_repo_readme(repo) -> str:
    """Retrieves the `README.md` file of a repository if it exists."""
    try:
        readme_content = repo.get_contents("README.md")
        return readme_content.decoded_content.decode()
    except UnknownObjectException:
        logging.info(
            f"Repository '{get_repo_name(repo)}' does not have a README.md file. Skipping."
        )
        return "A README for this repository is not available"
    except Exception as e:
        logging.error(
            f"An unexpected error occurred fetching README for '{repo.name}': {e}"
        )
        return "Error retrieving README"


def get_repo_url(repo):
    """Returns the github url => `https://github.com/...` of a repo instead of the api.github url => `https://api.github.com/...` of a repo."""
    return repo.html_url
