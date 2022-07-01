# Linux

==== 0622 ====

- Here Document (cat << EOF >> test.txt)

==== 0623 ====

- 자동 완성 기능
- less 명령어: 스크롤 표시하기
- 환경 변수
- 배시 설정 파일
- 쉘에서 bracket 종류에 따른 operations (https://stackoverflow.com/questions/6270440/simple-logical-operators-in-bash)
- 셸 변수
- [쉘 스크립트](https://inpa.tistory.com/entry/LINUX-%EC%89%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%95%B5%EC%8B%AC-%EB%AC%B8%EB%B2%95-%EC%B4%9D%EC%A0%95%EB%A6%AC)
- 표준 입력, 표준 출력, 표준 에러 출력
- /dev
- file descriptor

- 파일 디렉토리 구조
- 리눅스의 디렉터리 구조

## /proc/self

/proc/self의 symbolic link가 어떤 ~~터미널~~프로세스에서 보느냐에 따라 링크된 디렉토리가 다르다.

https://unix.stackexchange.com/questions/333225/which-process-is-proc-self-for

> 즉, /proc/self를 읽으려고 하면(커널 모듈 호출..?) 그때 동적으로 response를 생성해서 보여주는 것??

==== 0624 ====

- 2.3 셸 종류
- tty
- ln 명령어: 링크 만들기
- 파일을 찾는 방법
- 파일의 소유자와 소유 그룹
- 파일의 퍼미션
- 프로세스란
- 잡
- 잡과 프로세스의 종료
- 리다이렉션
- 파이프라인
- awk
- pipe, socket

## socket

[소켓 파일](https://stackoverflow.com/questions/71544605/how-socket-file-actually-works)

소켓은 커널 안에 있는 일종의 네트워크이다. network interface를 통하는 것보다 바로 프로그램 간에 주고받는 것이 빠르기 때문이다.

디스크에 파일을 생성하지만, 소켓은 실제로 디스크에 데이터를 보내지 않고, 커널 메모리에 보유하게 된다. 소켓 파일은 그저 참조하기 위함과 permissions을 통해 접근 제어를 하기 위함이다.

실제로 소켓 파일을 보았을 때 파일 크기가 0이다.

> 그래서 커널 메모리 어디에 저장되는거지? 커널이 알아서 관리하니까 굳이 알 필요가 없는건가?

==== 0627 ====

- /proc
- daemon
- cron
- IPC
- Unix Domain Socket
- cgroup
- chroot

==== 0628 ====

- ssl cert expriry check(https://sh-safer.tistory.com/39)
- 네트워크 명령어

==== 0629 ====

- shell string 처리 (sed, awk, cut, tr 등)
- shell if 없이 분기 처리(http://soopsaram.com/documentudy/2021/10/10/shell-script-without-if-else/)

==== 0630 ====

- [파일이란 무엇인가?](https://sunyzero.tistory.com/260)

  > 10테라 바이트의 정보를 저장할 때 파일 1개로 저장하는 것이 효율적일까? 1TB 10개로 저장하는게 효율적일까? 그것도 아니면 10MB짜리 100만개로 저장하는 것이 효율적일까?

  - 10MB 100만개는 메타데이터의 양이 그만큼 늘어나게 된다. 그래서 비효율 적이다.
  - 10테라 바이트 파일 하나로 저장하기에는 Ext2/3 (4kB block size) 기준 파일의 최대 크기는 2TB이다. 하나의 파일로 저장하기는 어려워보인다.
    > 하지만 XFS에서는 8 EiB 까지 저장된다.
    > 결국 하나의 파일로 저장하는 것이 메타데이터를 줄이기 떄문에 더 효율적인가?

- VFS

==== test ====

## EBS Volume mount

1. (mkfs 로 디바이스 file system 설정) 이미 데이터가 있다면 스킵, 주의
2. mount /dev/DEVICE_NAME /MOUNT_DIRECTORY

## linux list all user

cat /etc/passwd | cut -d ":" -f 1

## DNS host

cat /etc/resolv.conf | grep nameserver | cut -d " " -f 2
