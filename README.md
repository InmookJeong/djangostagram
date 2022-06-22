# Project Djangostagram
- 패스트캠퍼스(국비지원과정) Python & Dajngo
- Django를 사용한 장고스타그램 플랫폼 만들기

# 프로젝트 과제 요구사항
- 사용자 관리
    - 비밀번호는 hashers를 사용해 암호화하여 저장하기
- 공통 템플릿
    - base.html 템플릿 생성
    - 모든 페이지에서 base.html 상속받기
    - 로그인 상태에 따른 상단 네비게이션 UI 구분
        - 로그인이 안된 경우 '타임라인', '회원가입', '로그인' 메뉴 출력
        - 로그인이 된 경우 '타임라인', '로그아웃', '글 작성' 메뉴 출력
- 회원가입 페이지
    - 아이디, 이메일, 비밀번호, 비밀번호 확인 정보 필수 입력
    - 비밀번호, 비밀번호 확인 값 일치 여부 확인
    - 회원가입 완료 시 메인 화면으로 이동
- 로그인 페이지
    - 아이디 검증 : 없는 경우 '아이디가 없습니다.' Error 발생
    - 비밀번호 검증 : 틀린 경우 '비밀번호가 틀렸습니다.' Error 발생
    - 로그인 성공 시 메인 화면으로 이동