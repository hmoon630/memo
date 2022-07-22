# Storage services of AWS

## 0718

- storage concepts(EBS, EFS, S3)
- Block vs File vs Object Storage
- [AWS Storage Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/74237958-77c8-4e7f-a02f-ae201a04d759/en-US) - Lab 1

## 0719

- [AWS Storage Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/74237958-77c8-4e7f-a02f-ae201a04d759/en-US) - Lab 2, 3, 4
- concepts(data sync, backup, storage gateway)
- s3 presigned url - [boto3](server/main.py)

## 0720

- [pirate s3 game](http://s3game-level1.s3-website.us-east-2.amazonaws.com/level1.html)
- [galaxy s3 game](http://s3game-galaxy-level1.s3-website.us-east-2.amazonaws.com/)

## 0721

- [galaxy s3 game](http://s3game-galaxy-level1.s3-website.us-east-2.amazonaws.com/)

## 0722

- [Accelerate your content using Amazon CloudFront](https://catalog.us-east-1.prod.workshops.aws/workshops/9331108e-464e-4699-8a9c-486090105878/en-US/10-create-ec2-and-s3-origins)
- Cloudfront Alternative domain name
- strong consistency
- versioning

### questions

> s3에 static web hosting이 있지만, cloudfront와 연계해서 사용하면 굳이 기능을 사용할 이유가 없다. 그럼 단독으로 static web hosting을 할 이유가 있을까?

- 일단 성능과 비용 측면에서 보면 당연히 cloudfront 쪽이 우세할 것이다. cloudfront의 캐싱으로 trasnfer 비용도 줄어들고, 응답 시간도 줄어들 것이다.

## todo

- EBS
- EFS
- Glacier
- Storage gateway
- FSx
- AWS backup

- S3
  - class 간 transfer
  - s3 backup
  - cross account policy
  -
