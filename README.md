django를 활용하여 간단한 쇼핑몰 로직을 구현한 프로젝트입니다.
폼클래스를 활용한 클래스 기반 뷰를 통해 웹페이지를 렌더링하는 방식으로 구현했으나,
일부 URL에 대해서는 DRF + rest api를 활용하여 Response json data를 사용해 ajax로 프론트엔드에서 활용했습니다.(/api/product, /api/product/<int:pk>)

본 프로젝트를 통해 django의 구조를 이해하고 클래스들을 사용해볼 수 있었고, 세션처리에 대한 기본적인 이해, DRF의 활용, rest api의 목적과 기초들을 학습할 수 있었습니다.

구현로직
- 로그인
- 로그아웃
- 회원가입
- 상품보기
- 주문보기
- 상품등록

활용기술
- python
- django
- html
- virtualenv
- DRF(django rest framework)
- jquery/ajax (product.html의 마우스 오버)
