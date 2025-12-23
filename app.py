import streamlit as st
import random
import quotes 

# アプリの設定
st.set_page_config(page_title="ココロのサプリ", page_icon="💊")

# --- ✨ デザイン設定（修正版） ---
st.markdown("""
    <style>
    /* 全体の背景色を優しいグラデーションに */
    .stApp {
        background: linear-gradient(135deg, #e0f7fa 0%, #fff9c4 100%);
    }
    
    /* ボタンを丸くして色を変える */
    div.stButton > button:first-child {
        background-color: #ff8a65 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
    }
    
    /* 名言の表示エリアを白背景のカード風にする */
    .quote-card {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 25px;
        border-radius: 15px;
        border-left: 8px solid #ff8a65;
        margin: 20px 0;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💊 ココロのサプリ")
st.write("今のあなたにぴったりの言葉を届けます。")

# 1. 質問コーナー
st.header("今のことを少し教えてください")

q1 = st.select_slider(
    "1. 今、どれくらいお疲れですか？",
    options=["元気！", "ちょっと疲れ気味", "かなりヘトヘト", "もう限界..."]
)

q2 = st.selectbox(
    "2. 何について悩んでいますか？",
    ["人間関係", "将来のこと", "仕事や勉強", "なんとなく不安", "特にないけど元気が出ない"]
)

q3 = st.radio(
    "3. どんな風に声をかけてほしいですか？",
    ["優しく包み込んでほしい", "背中をガツンと押してほしい", "クスッと笑わせてほしい"]
)

# 2. 診断ボタン
if st.button("サプリを受け取る"):
    st.markdown("---")
    
    if "優しく" in q3:
        source_list = quotes.YASASHI
    elif "ガツンと" in q3:
        source_list = quotes.GATUN
    else:
        source_list = quotes.WARAI
    
    shuffled_quotes = random.sample(source_list, len(source_list))
    selected_quote = shuffled_quotes[0]
    
    # ✨ 結果表示（カード風デザインを適用）
    st.subheader("✨ 今のあなたへの言葉")
    st.markdown(f"""
        <div class="quote-card">
            <h2 style='color: #455a64; margin: 0;'>「 {selected_quote} 」</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # ツイート用設定
    my_app_url = "https://global-copy-generator-6gfqravah5oguhql6eoule.streamlit.app/"
    res_text = f"💊ココロのサプリより今の私への言葉は『{selected_quote}』でした。✨"
    tweet_url = f"https://twitter.com/intent/tweet?text={res_text}&url={my_app_url}"
    
    st.write(f"### [🐦 この結果をツイートする]({tweet_url})")
    
    if q1 == "もう限界...":
        st.warning("相当お疲れですね。今日はスマホを置いて、早めに寝ることを強くおすすめします。")
    
    st.balloons()
    st.snow()

st.markdown("---")
st.caption("Produced by My First App | 言葉ひとつで、明日はもっと良くなる。")
