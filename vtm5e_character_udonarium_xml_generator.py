import html
import streamlit as st

# ページの設定
st.set_page_config(
    page_title="V:tM 5e Udonarium XML Generator", layout="centered"
)

# --- XMLテンプレート（Udonarium出力用） ---
XML_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<character rotate="0" roll="0" location.name="table" location.x="450" location.y="500" posZ="0">
<data name="character">
<data name="image">
<data type="image" name="imageIdentifier"/>
</data>
<data name="common">
<data name="name">{name}</data>
<data name="size">1</data>
</data>
<data name="detail">
<data name="氏族">{clan}</data>
<data name="捕食の流儀">{predator}</data>
<data name="夜の年代記のタイトル">{chronicle}</data>
<data name="世代">{generation}</data>
<data name="大望">{ambition}</data>
<data name="コンセプト">{concept}</data>
<data name="親御">{sire}</data>
<data name="私欲">{desire}</data>
<data name="資質">
<data name="身体的">
<data name="筋力">{str}</data>
<data name="持久">{sta}</data>
<data name="敏捷">{dex}</data>
</data>
<data name="社会的">
<data name="自制">{com}</data>
<data name="魅力">{cha}</data>
<data name="誘導">{man}</data>
</data>
<data name="精神的">
<data name="機知">{wit}</data>
<data name="集中">{res}</data>
<data name="知性">{int}</data>
</data>
</data>
<data name="体力" type="numberResource" currentValue="0">{health}</data>
<data name="意志力">{willpower}</data>
<data name="技能">
<data name="運転">{drv}</data>
<data name="運動">{ath}</data>
<data name="隠密">{ste}</data>
<data name="格闘">{bra}</data>
<data name="近接武器">{mel}</data>
<data name="銃器">{fir}</data>
<data name="制作">{cra}</data>
<data name="生存術">{sur}</data>
<data name="窃盗">{lar}</data>
<data name="裏社会">{strw}</data>
<data name="脅迫">{intm}</data>
<data name="虚言">{sub}</data>
<data name="芸事">{per}</data>
<data name="指揮">{lea}</data>
<data name="推察">{ins}</data>
<data name="説得">{pers}</data>
<data name="動物理解">{ani}</data>
<data name="礼儀作法">{eti}</data>
<data name="医学">{med}</data>
<data name="隠秘学">{occ}</data>
<data name="科学">{sci}</data>
<data name="教養">{aca}</data>
<data name="財務">{fin}</data>
<data name="政治">{pol}</data>
<data name="先端技術">{tec}</data>
<data name="探偵">{inv}</data>
<data name="知覚">{awa}</data>
</data>
<data name="訓え">
<data name="1">{dis1}</data>
<data name="2">{dis2}</data>
<data name="3">{dis3}</data>
<data name="4">{dis4}</data>
<data name="5">{dis5}</data>
<data name="6">{dis6}</data>
</data>
<data name="汚点">{stain}</data>
<data name="気質">{temp}</data>
<data name="飢え">{hunger}</data>
<data name="人間性">{humanity}</data>
<data name="夜の年代記の良心">{conscience}</data>
<data name="試金石と徳心">{touchstone}</data>
<data name="氏族の悪癖">{bane}</data>
<data name="特長と欠点">
<data name="1">{adv1}</data>
<data name="2">{adv2}</data>
<data name="3">{adv3}</data>
<data name="4">{adv4}</data>
<data name="5">{adv5}</data>
<data name="6">{adv6}</data>
<data name="7">{adv7}</data>
<data name="8">{adv8}</data>
<data name="9">{adv9}</data>
<data name="10">{adv10}</data>
<data name="11">{adv11}</data>
</data>
<data name="メモ" type="note">{memo}</data>
<data name="血格">{blood_potency}</data>
<data name="血による増強の追加ダイス">{blood_surge}</data>
<data name="訓えへの追加ダイス">{mend_amount}</data>
<data name="食餌への制限">{power_bonus}</data>
<data name="飢餓チェック1回ごとの回復量">{rouse_reroll}</data>
<data name="飢餓チェックを振り直せる訓えのレベル">{feeding_penalty}</data>
<data name="悪癖の深刻さ">{bane_severity}</data>
<data name="総経験点">{xp_total}</data>
<data name="使用した経験点">{xp_spent}</data>
<data name="真の年齢">{true_age}</data>
<data name="外見年齢">{app_age}</data>
<data name="誕生日">{dob}</data>
<data name="命日">{dod}</data>
<data name="見た目" type="note">{appearance}</data>
<data name="目立つ特長" type="note">{dist_features}</data>
<data name="これまでの出来事" type="note">{history}</data>
</data>
</data>
<chat-palette dicebot="VampireTheMasquerade5th">{chat_palette}</chat-palette>
</character>
"""

# デフォルトのチャットパレット
DEFAULT_CHAT_PALETTE = """1d10>=6 飢渇判定
VMI({筋力}+{筋力})H{飢え} 筋力判定
VMI({敏捷}+{敏捷})H{飢え} 敏捷判定
VMI({持久}+{持久})H{飢え} 持久判定
VMI({魅力}+{魅力})H{飢え} 魅力判定
VMI({誘導}+{誘導})H{飢え} 誘導判定
VMI({自制}+{自制})H{飢え} 自制判定
VMI({知性}+{知性})H{飢え} 知性判定
VMI({機知}+{機知})H{飢え} 機知判定
VMI({集中}+{集中})H{飢え} 集中判定
VMI({集中}+{自制})H{飢え} 抵抗判定
VMI({敏捷}+{運動})H{飢え} 運動/回避/投擲/登攀/受け身
VMI({筋力}+{格闘})H{飢え} 格闘攻撃
VMI({敏捷}+{近接武器})H{飢え} 近接武器攻撃(片手)
VMI({筋力}+{近接武器})H{飢え} 近接武器攻撃(両手)
VMI({自制}+{銃器})H{飢え} 銃器攻撃
VMI({知性}+{先端技術})H{飢え} 先端技術(ハッキング/爆発物作成/etc)
VMI({知性}+{裏社会})H{飢え} 裏社会
VMI({知性}+{生存術})H{飢え} 生存術
VMI({知性}+{知覚})H{飢え} 知覚(何かを認識する)
VMI({知性}+{探偵})H{飢え} 探偵
VMI({知性}+{医学})H{飢え} 医学(診察)
VMI({知性}+{科学})H{飢え} 科学(理系)
VMI({知性}+{教養})H{飢え} 教養(文系)
VMI({知性}+{窃盗})H{飢え} 窃盗(知性)
VMI({知性}+{政治})H{飢え} 政治(知性)
VMI({機知}+{知覚})H{飢え} 知覚(何かに気づく(機知)/目線を逸らす/etc)
VMI({機知}+{生存術})H{飢え} 生存術(追跡/etc)
VMI({機知}+{運転})H{飢え} 運転(運転(機知)/etc)
VMI({機知}+{自制})H{飢え} (黙秘/etc)
VMI({集中}+{知覚})H{飢え} 知覚(何かから選ぶ)
VMI({集中}+{裏社会})H{飢え} 裏社会(尾行)
VMI({集中}+{脅迫})H{飢え} 脅迫(or 目線を捉える)
VMI({筋力}+{運動})H{飢え} 運動(重量挙げ)
VMI({筋力}+{窃盗})H{飢え} 窃盗(筋力)
VMI({筋力}+{脅迫})H{飢え} 脅迫(筋力)
VMI({敏捷}+{運転})H{飢え} 運転(敏捷)
VMI({敏捷}+{窃盗})H{飢え} 窃盗(敏捷)
VMI({敏捷}+{隠密})H{飢え} 隠密
VMI({魅力}+{芸事})H{飢え} 芸事(演説/ライブパフォーマンス/etc)
VMI({魅力}+{推察})H{飢え} 推察
VMI({魅力}+{虚言})H{飢え} 虚言(言いくるめ)
VMI({魅力}+{説得})H{飢え} 説得(魅力)
VMI({魅力}+{礼儀作法})H{飢え} 礼儀作法(魅力)
VMI({誘導}+{虚言})H{飢え} 虚言(嘘をつく/etc)
VMI({誘導}+{推察})H{飢え} 推察(尋問)
VMI({誘導}+{脅迫})H{飢え} 脅迫(誘導)
VMI({誘導}+{説得})H{飢え} 説得(誘導)
VMI({誘導}+{礼儀作法})H{飢え} 礼儀作法(誘導)
VMI({自制}+{推察})H{飢え} 推察(嘘を見破る)
VMI({意志力}) 意志力判定
VMI(10-({人間性}+{汚点})) 悔恨判定
VMI({人間性}) 人間性判定
VMI({筋力}+{集中})H{飢え} (同族喰らい判定)
VMI({人間性}+{血格})H{飢え} (同族喰らい(対抗))"""

st.title("Udonarium キャラクターシート入力 (V:tM 5e)")

# --- 基本情報 ---
st.header("基本情報")
col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input("名前", value="vampire's name")
    chronicle = st.text_input("夜の年代記のタイトル", value="神戸の夜")
    concept = st.text_input("コンセプト", value="ショタじじい")
with col2:
    clan = st.text_input("氏族", value="トレメール")
    generation = st.text_input("世代", value="13世代")
    sire = st.text_input("親御", value="キスショット")
with col3:
    predator = st.text_input("捕食の流儀", value="砂袋")
    ambition = st.text_input("大望", value="復讐の成就")
    desire = st.text_input("私欲", value="血糖たっぷりの血")

# --- 資質 (Attributes) ---
st.header("資質 (Attributes)")
col1, col2, col3 = st.columns(3)
with col1:
    str_val = st.number_input("筋力 (身体的)", value=5)
    com = st.number_input("自制 (社会的)", value=2)
    wit = st.number_input("機知 (精神的)", value=3)
with col2:
    sta = st.number_input("持久 (身体的)", value=4)
    cha = st.number_input("魅力 (社会的)", value=2)
    res = st.number_input("集中 (精神的)", value=3)
with col3:
    dex = st.number_input("敏捷 (身体的)", value=3)
    man = st.number_input("誘導 (社会的)", value=2)
    int_val = st.number_input("知性 (精神的)", value=3)

# --- リソース ---
st.header("リソース")
col1, col2, col3 = st.columns(3)
with col1:
    health = st.number_input("体力", value=10)
    humanity = st.number_input("人間性", value=5)
with col2:
    willpower = st.number_input("意志力", value=5)
    stain = st.number_input("汚点", value=2)
with col3:
    hunger = st.number_input("飢え", value=5)
    temp = st.text_input("気質", value="おこりっぽい")

# --- 技能 (Skills) ---
st.header("技能 (Skills)")
col1, col2, col3 = st.columns(3)
with col1:
    drv = st.number_input("運転", value=1)
    ath = st.number_input("運動", value=2)
    ste = st.number_input("隠密", value=2)
    bra = st.number_input("格闘", value=2)
    mel = st.number_input("近接武器", value=2)
    fir = st.number_input("銃器", value=2)
    cra = st.number_input("制作", value=2)
    sur = st.number_input("生存術", value=2)
    lar = st.number_input("窃盗", value=2)
with col2:
    strw = st.number_input("裏社会", value=2)
    intm = st.number_input("脅迫", value=2)
    sub = st.number_input("虚言", value=2)
    per = st.number_input("芸事", value=2)
    lea = st.number_input("指揮", value=2)
    ins = st.number_input("推察", value=2)
    pers = st.number_input("説得", value=2)
    ani = st.number_input("動物理解", value=2)
    eti = st.number_input("礼儀作法", value=2)
with col3:
    med = st.number_input("医学", value=2)
    occ = st.number_input("隠秘学", value=2)
    sci = st.number_input("科学", value=2)
    aca = st.number_input("教養", value=2)
    fin = st.number_input("財務", value=2)
    pol = st.number_input("政治", value=2)
    tec = st.number_input("先端技術", value=2)
    inv = st.number_input("探偵", value=2)
    awa = st.number_input("知覚", value=2)

# --- 血格・吸血鬼の特徴 ---
st.header("血格・吸血鬼の特徴")
col1, col2 = st.columns(2)
with col1:
    blood_potency = st.number_input("血格", value=5)
    mend_amount = st.number_input("訓えへの追加ダイス", value=2)
    rouse_reroll = st.number_input("飢餓チェック1回ごとの回復量", value=2)
    bane = st.text_input("氏族の悪癖", value="あくじき")
    conscience = st.text_input("夜の年代記の良心", value="ともだち")
with col2:
    blood_surge = st.number_input("血による増強の追加ダイス", value=1)
    power_bonus = st.text_input("食餌への制限", value="3")
    feeding_penalty = st.number_input(
        "飢餓チェックを振り直せる訓えのレベル", value=1
    )
    bane_severity = st.text_input("悪癖の深刻さ", value="ひひひ")  # 元コードのバリュー
    touchstone = st.text_input("試金石と徳心", value="りんり")

# --- 訓え (Disciplines) ---
st.header("訓え (Disciplines)")
col1, col2, col3 = st.columns(3)
with col1:
    dis1 = st.text_input("訓え 1", value="ほのお")
    dis4 = st.text_input("訓え 4", value="へんしん")
with col2:
    dis2 = st.text_input("訓え 2", value="れいき")
    dis5 = st.text_input("訓え 5", value="まほう")
with col3:
    dis3 = st.text_input("訓え 3", value="しはい")
    dis6 = st.text_input("訓え 6", value="きり")

# --- 特長と欠点 ---
st.header("特長と欠点")
col1, col2, col3 = st.columns(3)
with col1:
    adv1 = st.text_input("特長・欠点 1", value="つよい")
    adv4 = st.text_input("特長・欠点 4", value="わらい")
    adv7 = st.text_input("特長・欠点 7", value="ふふふ")
    adv10 = st.text_input("特長・欠点 10", value="かっか")
with col2:
    adv2 = st.text_input("特長・欠点 2", value="よわい")
    adv5 = st.text_input("特長・欠点 5", value="ははは")
    adv8 = st.text_input("特長・欠点 8", value="へへへへ")
    adv11 = st.text_input("特長・欠点 11", value="きいい")
with col3:
    adv3 = st.text_input("特長・欠点 3", value="かなしい")
    adv6 = st.text_input("特長・欠点 6", value="ひひひ")
    adv9 = st.text_input("特長・欠点 9", value="ほおおお")

# --- 経験点・経歴 ---
st.header("経験点・経歴")
col1, col2 = st.columns(2)
with col1:
    xp_total = st.number_input("総経験点", value=0)
    true_age = st.number_input("真の年齢", value=555)
    dob = st.text_input("誕生日", value="06/01")
with col2:
    xp_spent = st.number_input("使用した経験点", value=0)
    app_age = st.number_input("外見年齢", value=5)
    dod = st.text_input("命日", value="06/30")

# --- 詳細設定 ---
st.header("詳細設定")
appearance = st.text_area("見た目", value="わかい")
dist_features = st.text_area("目立つ特長", value="八重歯")
history = st.text_area("これまでの出来事", value="東北から九州へ")
memo = st.text_area("メモ", value="メモの中身")

# --- チャットパレット ---
st.header("チャットパレット")
chat_palette_raw = st.text_area(
    "マクロ (自由に編集・追加可能)", value=DEFAULT_CHAT_PALETTE, height=400
)

# --- XML生成処理 ---
chat_palette_escaped = html.escape(chat_palette_raw)

xml_content = XML_TEMPLATE.format(
    name=name,
    clan=clan,
    predator=predator,
    chronicle=chronicle,
    generation=generation,
    ambition=ambition,
    concept=concept,
    sire=sire,
    desire=desire,
    str=str_val,
    sta=sta,
    dex=dex,
    com=com,
    cha=cha,
    man=man,
    wit=wit,
    res=res,
    int=int_val,
    health=health,
    willpower=willpower,
    drv=drv,
    ath=ath,
    ste=ste,
    bra=bra,
    mel=mel,
    fir=fir,
    cra=cra,
    sur=sur,
    lar=lar,
    strw=strw,
    intm=intm,
    sub=sub,
    per=per,
    lea=lea,
    ins=ins,
    pers=pers,
    ani=ani,
    eti=eti,
    med=med,
    occ=occ,
    sci=sci,
    aca=aca,
    fin=fin,
    pol=pol,
    tec=tec,
    inv=inv,
    awa=awa,
    dis1=dis1,
    dis2=dis2,
    dis3=dis3,
    dis4=dis4,
    dis5=dis5,
    dis6=dis6,
    temp=temp,
    hunger=hunger,
    humanity=humanity,
    stain=stain,
    conscience=conscience,
    touchstone=touchstone,
    bane=bane,
    adv1=adv1,
    adv2=adv2,
    adv3=adv3,
    adv4=adv4,
    adv5=adv5,
    adv6=adv6,
    adv7=adv7,
    adv8=adv8,
    adv9=adv9,
    adv10=adv10,
    adv11=adv11,
    memo=memo,
    blood_potency=blood_potency,
    blood_surge=blood_surge,
    mend_amount=mend_amount,
    power_bonus=power_bonus,
    rouse_reroll=rouse_reroll,
    feeding_penalty=feeding_penalty,
    bane_severity=bane_severity,
    xp_total=xp_total,
    xp_spent=xp_spent,
    true_age=true_age,
    app_age=app_age,
    dob=dob,
    dod=dod,
    appearance=appearance,
    dist_features=dist_features,
    history=history,
    chat_palette=chat_palette_escaped,
)

filename = name.strip() if name.strip() else "character"

# ダウンロードボタン
st.download_button(
    label="XMLファイルをダウンロード",
    data=xml_content,
    file_name=f"{filename}.xml",
    mime="application/xml",
    use_container_width=True,
)
