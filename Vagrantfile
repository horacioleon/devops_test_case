Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.provider "virtualbox" do |config|
    config.gui = false
  end

  config.vm.define "postgres01" do |postgres01|
    postgres01.vm.hostname = "postgres01.local.com"
    postgres01.vm.network "private_network", ip: "192.168.0.30"
    postgres01.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/postgres_master.yml"
    end
    postgres01.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 2
    end
  end

  config.vm.define "postgres02" do |postgres02|
    postgres02.vm.hostname = "postgres02.local.com"
    postgres02.vm.network "private_network", ip: "192.168.0.31"
    postgres02.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/postgres_slave.yml"
    end
    postgres02.vm.provider "virtualbox" do |v|
      v.memory = 1024
      v.cpus = 1
    end
  end

  config.vm.define "odoo01" do |odoo01|
    odoo01.vm.hostname = "odoo01.local.com"
    odoo01.vm.network "private_network", ip: "192.168.0.20"
    odoo01.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/odoo_master.yml"
    end
    odoo01.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 2
    end
  end

  config.vm.define "odoo02" do |odoo02|
    odoo02.vm.hostname = "odoo02.local.com"
    odoo02.vm.network "private_network", ip: "192.168.0.21"
    odoo02.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/odoo.yml"
    end
    config.vm.provider "virtualbox" do |v|
      v.memory = 1024
      v.cpus = 1
    end
  end

  config.vm.define "odoo03" do |odoo03|
    odoo03.vm.hostname = "odoo03.local.com"
    odoo03.vm.network "private_network", ip: "192.168.0.22"
    odoo03.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/odoo.yml"
    end
    config.vm.provider "virtualbox" do |v|
      v.memory = 1024
      v.cpus = 1
    end
  end

  config.vm.define "nginx01" do |nginx01|
    nginx01.vm.hostname = "nginx01.local.com"
    nginx01.vm.network "public_network", ip: "10.0.0.10", bridge: "en1: Wi-Fi (AirPort)"
    nginx01.vm.network "private_network", ip: "192.168.0.10"
    nginx01.vm.network "forwarded_port", guest: 80, host: 8001
    nginx01.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/nginx.yml"
    end
    config.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 1
    end
  end

  config.vm.define "nginx02" do |nginx02|
    nginx02.vm.hostname = "nginx02.local.com"
    nginx02.vm.network "public_network", ip: "10.0.0.11", bridge: "en1: Wi-Fi (AirPort)"
    nginx02.vm.network "private_network", ip: "192.168.0.11"
    nginx02.vm.network "forwarded_port", guest: 80, host: 8002
    nginx02.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/nginx.yml"
    end
    config.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 1
    end
  end


end
