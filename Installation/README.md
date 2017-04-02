###Steps to be followed in Install Ansible and its Dependencies

1. Run NetworkAutomation/Installation/install.sh

2. Check Ansible Version using ($ansible --version). This should return proper value with no errors.

3. Edit /etc/hosts with proper IP addresses of Hosts or Network Devices

4. Create file with name "config" under ~/.ssh/ (touch config)

5. Make the StrictHostCheckingKey as NO so that Ansible need not fail to connect for first time.
 Open config file using vim and add the line 

6. Verify you are able to SSH into hosts configured in /etc/hosts

7. Few important alias commands are added into bashrc file instead of typing ssh commands every time.
   Please use it convenience.

	alias vmm1="sshpass -p 'password' ssh -o ServerAliveInterval=30 ubuntu@vmm1.local"
	alias vmm2="sshpass -p 'password' ssh -o ServerAliveInterval=30 ubuntu@vmm2.local"
	alias virl="sshpass -p 'VIRL' ssh -o ServerAliveInterval=30 virl@virl.local"
	alias web="sshpass -p 'password' ssh -o ServerAliveInterval=30 web@web.local"
	alias app="sshpass -p 'password' ssh -o ServerAliveInterval=30 app@app.local"
	alias db="sshpass -p 'password' ssh -o ServerAliveInterval=30 db@db.local"
	alias router1="sshpass -p 'cisco' ssh -o ServerAliveInterval=30 cisco@router1.local"
	alias router2="sshpass -p 'cisco' ssh -o ServerAliveInterval=30 cisco@router2.local"
	alias router3="sshpass -p 'cisco' ssh -o ServerAliveInterval=30 cisco@router3.local"
	alias nxswitch1="sshpass -p 'cisco' ssh -o ServerAliveInterval=30 cisco@nxswitch1.local"
	alias nxswitch2="sshpass -p 'cisco' ssh -o ServerAliveInterval=30 cisco@nxswitch2.local"


