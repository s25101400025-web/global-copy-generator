import streamlit as st
import google.generativeai as genai

# 1. APIキーの設定（取得したキーをここに貼り付けてください）
# 1. APIキーの設定（Secretsから読み込む）
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# アプリのタイトル
st.set_page_config(page_title="Global Copy Generator", page_icon="✍️")
st.title("🚀 海外プロダクト風コピー生成器")
st.write("商品の特徴を入力するだけで、シリコンバレーのプロダクトのようなキャッチコピーを作ります。")

# 2. 入力フォーム
with st.sidebar:
    st.header("📦 プロダクト情報")
    product_name = st.text_input("プロダクト名", placeholder="例：CodeGuide")
    target_user = st.text_input("ターゲット", placeholder="例：個人開発者、忙しいママ")
    features = st.text_area("主な特徴・売り", placeholder="例：AIが1秒で仕様書を作る、全自動で家計簿をつける")

# 3. 生成ボタン
if st.button("キャッチコピーを生成する"):
    if not GOOGLE_API_KEY:
        st.error("APIキーを正しく入力してください。")
    elif not product_name or not features:
        st.warning("プロダクト名と特徴を入力してください。")
    else:
        with st.spinner("AIが最高のコピーを考案中..."):
            try:
                # 4. AIへの指示（プロンプト）
                model = genai.GenerativeModel('gemini-pro')
                prompt = f"""
                あなたはシリコンバレーの一流コピーライターです。
                以下のプロダクトに対して、海外のテックプロダクト風の洗練されたキャッチコピーを生成してください。
                
                【プロダクト名】: {product_name}
                【ターゲット】: {target_user}
                【特徴】: {features}
                
                以下の形式で出力してください：
                1. 英語のメインコピー（短く、力強く、動詞から始まるようなもの）
                2. 日本語の翻訳（意訳してカッコよく）
                3. プロダクトの説明文（1行）
                """
                
                response = model.generate_content(prompt)
                
                # 結果表示
                st.success("生成が完了しました！")
                st.markdown("---")
                st.subheader("✨ 提案されたコピー")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")

st.markdown("---")
st.caption("Powered by Gemini API | 憧れの海外プロダクトのようなブランディングを。")
