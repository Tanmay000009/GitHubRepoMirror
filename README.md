[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10772484&assignment_repo_type=AssignmentRepo)

<br />
<div align="center">
  <h3 align="center">Tanmay Vyas's submission</h3>

  <p align="center">
    Submission to BalkanID's summer intern hiring by Tanmay Vyas 20BCE0755
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This project involves creating a program that interacts with the GitHub API using OAuth authentication to fetch data about repositories and their owners, and store the normalized and deduplicated data in a Postgres database. The program should handle network failures and other errors with proper error handling and retries, and log all relevant information to aid in debugging. The data should be normalized before being stored in the database, and duplicates should be checked and updated instead of creating new records. The program should be able to fetch both public and private repositories of a user, providing a dynamic and versatile solution for managing GitHub repository data.

### Built With
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

## Getting Started: Clone and venv Setup

1. Clone the repository using the git clone command. <br />
```
https://github.com/BalkanID-University/balkanid-summer-internship-vit-vellore-2023-Tanmay000009/
```
2. Navigate to the project directory.
```
cd balkanid-summer-internship-vit-vellore-2023-Tanmay000009
```
3. Create a new virtual environment using the venv module. Run the command:
```
python3 -m venv balkantask
```
4. Activate the virtual environment using the source command. Run the command:
```
source balkantask/bin/activate
```
> Note: If you are using Windows, the command to activate the virtual environment will be slightly different. You can run the command 
> ```
> .\env\Scripts\activate 
> ```
5. Install the required packages using the pip install command and the requirements.txt file. Run the command:
```
pip install -r requirements.txt
```

## Configuring GitHub OAuth and .env Settings

1. Create a GitHub account (if you don't already have one).
2. Register a new OAuth application on GitHub by going to `Settings -> Developer settings -> OAuth Apps -> New OAuth App`. <br />
[Click here](https://github.com/settings/applications/new)
3. Enter the following information for the application:
    - Application name: Choose a name for your application.
    - Homepage URL: Set this to http://127.0.0.1:8000/ or whatever your local server address is.
    - Application description: Optionally, enter a description for your application.
    - Authorization callback URL: Set this to http://127.0.0.1:8000/social-auth/complete/github.
4. After creating the application, you will be provided with a Client ID and a Client Secret. Keep these values safe, as you will need them later to configure the Django application.
5. Copy the values from .env.sample to a new .env file in your project's root directory.
6. Replace the placeholder values with your actual database credentials and GitHub OAuth application credentials.

     - `SECRET_KEY`: Generate a new Django secret key.
     - `DB_ENGINE`: The database engine you are using (e.g. `django.db.backends.postgresql`).
     - `DB_NAME`: The name of the database.
     - `DB_USERNAME`: The username for accessing the database.
     - `DB_PASSWORD`: The password for accessing the database.
     - `DB_HOST`: The hostname for the database.
     - `DB_PORT`: The port number for the database.
     - `GITHUB_CLIENT_ID`: The Client ID provided by GitHub for your OAuth application.
     - `GITHUB_CLIENT_SECRET`: The Client Secret provided by GitHub for your OAuth application.

## Starting the Program: Commands and Execution
1. Run the development server using the command <br /> 
 ```
 python manage.py runserver
 ``` 
This will start the server on the default port 8000. <br />
2. Open your web browser and navigate to http://127.0.0.1:8000/ to see your Django project up and running.
