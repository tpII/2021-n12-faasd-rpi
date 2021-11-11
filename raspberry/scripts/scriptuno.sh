#!/bin/bash
# Instalacion containerd / faas-cli / faasd
cd
## Instalar dependencias
apt update
apt install -qy git runc bridge-utils
## Instalar containerd
curl -sSL https://github.com/alexellis/containerd-arm/releases/download/v1.5.4/containerd-1.5.4-linux-armhf.tar.gz | sudo tar -xvz --strip-components=1 -C /usr/local/bin/
wget --output-document=/etc/systemd/system/containerd.service https://raw.githubusercontent.com/containerd/containerd/v1.5.4/containerd.service
systemctl enable containerd
systemctl start containerd.service
## Configurar container networking y CNI plugins
modprobe br_netfilter
sysctl net.bridge.bridge-nf-call-iptables=1
/sbin/sysctl -w net.ipv4.conf.all.forwarding=1
mkdir -p /opt/cni/bin
curl -sSL https://github.com/containernetworking/plugins/releases/download/v1.0.1/cni-plugins-linux-arm-v1.0.1.tgz | tar -xz -C /opt/cni/bin
## Instalar faas-cli
curl -sLfS https://cli.openfaas.com | sh
source <(faas-cli completion --shell bash)
## Instalar faasd
wget --output-document=/usr/local/bin/faasd https://github.com/openfaas/faasd/releases/download/0.14.2/faasd-armhf && chmod +x /usr/local/bin/faasd
export GOPATH=$HOME/go/
mkdir -p $GOPATH/src/github.com/openfaas
cd $GOPATH/src/github.com/openfaas
git clone https://github.com/openfaas/faasd.git
cd faasd/
faasd install
