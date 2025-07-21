import streamlit as st

st.title("Streamlit 요소 예시 페이지")  # ① 페이지 제목

st.header("헤더 예시")  # ② 헤더

st.subheader("서브헤더 예시")  # ③ 서브헤더

st.text("텍스트 예시입니다.")  # ④ 일반 텍스트

st.markdown("**마크다운 예시**: _굵게, 이탤릭, 링크 등 지원합니다._")  # ⑤ 마크다운

st.code("print('Hello, Streamlit!')", language='python')  # ⑥ 코드 블록

st.latex(r"\int_a^b f(x)dx")  # ⑦ LaTeX 수식

st.write("write 함수는 다양한 타입을 자동으로 렌더링합니다.", {"key": "value"})  # ⑧ write 함수

st.success("성공 메시지입니다!")  # ⑨ 성공 메시지

st.info("정보 메시지입니다!")  # ⑩ 정보 메시지

st.warning("경고 메시지입니다!")  # ⑪ 경고 메시지

st.error("에러 메시지입니다!")  # ⑫ 에러 메시지

st.image("https://static.streamlit.io/examples/dog.jpg", caption="이미지 예시")  # ⑬ 이미지

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # ⑭ 오디오

st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # ⑮ 비디오

st.checkbox("체크박스 예시")  # ⑯ 체크박스

st.radio("라디오 버튼 예시", ["옵션 1", "옵션 2", "옵션 3"])  # ⑰ 라디오 버튼

st.selectbox("셀렉트박스 예시", ["A", "B", "C"])  # ⑱ 셀렉트박스

st.multiselect("멀티셀렉트 예시", ["Python", "Java", "C++"])  # ⑲ 멀티셀렉트

st.slider("슬라이더 예시", 0, 100, 50)  # ⑳ 슬라이더

st.number_input("숫자 입력 예시", min_value=0, max_value=100, value=10)  # ㉑ 숫자 입력

st.text_input("텍스트 입력 예시")  # ㉒ 텍스트 입력

st.text_area("텍스트 영역 예시")  # ㉓ 텍스트 영역

st.date_input("날짜 입력 예시")  # ㉔ 날짜 입력

st.time_input("시간 입력 예시")  # ㉕ 시간 입력

st.file_uploader("파일 업로더 예시")  # ㉖ 파일 업로더

st.button("버튼 예시")  # ㉗ 버튼

st.sidebar.title("사이드바 제목")  # ㉘ 사이드바 제목

st.sidebar.button("사이드바 버튼")  # ㉙ 사이드바 버튼

st.progress(70)  # ㉚ 진행률 바

st.spinner("로딩 중...")  # ㉛ 스피너

import pandas as pd
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
st.table(df)  # ㉜ 테이블

st.dataframe(df)  # ㉝ 데이터프레임

st.metric(label="온도", value="25°C", delta="1°C")  # ㉞ 메트릭

st.caption("이것은 캡션입니다.")  # ㉟ 캡션

st.divider()  # ㊱ 구분선

# 각주
st.markdown("""
---
① st.title: 페이지의 제목을 표시합니다.  
② st.header: 큰 헤더를 표시합니다.  
③ st.subheader: 작은 헤더를 표시합니다.  
④ st.text: 일반 텍스트를 표시합니다.  
⑤ st.markdown: 마크다운 형식의 텍스트를 표시합니다.  
⑥ st.code: 코드 블록을 표시합니다.  
⑦ st.latex: LaTeX 수식을 표시합니다.  
⑧ st.write: 다양한 타입의 데이터를 자동으로 렌더링합니다.  
⑨~⑫: 성공, 정보, 경고, 에러 메시지를 표시합니다.  
⑬ st.image: 이미지를 표시합니다.  
⑭ st.audio: 오디오를 재생합니다.  
⑮ st.video: 비디오를 재생합니다.  
⑯~㉗: 다양한 입력 위젯(체크박스, 라디오, 셀렉트박스, 슬라이더 등)을 표시합니다.  
㉘~㉙: 사이드바에 요소를 표시합니다.  
㉚ st.progress: 진행률 바를 표시합니다.  
㉛ st.spinner: 로딩 스피너를 표시합니다.  
㉜ st.table: 테이블을 표시합니다.  
㉝ st.dataframe: 데이터프레임을 표시합니다.  
㉞ st.metric: 메트릭(지표)을 표시합니다.  
㉟ st.caption: 캡션(설명)을 표시합니다.  
㊱ st.divider: 구분선을 표시합니다.
""")