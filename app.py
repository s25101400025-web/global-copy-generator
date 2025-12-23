import streamlit as st
import google.generativeai as genai

# 1. APIキーの設定
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Secretsに 'GEMINI_API_KEY' が設定されていません。")
    st.stop()

# 💡 ここで最新の通信方式を強制指定します
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="Global Copy Generator")
st.title("🚀 海外プロダクト風コピー生成器")

# 2. 入力フォーム
with st.sidebar:
    st.header("📦 プロダクト情報")
    p_name = st.text_input("プロダクト名")
    p_target = st.text_input("ターゲット")
    p_feat = st.text_area("特徴")

# 3. 生成ロジック
if st.button("キャッチコピーを生成する"):
    if not p_name or not p_feat:
        st.warning("情報を入力してください。")
    else:
        try:
            # 最新のフラッシュモデルを指定
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"プロダクト名「{p_name}」、ターゲット「{p_target}」、特徴「{p_feat}」に基づき、シリコンバレー風の英語コピーと日本語訳を3つ作成して。"
            
            with st.spinner('AIが回答を作成中...'):
                response = model.generate_content(prompt)
                st.success("成功！")
                st.write(response.text)
                st.balloons()
        except Exception as e:
            st.error(f"エラーが発生しました。設定を再確認してください。")
            st.code(str(e)) # エラーの詳細を表示
