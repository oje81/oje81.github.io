# 오지은 개인 웹사이트 + 국제개발봉사 브리프 아카이브

GitHub Pages용 정적 사이트입니다. 빌드 과정 없이 그대로 올리면 됩니다.

## 구성
- `index.html` — 홈 (소개·약력·연구·브리프 최근 호), 한/영 전환
- `newsletter/index.html` — 브리프 전체 아카이브
- `newsletter/issues/001.html`, `002.html` — 각 호 원본 (상단에 아카이브 이동·PDF 저장 버튼 추가)
- `assets/site.css`, `assets/site.js` — 공통 디자인·언어 전환

## 새 호 추가하는 법 (격주)
1. 새 호 HTML을 `newsletter/issues/003.html`로 올린다
2. `newsletter/index.html`의 `<ul class="issues">` 맨 위에 `<li>` 한 줄을 복사해 번호·날짜·제목을 바꾼다
3. 홈 `index.html`의 최근 호 목록도 같이 바꾼다 (최근 2개만 유지)

## 확인할 것
- 학술논문: 지방정부연구(2024)·국제학논총(2020) 제목은 웹 검색으로 찾은 것 → 확인 필요
- 한국자치행정학보(2024), 한국진로창업경영학회지(2024), 평화와지역연구(2022), KAIDEC 논문집(2025.12) 제목 추가 필요
