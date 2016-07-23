
rsync --remove-source-files -azv -e 'ssh -i /app/scout/conf/scout.pem' /app/scout/data/* ec2-user@ec2-54-84-169-92.compute-1.amazonaws.com:/data/

rsync --remove-source-files -azv -e 'ssh -i /app/scout/conf/scout.pem' /app/scout/logs/* ec2-user@ec2-54-84-169-92.compute-1.amazonaws.com:/logs/
