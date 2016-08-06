cd /app/scout_plates/data/incoming/

while true
do

if [ $(ls -ltr /app/scout_plates/data/incoming/ | wc -l) -gt 1 ]
then
for f in *.jpg
do
	echo "file=" $f 
	plate=$(alpr -n 3 -p nc $f)
	
	if [ $(echo $plate | wc -c) -gt 25 ]
	then
		ts=$(date +%s)
		echo "plate=" $plate
		echo $plate " - " $f > /app/scout_plates/logs/${ts}.log

		scp -i /app/scout_plates/conf/scout.pem /app/scout_plates/logs/${ts}.log ec2-user@ec2-54-173-144-98.compute-1.amazonaws.com:/logs/

		scp -i /app/scout_plates/conf/scout.pem /app/scout_plates/data/incoming/${f} ec2-user@ec2-54-173-144-98.compute-1.amazonaws.com:/data/

	else
		echo "No match for " ${f}
	fi
	rm -v $f
	#mv -v $f /app/scout_plates/data/archive/
	sleep 1 
done

fi

sleep 5

#if [ $(ls -ltr /app/scout_plates/logs/ | wc -l) -gt 1 ]
#then

#rsync --remove-source-files -az -e 'ssh -i /app/scout_plates/conf/scout.pem' /app/scout_plates/logs/*.log ec2-user@ec2-54-173-144-98.compute-1.amazonaws.com:/logs/

#fi

done
