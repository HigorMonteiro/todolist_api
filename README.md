
### clone the repository

```
git clone git@github.com:HigorMonteiro/todolist_api.git
cd todolist_api/
```
### Running with Docker:

1. [Install docker](https://docs.docker.com/install/)
2. [Install the docker-compose](https://docs.docker.com/compose/install/)


```
docker-compose build
docker-compose run web python manage.py migrate
docker-compose run web pytest
docker-compose up
```
### Test Api GraphQL

url: http://localhost:8000/graphql

### Examples for testing in GraphQL


### LIST
```
{
  assignments {
    id
    title
    description
    createdAt
    projectBy {
      id
    }
  }
}

{
  project {
    id
    name
    assignmentSet {
      id
      title
    }
  }
}
```
### CREATE
```
mutation  {
createProject(name: "Primeiro Projeto")
  {
    project {
      id
      name
      
    }
  }
}

mutation  {
createAssignment(projectBy: 1, title: "Primeira Tarefa", description: "Criando minha primeira tarefa")
    {
        assignment {
            id
          	title
          	description
          	createdAt
          	projectBy {
          	  id
          	}

        }
    }
}
```

### UPDATE

```
mutation  {
updateAssignment(
  	assignmentId: 3,
    title: "Task pytest3",
    description: "Task pytest description",
  projectBy:2)
  	
    {
        assignment {
            id
            title
            description
          	projectBy {
          	  id
          	}
        }
    }
}

mutation  {
updateProject(
  	projectId: 2,
    name: "Project test2")
    {
        project {
            id
            name
        }
    }
}
```

### DELETE
```
mutation {
  deleteAssignment(assignmentId: 4){
    assignmentId
  }
}

mutation {
  deleteProject(projectId: 1){
    projectId
  }
}
```