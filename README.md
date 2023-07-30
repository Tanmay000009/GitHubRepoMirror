<br />
<div align="center">
  <h3 align="center">GitHubRepoMirror</h3>
</div>

<!-- ABOUT THE PROJECT -->

## About The Project

This project involves creating a program that interacts with the GitHub API using OAuth authentication to fetch data about repositories and their owners, and store the normalized and deduplicated data in a Postgres database. The program handles network failures and other errors with proper error handling and retries, and log all relevant information to aid in debugging. The data is normalized before being stored in the database, and duplicates are checked and updated instead of creating new records. The program is able to fetch both public and private repositories of a user, providing a dynamic and versatile solution for managing GitHub repository data.

### Built With

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

## Prerequisites

1. Python 3.11 installed on the system. [Get Python](https://www.python.org/).
2. Access to a Postgres database instance.
3. Docker & Docker Compose (Optional).

## Getting Started: Clone and venv Setup

1. Clone the repository using the git clone command. <br />

```
https://github.com/Tanmay000009/GitHubRepoMirror
```

2. Navigate to the project directory.

```
cd GitHubRepoMirror
```

3. Create a new virtual environment using the venv module. Run the command:

```
python3 -m venv <virtual-env name>
```

4. Activate the virtual environment using the source command. Run the command:

```
source <virtual-env name>/bin/activate
```

> Note: If you are using Windows, the command to activate the virtual environment will be slightly different. You can run the command
>
> ```
> .\env\Scripts\activate
> ```
>
> 5. Install the required packages using the pip install command and the requirements.txt file. Run the command:

```
pip install -r requirements.txt
```

## Configuring GitHub OAuth and .env Settings

1. Create a GitHub account (if you don't already have one). [Create Github Account](https://github.com/join).
2. Register a new OAuth application on GitHub by going to `Settings -> Developer settings -> OAuth Apps -> New OAuth App`. <br />
   [Click here](https://github.com/settings/applications/new)
3. Enter the following information for the application:
   - Application name: Choose a name for your application.
   - Homepage URL: Set this to `http://127.0.0.1:8000/` or whatever your local server address is.
   - Application description: Optionally, enter a description for your application.
   - Authorization callback URL: Set this to `http://127.0.0.1:8000/social-auth/complete/github`.
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

This will start the server on the default port 8000. <br /> 2. Open your web browser and navigate to http://127.0.0.1:8000/ to see your Django project up and running.

## Starting the Program: Commands and Execution [With Docker]

> Note: Make sure the database instance is accessible through Docker container.

1. Build a docker image for the container.

```
docker build -t <app-name> .
```

2. Run the docker image.

```
docker run -it -p 8000:8000 <app-name>
```

## Starting the Program: Commands and Execution [With Docker Compose]

1. Compose the docker image for the container.

```
docker-compose up
```

<!-- CONTACT -->

## Contact

Tanmay Vyas

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Tanmay000009)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tanmay-vyas-09/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tanmayvyas09@gmail.com)
[![Resume](https://img.shields.io/badge/Resume-000000?style=for-the-badge&logo=read-the-docs&logoColor=white)](https://drive.google.com/file/d/1lkfmeqseeSwK1GlJHEblz2ZuYzdNBRhm/view?usp=drive_link)
