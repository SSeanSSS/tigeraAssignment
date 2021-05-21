to build : docker build --tag tigera-project .
To run use the command : docker run --publish 5000:5000 tigera-project
to run test cases : docker exec -d [container_id] python -m unittest -v test1.py
to show result : curl http://localhost:5000/
