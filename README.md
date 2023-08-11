This repository was made by myself to make RPI dashboard.

It mainly uses Flask to run the web server and connect between python and HTML.
RPI's sensor values can be loaded to webpage using psutil.

https://opensource.com/article/23/3/build-raspberry-pi-dashboard-appsmith

I've got many helps while reading this article. I changed some code, also not using Appsmith API.
Other codes were referred to official/other helpful wikis. (flask, psutil etc.)


Objective
	- Display RPI's temperature, RAM usage, CPU usage, disk usage
	- Personal memo. (aka. daily garbage thought disposal like Twitter) It can save text and image files. Will be implemented with SQL languages.
	- Drawing pad. It uses a 3.5" GPIO touchscreen(not that precise like smartphones). Will be implemented with javascript. (If I could)
	- Managing game servers. It will launch a batch file to find the current process, turning on/off with click.



이 리포지토리는 라즈베리파이를 대시보드/웹서버 화 시키기 위하여 제작된 개인 프로젝트입니다.

Flask를 이용하여 웹페이지를 만들고 psutil을 이용하여 라즈베리파이의 센서 정보를 불러옵니다.

https://opensource.com/article/23/3/build-raspberry-pi-dashboard-appsmith

위 링크에서 많은 도움을 얻었으며 후반부 대시보드화에서 제공된 사이트를 사용하지 않고 개인 서버를 만들어서 변형을 시켰습니다.
다른 코드는 다양한 예제와 공식 위키를 참조하여 작성했습니다.


목표
	- 라즈베리파이의 온도, RAM 사용량, CPU 사용량, 디스크 사용량 정보 제공
	- 개인 메모장. 텍스트와 사진 파일을 저장/불러오기 가능하며 수정 가능, SQL 데이터베이스 사용 예정
	- 그림판 기능. 위 메모장과 합쳐진 기능이며 3.5인치 터치스크린을 이용하여 간단한 그림 그리기 가능. 자바스크립트로 구현 예정
	- 실행중인 게임 서버 시작/종료 기능. 배치 파일을 사용하여 프로세스 시작, 실행중인 프로세스 종료 구현 예정.


