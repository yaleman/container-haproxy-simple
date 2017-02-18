A small set of scripts to run up a HAProxy load balancer and a pair of nginx containers to play with load balancing.

# Testing docker and the build

1. Find the IP address of the docker machine you're using (`docker-machine env`) and place it in docker_ip.cfg
2. Set up the virtual environment  by running `./setup_pip.sh`
3. Build the VMs and configuration with `./rebuild.sh`
4. Start it by running `./start.sh`

Now it should be running! Run `docker ps -f name=haproxy-simple-` to see a list of the nodes for this set.

# Turning off the containers

When you're done, stop them with `./stop.sh`

# Showing how load balancers work

A program called `getchecker.py` does repeated requests to the base URL of the HAProxy-provided endpoint. For every response it gets, it increments internal statistics. The servers are set up to respond with either "1" or "2" so statistics are fairly simple. :)

To run the program:

1. Activate the virtual environment with `source venv/bin/activate`
2. Run `python3 getchecker.py`.

You'll see something like this:

    Stats:
    1	224
    2	225

The left hand column is the response from the server, the number on the right is the number of responses it gets. If you stop one of the nginx nodes (with `./one_stop.sh`) you'll see the numbers change. To re-start the node, run `one_start.sh`.

