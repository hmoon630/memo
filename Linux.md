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
- 리눅스는 파일로 구성된다
- 리눅스의 디렉터리 구조

## /proc/self

/proc/self의 symbolic link가 어떤 ~~터미널~~프로세스에서 보느냐에 따라 링크된 디렉토리가 다르다.

https://unix.stackexchange.com/questions/333225/which-process-is-proc-self-for

> > 즉, /proc/self를 읽으려고 하면(커널 모듈 호출..?) 그때 동적으로 response를 생성해서 보여주는 것??

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
- wc 명령어: 바이트 수, 단어 수, 행 수 세기
- sort 명령어: 행 단위로 정렬하기
- uniq 명령어: 중복 제거하기
- cut 명령어: 입력의 일부 추출하기
- tr 명령어: 문자 교환과 삭제하기
- tail 명령어: 마지막 부분 출력하기
- diff 명령어: 차이 출력하기
- sed 명령어: 스트림 에디터
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

==== todo ====

- grep, 정규식
- 네트워크 명령어
-
