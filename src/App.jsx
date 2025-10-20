import { useState, useEffect } from "react";
import { Spinner, Text } from "@chakra-ui/react";
import { Projects } from "./components/RepoRenderer";

import "./App.css";

const App = ({ appName }) => {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await fetch("/api/projects");

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        setProjects(data);
      } catch (e) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };

    fetchProjects();
  }, []);

  if (loading) {
    return (
      <div>
        <Spinner size="sm" />
        <Text> Loading ...</Text>
      </div>
    );
  }

  if (error) {
    return <div>Error fetching projects: {error}</div>;
  }

  return <Projects title={appName || "Default Title"} myRepos={projects} />;
};

export default App;
