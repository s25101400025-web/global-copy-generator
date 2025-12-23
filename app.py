import streamlit as st
import random

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

# 名言データベース
quotes = {
    "優しく": [
        "大丈夫、明日の自分に任せちゃおう。",
        "あなたはもう、十分すぎるくらい頑張っています。",
        "休むことも、立派な仕事のひとつですよ。"
    ],
    "ガツンと": [
        "下を向いていたら、虹を見つけることはできないよ。（チャップリン）",
        "追い込まれた時こそ、新しい自分が生まれるチャンスだ。",
        "とりあえず、温かい飲み物でも飲んでから考えようぜ！"
    ],
    "笑わせて": [
        "人生は近くで見ると悲劇だが、遠くから見れば喜劇だ。（チャップリン）",
        "悩みの9割は、寝て起きたら忘れるように人間はできています（たぶん）。",
        "宇宙の広さに比べたら、今の悩みは豆粒みたいなもんですよ！"
    ]
}

# 3. 診断ボタン
if st.button("サプリを受け取る"):
    st.markdown("---")
    
    if "優しく" in q3:
        target_list = quotes["優しく"]
    elif "ガツンと" in q3:
        target_list = quotes["ガツンと"]
    else:
        target_list = quotes["笑わせて"]
    
    selected_quote = random.choice(target_list)
    
    # ✨ 魔法1：文字を大きく、インパクトのある表示に変更
    st.subheader("✨ 今のあなたへの言葉")
    # st.infoの代わりに Markdownのデカ文字(##) を使用
    st.markdown(f"## 「 {selected_quote} 」")
    
    # 疲れ具合に合わせたメッセージ
    if q1 == "もう限界...":
        st.warning("相当お疲れですね。今日はスマホを置いて、早めに寝ることを強くおすすめします。")
    
    # ✨ 魔法2：風船に加えて「雪」を降らせる演出
    st.balloons()
    st.snow()
    # ツイート用URLの作成（自動で文章が入るようにします）
# 実際のアプリのURL（ここはそのままでOKです）
    my_app_url = "https://global-copy-generator-6gfqravah5oguhql6eoule.streamlit.app/"

    # ✨ ツイート文面のカスタマイズ
    # 「ココロのサプリより」という文言を追加しました
    res_text = f"💊ココロのサプリより今の私への言葉は『{selected_quote}』でした。✨"
    
    # Twitterに送るためのリンクを作成
    tweet_url = f"https://twitter.com/intent/tweet?text={res_text}&url={my_app_url}"
    
    # 画面にリンクを表示
    st.write(f"### [🐦 この結果をツイートする]({tweet_url})")

st.markdown("---")
st.caption("Produced by My First App | 言葉ひとつで、明日はもっと良くなる。")
