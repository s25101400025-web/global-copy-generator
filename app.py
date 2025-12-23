# --- 修正後のコード (if st.button の中身) ---

if st.button("サプリを受け取る"):
    st.markdown("---")
    
    # 1. 倉庫からリストを持ってくる
    if "優しく" in q3:
        source_list = quotes.YASASHI
    elif "ガツンと" in q3:
        source_list = quotes.GATUN
    else:
        source_list = quotes.WARAI
    
    # 2. ✨【ここがポイント】リストをコピーしてバラバラに混ぜる
    # sample を使うと、元の順番を無視して全件をランダムに並べ替えます
    shuffled_quotes = random.sample(source_list, len(source_list))
    
    # 3. 混ぜた後の「一番上」にある言葉を取り出す
    selected_quote = shuffled_quotes[0]
    
    # --- あとの表示部分はそのまま ---
