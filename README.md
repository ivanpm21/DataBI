# Simple analitics project

This is a simple project with the purpose of analize the productivity and well being of employees with a synthetic dataset obtained from [Kaggle](https://www.kaggle.com/datasets/mrsimple07/remote-work-productivity). 

## Diagram

![diagram](diagram.png)

## Run locally

To run locally, you need Docker, PowerBI and create a file named '.env' with the next variables:

1. POSTGRES_USER
2. POSTGRES_PASSWORD
3. POSTGRES_DB

Then you can use "docker-compose up" to run it and connect via PowerBI with the credentials you just put and the port 5432.
