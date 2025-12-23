import streamlit as st
import random
# 先ほど作成した quotes.py を読み込みます
import quotes 
# --- デザイン設定 (ここから追加) ---
st.markdown("""
    <style>
    /* 全体の背景色を優しいパステルブルーに */
    .stApp {
        background: linear-gradient(135deg, #e0f7fa 0%, #fff9c4 100%);
    }
    
    /* ボタンを丸くして色を変える */
    div.stButton > button:first-child {
        background-color: #ff8a65;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    
    /* 名言の表示エリアをカード風にする */
    .stMarkdown h2 {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff8a65;
        color: #455a64;
    }
    </style>
    """, unsafe_allow_stdio=True, unsafe_allow_html=True)
# --- デザイン設定 (ここまで追加) ---
# アプリの設定
st.set_page_config(page_title="ココロのサプリ", page_icon="💊")

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
    
    # 倉庫(quotes.py)からリストを選択
    if "優しく" in q3:
        source_list = quotes.YASASHI
    elif "ガツンと" in q3:
        source_list = quotes.GATUN
    else:
        source_list = quotes.WARAI
    
    # ✨【被り防止】トランプを混ぜるようにシャッフルして1つ選ぶ
    shuffled_quotes = random.sample(source_list, len(source_list))
    selected_quote = shuffled_quotes[0]
    
    # 結果表示
    st.subheader("✨ 今のあなたへの言葉")
    st.markdown(f"## 「 {selected_quote} 」")
    
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
