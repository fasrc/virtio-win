This virtio-win RPM spec file has been used to resolve this error:

     [root at kvm01b ~]# virt-v2v -ic 'esx://my-vmware-hypervisor.example.com/' -os transferimages --network default my-vm
     my-vm_my-vm: 100% [====================================]D
     virt-v2v: Installation failed because the following files referenced in
     the configuration file are required, but missing:
     /usr/share/virtio-win/drivers/amd64/Win2008

See also

* http://serverfault.com/questions/395347/where-should-centos-users-get-usr-share-virtio-win-drivers-for-virt-v2v
* [CentOS-virt] Where should CentOS users get /usr/share/virtio-win/drivers for virt-v2v? - http://lists.centos.org/pipermail/centos-virt/2012-June/002927.html
