FROM worker:latest
WORKDIR app
# Run app.py when the container launches
CMD ["mrq-worker", "-c", "config/cake.py"]
