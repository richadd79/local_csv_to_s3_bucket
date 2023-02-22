# DE - Move/Copy Local CSV File(s) to S3 Bucket
___

This small project demonstrates how to copy/move a local file(csv, txt etc) to a specified S3 Bucket.

___
### Setup
___
#### Prerequisite
1. Visual Studio Code or (any IDE of choice)
2. AWS account
3. Docker with at least 4GB of RAM and Docker Compose v1.27.0 or later

---

Run these commands to setup your project

    # Clone and cd into the project directory.
      git clone https://github.com/richadd79/local_csv_to_s3_bucket.git
      cd local_csv_to_s3_bucket

    # Run command to create folder to store your csv or flat file to work with, Run command
      mkdir ./data

    # Run command to start Airflow
      docker-compose up -d

    # Open Airflow UI, 
      Go to: localhost:8080
      
    # Do this! 
     Create a connection for AWS like in the screenshot below
 
   ![image](https://user-images.githubusercontent.com/24456790/220696846-04a985d7-d201-4905-a92a-79516c394308.png)
   
## Have a little fun with this
