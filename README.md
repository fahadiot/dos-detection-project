# DoS attack simulation and detection

by Fahad Waseem (M2 Networks and IoT, Cnam)

this project simulates some DoS attacks, detects them, logs the detected attacks
into a csv file and then analyses that csv in a jupyter notebook.

the files:

- attack_simulator.py is the attacker. it sends the attacks like syn_flood, pod,
  syn_ack, smurf. you give it the target ip, the attack type and how long to run.
- attack_detector.py is the detector. it listens on an interface and writes every
  detected attack packet into data/attacks.csv.
- sniffndetect.py is the detection module. it is based on the SniffnDetect module
  from github, i removed its web ui and fixed its bugs.
- analysis.ipynb is the notebook that reads data/attacks.csv and answers the three
  questions with plots.

for the floods i use a random source ip so the detected ips come from different
places as its needed for the map.

## setup

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

sniffing and sending raw packets normally needs root. to run it without sudo i
gave python the raw socket permission once:

```
sudo setcap cap_net_raw,cap_net_admin+eip venv/bin/python3.12
```

if you dont want to do that you can just run the commands below with sudo.

## how to run

i test it on one machine on the loopback address (127.0.0.1) using two terminals.

terminal 1, start the detector:

```
venv/bin/python attack_detector.py
```

terminal 2, run an attack (do it for each type):

```
venv/bin/python attack_simulator.py 127.0.0.1 syn_flood 10
venv/bin/python attack_simulator.py 127.0.0.1 pod 10
venv/bin/python attack_simulator.py 127.0.0.1 syn_ack 10
venv/bin/python attack_simulator.py 127.0.0.1 smurf 10
```

to run it on two machines, start the detector on the victim machine and point the
attacker at the victim ip, for example:

```
venv/bin/python attack_detector.py --iface wlp0s20f3 --victim-ip 192.168.1.55
venv/bin/python attack_simulator.py 192.168.1.55 syn_flood 10
```

## the analysis

open analysis.ipynb and run all the cells. it answers where the suspect ips are
located on a world map, which attack sent the most packets, and which attack
sent the most bytes and bytes per second.