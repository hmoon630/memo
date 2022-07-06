# VPC

## 0704

- vpc concepts(subnet, route table, igw, EIP)
- Peering vs Transit Gateway
  - 대역폭 제한 x vs 50Gbps
  - VPC당 구성 가능 개수 125 vs 5000
  - 연결 비용 x vs $0.07 per hour
  - vpn 사용시 각각 연결 vs Transit Gateway에만 연결(Peering에서 각 vpn 연결에서 비용 발생)
  - Transit Gateway가 더 간단한 구성을 제공하나 추가 요금 발생 & 대역폭 제한
- Outpost / Wavelength / Local Zone

### questions

> ec2 or aws resources 에 Public(or Private) Ipv4 DNS가 붙는 이유는?

단순 ip 대신 DNS를 사용하여 region이나 resource type을 확인할 수 있기 때문인가?

> [RFC 1918](http://www.faqs.org/rfcs/rfc1918.html): 기존에는 VPC Ipv4 CIDR로 10.0.0.0/8이 가능했지만 이젠 netmask가 /16 ~ /28만 가능하다. 바뀐 이유는?

[2022/07/01 구글 캐시](https://webcache.googleusercontent.com/search?q=cache:ypgXp8wp7mYJ:https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/VPC_Subnets.html+&cd=1&hl=ko&ct=clnk&gl=kr) 이 당시엔 /8 netmask에 관한 내용이 공식 document에 있었다. 3일 사이에 변경이 있었던 것?

## 0705

- vpc concepts(NAT, Peering, Transit gateway)
- Transit Gateway
  - [Connecting Overlapping VPCs with Private NAT](https://cloudnetworks.io/2021-07-12-private-nat-overlapping/)
    - 각 VPC에 public subnet과 ec2 구성
    - 각 VPC에 2번째 CIDR 대역을 부여한 후 그 대역에 private subnet을 구성
    - 각 private subnet을 tgw에 attach
    - Source VPC private subnet에 NAT를 구성
    - Destination VPC private subnet에 nlb를 구성하여 target EC2에 접근
    - Source VPC ec2에서 nlb로 접속
- VPC Peering
  - [One VPC peered to specific subnets in two VPCs](https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations-partial-access.html#one-to-two-vpcs-specific-subnets)
    - A, C VPC cidr = 10.0.0.0/16, B VPC cidr = 172.16.0.0/16
    - A, B, C에 ec2 인스턴스 1개씩 구성, A만 퍼블릭
    - A > B > C 순으로 ssh 접근
    - B subnet의 rtb에서는 A의 10.0.aa.0/24로 피어링, C의 10.0.cc.0/24로 피어링
    - 서브넷 대역도 같다면 A의 10.0.0.aa/32로 피어링, C의 10.0.0.cc/32로 피어링

### questions

> NLB가 ICMP 중에서 Type3(Destination unreachable)을 제외한 메시지를 unintended traffic으로 간주한다. 그렇게 하는 이유는?

ICMP를 이용한 DDOS를 방어하기 위한것? [Shoud I block ICMP](http://shouldiblockicmp.com/)

> Peering은 별도의 장비를 사용하지 않고 기존의 장비만으로 서비스 된다고 한다. 그렇다면 어떻게 다른 VPC로의 트래픽을 허용/차단 하는 것인가? Peering Connection을 생성함으로서 허용해주는 정책이 생성되는 것인가?

## 0706

- private link
- Endpoints (gateway, interface of S3)
- [vpc endpoint service workshop](https://networking.workshop.aws/intermediate/5-vpc-endpoint-services/10-vpc-endpoint-services-overview.html)

## todo

- gateway loadbalancer
- ACL
- security groups
- Firewall
- VPN
- Transit gateway multicast
- Traffic mirroring
- subnet prefix