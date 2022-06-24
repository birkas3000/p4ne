import glob

ip_adresseses = []

for current_file in glob.glob(r'..\config_files\*.txt'):
    with open(current_file) as f:
        i = 0
        for ip_line in f:
            if ip_line.find("ip address") == 1:
                str_common = (ip_line.replace("ip address", " ").strip()).split(' ')
                str_ip = str_common[0]
                str_mask = str_common[-1]
                ip_adresseses.append({'IP_{}'.format(i): str_ip, 'Mask_{}'.format(i) : str_mask})
                i += 1

for i in range(len(ip_adresseses)):
    print(ip_adresseses[i])
