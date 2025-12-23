import streamlit as st
import google.generativeai as genai

# 1. APIキーの設定（Secretsから読み込む）
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Secretsに 'GEMINI_API_KEY' が設定されていません。")
    st.stop()

GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# アプリのタイトル
st.set_page_config(page_title="Global Copy Generator", page_icon="🚀")
st.title("🚀 海外プロダクト風コピー生成器")
st.write("商品の特徴を入力するだけで、シリコンバレーのプロダクトのようなキャッチコピーを作ります。")

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
            # 最新の安定版モデル名を指定
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            あなたは世界的に有名なマーケティングコンサルタントです。
            以下のプロダクトについて、海外（特にシリコンバレー）のスタートアップが使うような、
            シンプルでインパクトのある英語のキャッチコピーと、その日本語訳を3セット提案してください。

            プロダクト名: {product_name}
            ターゲット: {target_user}
            特徴: {features}

            形式：
            ■ 案1
            英語：
            日本語：
            """
            
            with st.spinner('AIが思考中...'):
                # 呼び出し方を最も標準的な形に変更
                response = model.generate_content(prompt)
                
                st.subheader("✨ 生成されたキャッチコピー")
                st.write(response.text)
                st.balloons()
                
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
            st.info("ヒント：APIキーが正しいか、Google AI Studioで有効になっているか確認してください。")

st.markdown("---")
st.caption("Powered by Gemini 1.5 Flash | 海外進出の第一歩を、ここから。")
