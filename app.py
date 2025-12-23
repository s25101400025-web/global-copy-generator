import streamlit as st
import random
import quotes 

# アプリの設定
st.set_page_config(page_title="ココロのサプリ", page_icon="💊")

# --- ✨ 目に優しい黄緑デザイン設定 ---
st.markdown("""
    <style>
    /* 1. 全体の背景：目に優しい淡い黄緑のグラデーション */
    .stApp {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    }
    
    /* 2. 文字の色を濃くして読みやすくする */
    h1, h2, h3, p, span, label {
        color: #166534 !important; /* 濃い緑色 */
        font-weight: 600;
    }

    /* 3. ボタンのデザイン：視認性の高いオレンジ */
    div.stButton > button:first-child {
        background-color: #16a34a !important; /* 濃いめの緑 */
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 12px 24px !important;
        font-size: 18px !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    
    /* 4. 名言を表示するカード：白背景で文字を際立たせる */
    .quote-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #bbf7d0;
        margin: 25px 0;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.05);
        text-align: center;
    }
    
    .quote-text {
        color: #15803d !important;
        font-size: 24px !important;
        line-height: 1.6;
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
    
    # ✨ 結果表示：白いカードの中に濃い緑の文字で表示
    st.subheader("✨ 今のあなたへの言葉")
    st.markdown(f"""
        <div class="quote-card">
            <div class="quote-text">「 {selected_quote} 」</div>
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
