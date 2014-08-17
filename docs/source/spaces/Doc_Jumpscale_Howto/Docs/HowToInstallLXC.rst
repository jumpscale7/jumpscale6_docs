

How to configure your machine to use LXC
****************************************

install sandbox on 14.04
========================




.. code-block:: python

  curl http://install.jumpscale.org:85/cmds/jsbox_unstable.sh > /tmp/init.sh;sh /tmp/init.sh
  export JSBASE=/opt/jsbox
  js




Install lxc as host
===================




.. code-block:: python

  jpackage install -n lxc,openvswitch
  
  #on 1 disk
  mkfs.btrfs /dev/sdb -f
  
  #on 2 disk
  mkfs.btrfs -d /dev/sdb /dev/sdc -f
  
  mkdir /mnt/btrfs
  mount /dev/sdb /mnt/btrfs
  btrfs subvolume create /mnt/btrfs/lxc
  
  h3. configure networking
  
  if you work with DHCP
  jsnet initdhcp -i eth0 -b public
  otherwise when static ip
  jsnet init -i eth0 -a 192.168.248.100/24 -g 192.168.248.1 -b public
  
  
  jsnet init -i eth0 -a 172.16.4.2/24 -b gw_mgmt
  jsnet init -i eth0 -a 172.16.1.2/24 -b mgmt
  jsnet init -i eth0 -a 172.16.22.2/24 -b storage
  
  #NEXT IS FOR SURE REQUIRED, is internal network for mgmt of LXC containers, use this network for automation
  jsnet init -i p5p1 -a 10.10.253.1/24 -b lxc
  
  h3. get your base
  
  #IMPORT BASE
  #you can define a other basepath if its something else then /mnt/btrfs/lxc/ by defining 
  #lxc.basepath=/mnt/btrfs/lxc
  #Import is a rsync commando towards a sync server this server should be configured as:
  #jssync.addr=95.85.60.252
  
  jsmachine importR -n base -m base -k test

