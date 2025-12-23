import streamlit as st
import requests

# 1. APIキーの設定（金庫から読み込み）
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Secretsに 'GEMINI_API_KEY' が設定されていません。Settings > Secrets を確認してください。")
    st.stop()

api_key = st.secrets["GEMINI_API_KEY"]

# アプリのタイトル・設定
st.set_page_config(page_title="心に響くコピー生成器", page_icon="✍️")
st.title("✍️ 心に響くコピー生成器")
st.write("機能ではなく「物語」を。あなたのプロダクトに、心に刺さる言葉を添えます。")

# 2. 入力フォーム
with st.sidebar:
    st.header("📦 プロダクトの想い")
    p_name = st.text_input("プロダクト名", placeholder="例：FocusFlow")
    p_target = st.text_input("届けたい相手", placeholder="例：変わりたいと思っているあなたへ")
    p_feat = st.text_area("特徴や込めた願い", placeholder="例：ついついサボってしまう自分を、優しく見守ってくれる")

# 3. 生成ロジック
if st.button("心を動かす言葉を紡ぐ"):
    if not p_name or not p_feat:
        st.warning("プロダクト名と特徴（想い）を入力してください。")
    else:
        # 通信先の設定（最新の安定版 v1 を使用）
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
        
        headers = {'Content-Type': 'application/json'}
        
        # 💡 ここで「ゼクシィ風」の深い指示を出しています
        prompt = f"""
        あなたは日本を代表するコピーライターです。
        「結婚しなくても幸せになれるこの時代に、あなたと結婚したいと思った」というゼクシィの名作コピーのように、
        プロダクトの機能説明ではなく、その裏側にある「人生」「感情」「時代の空気」を捉えた、
        読む人の心に波紋を広げるようなキャッチコピーを提案してください。

        プロダクト名: {p_name}
        届けたい相手: {p_target}
        込めた願い: {p_feat}

        【条件】
        ・「便利」「最高」といった安易な言葉は使わないこと。
        ・読み手が「あ、自分のことだ」と思うような、鋭い洞察を含めること。
        ・日本語の響きの美しさを大切にすること。

        心に響く3つの案を、それぞれの「言葉に込めた物語」と共に提示してください。
        """

        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }
        
        try:
            with st.spinner('言葉を紡いでいます...'):
                response = requests.post(url, headers=headers, json=payload)
                result = response.json()
                
                if response.status_code == 200:
                    output_text = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("成功しました。")
                    st.markdown("---")
                    st.write(output_text)
                    st.balloons()
                else:
                    st.error(f"エラー（{response.status_code}）: キーや設定を確認してください。")
                    st.json(result)
                    
        except Exception as e:
            st.error(f"通信エラーが発生しました: {e}")

st.markdown("---")
st.caption("Produced by Gemini AI | 言葉ひとつで、世界は変わる。")
