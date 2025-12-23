import streamlit as st
import requests

# 1. APIキーの設定
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Secretsに 'GEMINI_API_KEY' が設定されていません。")
    st.stop()

api_key = st.secrets["GEMINI_API_KEY"]

# アプリの設定
st.set_page_config(page_title="心に響くコピー生成器", page_icon="✍️")
st.title("✍️ 心に響くコピー生成器")

# 2. 入力フォーム
with st.sidebar:
    st.header("📦 プロダクトの想い")
    p_name = st.text_input("プロダクト名", value="ミライポスト")
    p_target = st.text_input("届けたい相手", value="20年後の自分へ手紙を書きたい人")
    p_feat = st.text_area("特徴や込めた願い", value="忘れたくない「今」を未来に届けるサービス。")

# 3. 生成ロジック
if st.button("心を動かす言葉を紡ぐ"):
    if not p_name or not p_feat:
        st.warning("情報を入力してください。")
    else:
        # 💡 【重要】確実に動く「v1beta」と「gemini-1.5-flash」の組み合わせに固定します
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        
        headers = {'Content-Type': 'application/json'}
        
        prompt = f"""
        あなたは日本を代表するコピーライターです。
        ゼクシィの広告コピーのように、人生の機微に触れる深いキャッチコピーを提案してください。
        機能の説明ではなく、その先にある感情を言葉にしてください。

        プロダクト名: {p_name}
        相手: {p_target}
        想い: {p_feat}
        """

        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        
        try:
            with st.spinner('言葉を紡いでいます...'):
                response = requests.post(url, headers=headers, json=payload)
                result = response.json()
                
                if response.status_code == 200:
                    output_text = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("成功しました！")
                    st.markdown("---")
                    st.write(output_text)
                    st.balloons()
                else:
                    # エラーメッセージを分かりやすく表示
                    error_msg = result.get('error', {}).get('message', '不明なエラー')
                    st.error(f"エラーが発生しました（コード: {response.status_code}）")
                    st.write(f"原因: {error_msg}")
                    st.info("APIキーが正しく貼り付けられているか、もう一度確認してみてください。")
                    
        except Exception as e:
            st.error(f"接続エラー: {e}")
