import os

tendrl = raw_input("Enter type server/node = ")
if tendrl == "node":
    oper = raw_input("Enter oper stop/start = ")
    if oper == "stop":
        os.system('service tendrl-node-agent stop')
        os.system('service collectd stop')
        os.system('service tendrl-gluster-integration stop')
        # os.system('yum -y remove tendrl-gluster-integration -y')
    if oper == "start":
        os.system('service tendrl-node-agent start')
        

if tendrl == "server":
    oper = raw_input("Enter oper stop/start = ")
    if oper == "stop":
        os.system('service tendrl-node-agent stop')
        os.system('service etcd stop')
        os.system('service grafana-server stop')
        os.system('service carbon-cache stop')
        os.system('rm -rf /var/lib/carbon/whisper/*')
        os.system('rm -rf /var/lib/grafana/grafana.db')
        os.system('rm -rf /var/lib/etcd/default.etcd/member/*')
    if oper == "start":
        os.system('service etcd start')
        os.system('service grafana-server start')
        os.system('service carbon-cache start')
        os.system('service tendrl-node-agent start')   
        os.chdir("/usr/share/tendrl-api")
        os.system('RACK_ENV=production rake etcd:load_admin')
        os.system('service tendrl-api start')
        os.system('service tendrl-monitoring-integration start')
        os.system('service tendrl-notifier start')
