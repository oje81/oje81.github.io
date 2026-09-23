# 오지은 개인 웹사이트 + 국제개발봉사 브리프 아카이브

GitHub Pages 정적 사이트. 빌드 없이 파일을 그대로 올리면 됩니다.
공개 주소: https://oje81.github.io · 저장소: https://github.com/oje81/oje81.github.io

## 구성
- `index.html` — 홈 (소개·약력·연구·용역·발표·브리프), 한/영 전환
- `newsletter/index.html` — 브리프 전체 아카이브
- `newsletter/issues/001.html`, `002.html` — 각 호 원본
- `assets/site.css`, `assets/site.js`, `assets/portrait.jpg` — 디자인·언어 전환·사진

## 수정하는 법
- 파일 교체: 저장소에서 `Add file → Upload files` → 같은 이름 파일을 올리고 `Commit changes` (덮어쓰기)
- 한 줄 수정: 파일 열기 → 연필(Edit) 아이콘 → 수정 → `Commit changes`
- 사진 교체: 같은 이름 `assets/portrait.jpg`로 업로드 (세로형 권장, 가로 560px 정도)

## 새 호 추가 (격주)
1. `newsletter/issues/003.html` 업로드
2. `newsletter/index.html`의 `<ul class="issues">` 맨 위 `<li>` 복사해 번호·날짜·제목 수정
3. 홈 `index.html`의 최근 호 목록도 수정 (최근 2개 유지)
