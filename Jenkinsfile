pipeline {

   agent {
         label 'Honeybees-API-DEV'
         }
   stages {

     stage ('Docker Deployment') {
       steps {
          echo "copying the latest file in Docker container"
          sh 'sudo docker cp . bed-dev-server:/usr/src/app'
             }
         }

     stage  ('Python Packages') {
       steps {
          echo "installing the packages from requirement.txt file"
          sh 'sudo docker exec bed-dev-server pip install -r requirements.txt'
             }
         }
     stage  ('Cron Remove') {
       steps {
          echo "removing crons in crontab"
          sh 'sudo docker exec bed-dev-server python manage.py crontab remove'
             }
         }
     stage  ('Cron addition') {
       steps {
          echo "adding crons in crontab"
          sh 'sudo docker exec bed-dev-server python manage.py crontab add'
             }
         }
     stage  ('Static files') {
       steps {
          echo "Updating static files"
          sh 'sudo docker exec bed-dev-server python manage.py collectstatic --noinput'
             }
         }
     stage ('Restart Docker and cron service') {
       steps {
          echo "restarting the docker"
          sh "sudo docker restart bed-dev-server"
          sh "sudo docker exec  bed-dev-server bash /etc/init.d/cron start"
             }
         }
     }
}
