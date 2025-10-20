import { Box, Button, Card, Heading, SimpleGrid } from "@chakra-ui/react";
import { FaGithub } from "react-icons/fa";
import { Quote } from "./Quote";
import { random } from "quotesy";

const ProjectTitle = ({ title }) => {
  return (
    <Heading size="4xl" fontWeight="bold" pb="32px">
      {title || "Default Title"}
    </Heading>
  );
};

const RepoCard = ({ repoName, repoDescription, repoLanguage, repoLink }) => {
  return (
    <Card.Root>
      <Card.Header>{repoLanguage}</Card.Header>
      <Card.Body>
        <Card.Title mb="2">{repoName}</Card.Title>
        <Card.Description>{repoDescription}</Card.Description>
      </Card.Body>
      <Card.Footer justifyContent="flex-end">
        <Button size="md" variant="subtle" rounded="13" asChild>
          <a href={repoLink} target="_blank" rel="noopener noreferrer">
            <FaGithub /> GitHub
          </a>
        </Button>
      </Card.Footer>
    </Card.Root>
  );
};

const RepoGrid = ({ myRepos }) => {
  return (
    <SimpleGrid columns={3} gap="40px">
      {myRepos.map((repo) => (
        <RepoCard
          repoName={repo.name}
          repoDescription={repo.description}
          repoLanguage={repo.language}
          repoLink={repo.url}
        />
      ))}
    </SimpleGrid>
  );
};

const Projects = ({ title, myRepos }) => {
  const quote = random();
  return (
    <Box>
      <ProjectTitle title={title} />
      <Quote quote={quote.text} author={quote.author} />
      <RepoGrid myRepos={myRepos} />
    </Box>
  );
};

export { Projects };
