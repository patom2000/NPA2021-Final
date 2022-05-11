mkdir tempdir

cp 62070111-bot.py tempdir/.
cp requirment.txt tempdir/.

echo "FROM python" > tempdir/Dockerfile
echo "COPY ./requirment.txt /home/myapp/req/" >> tempdir/Dockerfile
echo "RUN pip install -r /home/myapp/req/requirment.txt" >> tempdir/Dockerfile

echo "COPY ./62070111-bot.py /home/myapp/" >> tempdir/Dockerfile

echo "EXPOSE 8080" >> tempdir/Dockerfile

echo "CMD python3 /home/myapp/62070111-bot.py" >> tempdir/Dockerfile

cd tempdir
docker build -t bot .
docker run -t -d -p 8080:8080 --name botrunning samplebot
docker ps -a