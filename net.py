from netmiko import ConnectHandler


linux = {
        'device_type': 'linux',
        'ip': '192.168.56.120',
        'username': 'vagrant',
        # 'password': 'testpass',
        'port': 22,
        'allow_agent': True,
        'use_keys': True,
        'key_file': r'C:\Users\solya\.ssh\id_rsa',
        'verbose': True,
        'timeout': 5
        }

connection = ConnectHandler(**linux)

output = connection.send_command('hostname')
print(f"\n \033[1mhostname\033[0m: {output}\n")

output = connection.send_command('sudo netstat -ltupn')
print(f"\n \033[1mActive connections\033[0m{output}\n")

output = connection.send_command('docker ps')
print(f"\033[1mList active containers\033[0m:\n{output}\n")

output = connection.send_command("""docker ps --format "{{.ID}}" | xargs docker container inspect \
    | grep -o '"NetworkID": "[^"]*' | grep -o '[^"]*$'  \
    | uniq | xargs docker network inspect""")
print(f"\033[1mNetwork configuration activ containers\033[0m:\n {output}\n")

output = connection.send_command('sudo fdisk -l')
print(f"\033[1mlist disks and partions\033[0m:\n {output}\n")

output = connection.send_command('df -h')
print(f"\033[1mAvalible space\033[0m:\n {output}\n")

output = connection.send_command('sudo cat /etc/passwd')
print(f"\033[1mlist of the system's accounts\033[0m:\n {output}\n")

output = connection.send_command("""docker inspect --format 'At container\
     {{ .Name }} runs {{ .Args }} on port {{ .HostConfig.PortBindings }}' $(docker ps -q)""")
print(f"\n \033[1mAt container runs on port\033[0m:\n {output}\n")

output = connection.send_command('sudo netstat -tulpn | grep LISTEN')
print(f"\n \033[1mlist of running app with binding to open network ports\033[0m:\n {output}\n")

print(f"\n\n\033[1mReport Complete!!!\033[0m\n\n")



connection.disconnect()