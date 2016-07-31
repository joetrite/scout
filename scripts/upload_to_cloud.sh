rsync --remove-source-files -azv -e 'ssh -i /app/scout_plates/conf/scout.pem' /app/scout/logs/*.log ec2-user@ec2-54-173-144-98.compute-1.amazonaws.com:/logs/
