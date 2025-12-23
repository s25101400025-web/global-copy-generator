import streamlit as st
import google.generativeai as genai

# 1. APIキーの設定（Secretsから読み込む）
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Secretsに 'GEMINI_API_KEY' が設定されていません。")
    st.stop()

# APIの通信設定を最新の安定版に固定します
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# アプリのタイトル
st.set_page_config(page_title="Global Copy Generator", page_icon="🚀")
st.title("🚀 海外プロダクト風コピー生成器")

# 2. 入力フォーム
with st.sidebar:
    st.header("📦 プロダクト情報")
    product_name = st.text_input("プロダクト名", placeholder="例：ZenStep")
    target_user = st.text_input("ターゲット", placeholder="例：忙しい会社員")
    features = st.text_area("主な特徴・売り", placeholder="例：AIが1分間の瞑想をガイドする")

# 3. 生成ロジック
if st.button("キャッチコピーを生成する"):
    if not product_name or not features:
        st.warning("プロダクト名と特徴を入力してください。")
    else:
        try:
            # モデルの呼び出し方を最新の安定版に合わせます
            model = genai.GenerativeModel(model_name='gemini-1.5-flash')
            
            prompt = f"プロダクト名「{product_name}」、ターゲット「{target_user}」、特徴「{features}」について、海外スタートアップ風の英語コピーと日本語訳を3案出してください。"
            
            with st.spinner('AIが考え中...'):
                # 通信エラーを防ぐため、最もシンプルな呼び出しに変更
                response = model.generate_content(prompt)
                
                st.subheader("✨ 生成されたキャッチコピー")
                st.write(response.text)
                st.balloons()
                
        except Exception as e:
            st.error(f"エラーが発生しました。時間を置いて再度お試しください。")
            st.info(f"技術的な詳細: {e}")

st.markdown("---")
st.caption("Powered by Gemini 1.5 Flash")
