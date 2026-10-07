# 오지은 개인 웹사이트

GitHub Pages 정적 사이트. 빌드 과정 없이 파일을 그대로 올리면 됩니다.
공개 주소: https://oje81.github.io · 저장소: https://github.com/oje81/oje81.github.io

## 구성
- `index.html` — 홈 (소개·브리프·기록·약력·연구·용역·발표), 한/영 전환
- `newsletter/` — 국제개발봉사 브리프 아카이브 (`index.html` 목차, `issues/00N.html` 각 호)
- `youth/` — 글로벌 청년정책 브리프 아카이브 (`index.html` 목차, `issues/00N.html` 각 호)
- `notes/` — 기록 탭. `index.html`은 현장 노트 목록(`posts/00N.html`, `_template.html` 새 글 틀), `reading/index.html`은 Reading 목록(`reading/00N.html`)
- `assets/` — `site.css`(디자인), `site.js`(언어 전환), `portrait-2026.jpg`(사진), `notes/`(현장 노트 사진)

폴더마다 `index.html`이 하나씩 있고, 이름이 같아도 자리가 다르면 다른 페이지입니다.
`youth/index.html`은 청년 브리프 목차이고, 맨 위의 `index.html`만 홈입니다.

## 파일 올릴 때 주의
- Claude에서 받은 파일은 브라우저가 `index (1).html`처럼 이름을 바꿔 저장할 때가 있습니다. 올리기 전에 반드시 `index.html`로 이름을 되돌리고, 설명에 적힌 폴더(예: `youth/`)에 들어가서 올립니다.
- 폴더째 끌어다 놓으면 `youth/youth/`처럼 폴더 안에 같은 폴더가 생깁니다. 파일만 올립니다.
- 같은 이름 파일을 같은 자리에 올리면 덮어써집니다. 그것이 수정하는 방법입니다.

## 수정하는 법
- 파일 교체: 해당 폴더에서 `Add file → Upload files` → 같은 이름 파일을 올리고 `Commit changes`
- 한 줄 수정: 파일 열기 → 연필(Edit) 아이콘 → 수정 → `Commit changes`
- 사진 교체: 같은 이름 `assets/portrait-2026.jpg`로 업로드 (세로형, 가로 560px 정도)

## 새 호 추가
1. `newsletter/issues/00N.html` 또는 `youth/issues/00N.html` 업로드
2. 그 폴더의 `index.html`에서 `<ul class="issues">` 맨 위 `<li>`를 복사해 번호·날짜·제목 수정
3. 홈 `index.html`의 최근 호 목록도 수정 (최근 2개 유지)

## 현장 노트 새 글
1. `notes/_template.html`을 복사해 `notes/posts/0NN.html`로 저장하고 내용을 채움 (사진은 `assets/notes/0NN-이름.jpg`)
2. `notes/index.html` 목록 맨 위에 한 줄 추가
3. 홈 `index.html`의 현장 노트 카드는 최근 3개만 유지

## Reading 새 글 (템플릿 고정)
Reading 글의 모양은 `notes/reading/_template.html`로 고정합니다(2026-10-08 확정). 다른 형식으로 만들지 않습니다.
- 판형: 왼쪽 문서 카드(DOCUMENT 상자 + 목차 상자) / 오른쪽 본문. `<body class="reading">`과 `assets/site.css`의 `.reading` 규칙을 그대로 씁니다. 파일 안에 `<style>`을 넣지 않습니다.
- 구조: 세 줄 요약 → 01 문서 개요 → 02 핵심 주장 → 03 제도 설계 분석 → 04 근거의 타당성 → 05 반론과 경쟁 가설 → 06 한국에 주는 시사점 → 평가표 → 주 → 참고문헌. 02~05절 끝에 「판단」 상자.
- 강조: 꼭 기억할 문장은 `<mark>`, 핵심 숫자는 `<b class="num">`. 절마다 한두 번만.
- 상세 노트: 원문 절별 요약·번역은 `notes/reading/00N-notes.html`에 따로 두고 본문 카드에서 링크. 템플릿은 `notes/reading/_template-notes.html`로 고정(본문과 같은 판형, `body class="reading notes-page"`로 색만 청회색). 001-notes.html이 예시.
1. `_template.html`을 복사해 `notes/reading/00N.html`로, `_template-notes.html`을 복사해 `00N-notes.html`로 저장하고 내용을 채움
2. `notes/reading/index.html` 목록 맨 위에 한 줄 추가
3. 홈 `index.html`의 Reading 카드는 최근 3개만 유지
