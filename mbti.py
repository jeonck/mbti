# mbti.py
import streamlit as st

def mbti():
    # 질문과 답변 목록
    questions = [
        {"id": 1, "text": "사교적이며 사람들과 함께 시간을 보내는 것을 좋아합니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 2, "text": "계획을 세우고 조직화하는 것을 좋아합니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 3, "text": "결정을 내릴 때 논리와 사실에 기반합니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 4, "text": "새로운 아이디어나 가능성에 대해 생각하는 것을 즐깁니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 5, "text": "다른 사람들의 감정에 민감합니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 6, "text": "갑작스러운 변화나 예기치 않은 상황에 잘 적응합니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 7, "text": "혼자서 생각하고 시간을 보내는 것을 좋아합니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 8, "text": "주어진 규칙과 절차를 따르는 것을 선호합니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 9, "text": "감정적이고 직관적인 결정을 자주 내립니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 10, "text": "현실적이고 구체적인 것들에 집중합니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 11, "text": "다른 사람들과 상호작용할 때 에너지를 얻습니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 12, "text": "조직적이고 체계적인 접근 방식을 선호합니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 13, "text": "논리적이고 분석적인 사고를 즐깁니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 14, "text": "미래에 대한 상상과 꿈을 즐깁니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 15, "text": "다른 사람들과 공감하는 능력이 뛰어납니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 16, "text": "유연하고 적응력이 좋습니다.", "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 17, "text": "대화를 통해 생각을 정리하는 편입니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 18, "text": "구체적인 사실과 세부 사항을 중시합니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 19, "text": "감정이 아닌 논리에 따라 결정을 내립니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}},
        {"id": 20, "text": "직관에 따라 행동하는 편입니다.",
         "options": {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": -1, "전혀 그렇지 않다": -2}}
    ]

    # MBTI 유형 설명
    mbti_descriptions = {
        "ISTJ": "신중하고 책임감이 강하며, 실용적이고 체계적인 접근을 선호합니다.",
        "ISFJ": "세심하고 배려심이 많으며, 다른 사람을 돕는 것을 좋아합니다.",
        "INFJ": "통찰력 있고 창의적이며, 깊이 있는 인간관계를 추구합니다.",
        "INTJ": "독립적이고 분석적이며, 전략적으로 목표를 설정하고 달성합니다.",
        "ISTP": "논리적이고 현실적이며, 문제 해결에 능숙합니다.",
        "ISFP": "조용하고 친근하며, 예술적 감각이 뛰어납니다.",
        "INFP": "이상적이고 충성심이 강하며, 깊은 감정을 가지고 있습니다.",
        "INTP": "호기심이 많고 논리적이며, 새로운 아이디어를 탐구하는 것을 좋아합니다.",
        "ESTP": "활발하고 모험적이며, 즉각적인 문제 해결을 선호합니다.",
        "ESFP": "사교적이고 유쾌하며, 다른 사람들과 함께 있는 것을 즐깁니다.",
        "ENFP": "열정적이고 창의적이며, 새로운 가능성을 탐색합니다.",
        "ENTP": "논쟁을 즐기고, 새로운 아이디어를 발전시키는 것을 좋아합니다.",
        "ESTJ": "현실적이고 조직적이며, 목표 달성을 위해 노력합니다.",
        "ESFJ": "친절하고 사교적이며, 다른 사람을 돕는 것을 좋아합니다.",
        "ENFJ": "카리스마 있고 공감 능력이 뛰어나며, 사람들에게 영감을 줍니다.",
        "ENTJ": "결단력 있고 지도력이 뛰어나며, 목표 달성을 위해 노력합니다."
    }

    def calculate_mbti(answers):
        E = sum([answers[i] for i in [0, 6, 10, 16]])
        I = -E
        S = sum([answers[i] for i in [3, 9, 13, 17]])
        N = -S
        T = sum([answers[i] for i in [2, 8, 12, 18]])
        F = -T
        J = sum([answers[i] for i in [1, 7, 11, 15, 19]])
        P = -J

        personality = ''
        personality += 'E' if E > 0 else 'I'
        personality += 'S' if S > 0 else 'N'
        personality += 'T' if T > 0 else 'F'
        personality += 'J' if J > 0 else 'P'

        return personality

    # 현재 질문의 인덱스를 저장할 변수 초기화
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0

    # 사용자 답변 저장할 리스트 초기화
    if 'answers' not in st.session_state:
        st.session_state.answers = []

    st.title('MBTI 성격 유형 테스트')
    st.write('각 질문에 답변하고 MBTI 성격 유형을 확인하세요.')

    # 현재 질문 가져오기
    current_question = st.session_state.current_question

    if current_question < len(questions):
        question = questions[current_question]

        st.markdown(f"<h3 style='font-size:20px'>{question['text']}</h3>", unsafe_allow_html=True)

        with st.form(key='question_form'):
            answer = st.radio('질문에 대한 답변을 선택해주세요:', list(question["options"].keys()), index=0)  # 기본값을 첫 번째 옵션으로 설정
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                submit_button = st.form_submit_button(label='다음')
            with col2:
                previous_button = st.form_submit_button(label='이전')

        st.write(f"질문 {current_question + 1} / {len(questions)}")  # 진행 상황 표시

        if previous_button:
            if st.session_state.current_question > 0:
                st.session_state.current_question -= 1
                st.session_state.answers.pop()  # 이전 질문으로 돌아갈 때 마지막 답변 삭제
            st.rerun()  # 이전 버튼 클릭 시 페이지 새로고침

        if submit_button:
            if answer is not None:  # 답변이 선택된 경우에만 진행
                if len(st.session_state.answers) > current_question:
                    st.session_state.answers[current_question] = question["options"][answer]
                else:
                    st.session_state.answers.append(question["options"][answer])
                st.session_state.current_question += 1
                st.rerun()  # 폼 제출 후 페이지 새로고침
            else:
                st.warning("옵션을 선택하세요.")

    else:
        personality = calculate_mbti(st.session_state.answers)
        description = mbti_descriptions[personality]
        st.subheader(f'당신의 MBTI 성격 유형: {personality}')
        st.write(description)

        # 재시작 버튼
        if st.button('다시 시작'):
            st.session_state.current_question = 0
            st.session_state.answers = []
            st.rerun()  # 페이지 새로고침하여 초기화

# Streamlit 앱 실행
if __name__ == '__main__':
    mbti()
