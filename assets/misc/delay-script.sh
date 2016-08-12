#!/bin/bash

usage() {
	echo "Usage: delay-script.sh <add/change/replace/change/del/show> <delay ms> [variation] [correlation]"
}

DEVICES="eth0 eth1"

OP=$1
DELAY=$2

if [ -z "$OP" ]; then 
	usage
	exit 1
fi

if [ -z "$DELAY" ] && [ "$OP" != "show" ]; then
	usage
	exit 1
fi

if [ -z "$3" ]; then
        VAR="10"
else
        VAR=$3
fi

if [ -z "$4" ]; then
	CORR="25"
else
	CORR=$4
fi

modprobe ifb
DEVCOUNT=0

# args: dev, ifb index
show() {
	tc qdisc show dev $1
	tc qdisc show dev ifb${2}
}

if [ "$OP" != "show" ] ; then 
	echo "Min Delay: $DELAY ms"
	echo "Variation: $VAR"
	echo "Correlation: $CORR"
fi

for DEV in $DEVICES; do 
	if [ "$OP" == "show" ]; then
		show $DEV $DEVCOUNT
		exit 0
	fi
	
	if [ "$OP" != "del" ]; then 
		ip link set dev ifb${DEVCOUNT} up
		tc qdisc add dev $DEV ingress
		tc filter add dev $DEV parent ffff: \
		protocol ip u32 match u32 0 0 flowid 1:1 action mirred egress redirect dev ifb${DEVCOUNT}
	fi

	IFBCOM="tc qdisc $OP dev ifb${DEVCOUNT} root netem delay ${DELAY}ms $VAR ${CORR}%"
	COM="tc qdisc $OP dev $DEV root netem delay ${DELAY}ms $VAR ${CORR}%"
	
	echo $IFBCOM
	echo $COM
	`$COM`
       	`$IFBCOM`
	show $DEV $DEVCOUNT


	if [ "$OP" == "del" ]; then
		# not sure all of this is necessary.  'filter del' always has error.
                tc filter del dev $DEV parent ffff:
		tc qdisc del dev $DEV ingress
		ip link set dev ifb${DEVCOUNT} down
        fi

	DEVCOUNT=$((DEVCOUNT + 1))
done
