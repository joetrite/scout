cd /app/scout_plates/data/incoming/

while true
do

for f in *.jpg
do
	echo "file=" $f 
	plate=$(alpr -n 3 -p nc -j $f)
	
	if echo $plate | grep -q "candidate"
	then
		echo "plate=" $plate
		echo $plate > /app/scout_plates/logs/`date +%s`.log
	fi
	rm -v $f
	sleep 1 
done

sleep 5

rsync --remove-source-files -azv -e 'ssh -i /app/scout_plates/conf/scout.pem' /app/scout_plates/logs/*.log ec2-user@ec2-54-173-144-98.compute-1.amazonaws.com:/logs/

done
