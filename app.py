import streamlit as st
import pandas as pd
import pickle
import numpy as np
import plotly.graph_objects as go 

# ------------------------------------------------------------------------------
# 1. AYARLAR
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Auto // Arbitrage",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown('<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Rajdhani:wght@300;500;700&display=swap" rel="stylesheet">', unsafe_allow_html=True)

st.markdown("""
    <style>
    @keyframes gradient { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
    .stApp { background: linear-gradient(-45deg, #050505, #0f172a, #1e1b4b, #000000); background-size: 400% 400%; animation: gradient 15s ease infinite; color: white; }
    
    h1, h2, h3 { font-family: 'Orbitron', sans-serif !important; letter-spacing: 2px; text-shadow: 0 0 20px rgba(0, 243, 255, 0.3); text-transform: uppercase; }
    p, label, div { font-family: 'Rajdhani', sans-serif; }
    
    /* --- CSS DÜZELTMESİ: YAZILARI OKUNUR YAPMA --- */
    
    /* 1. Selectbox ve NumberInput Kutularının Arka Planı ve Çerçevesi */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="input"] > div {
        background-color: rgba(0, 0, 0, 0.8) !important; /* Daha koyu siyah */
        border: 2px solid rgba(0, 243, 255, 0.4) !important;
        border-radius: 12px !important;
        min-height: 75px !important;
    }

    /* 2. Kutuların İçindeki SEÇİLMİŞ YAZI RENGİ */
    /* Selectbox içindeki seçili öğe */
    .stSelectbox div[data-baseweb="select"] div {
        color: #ffffff !important; /* BEYAZ YAZI */
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.5rem !important;
    }
    
    /* NumberInput içindeki sayılar */
    .stNumberInput input {
        color: #ffffff !important; /* BEYAZ YAZI */
        font-family: 'Rajdhani', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1.5rem !important;
        -webkit-text-fill-color: #ffffff !important;
        caret-color: #00f3ff;
    }

    /* Dropdown Menüsü Açıldığındaki Seçenekler */
    ul[data-baseweb="menu"] li {
        background-color: #111 !important;
        color: white !important;
        font-size: 1.2rem;
    }

    /* Etiketler (MARKA, MODEL vs.) */
    .stSelectbox label, .stNumberInput label, .stSlider label {
        font-size: 1.1rem !important;
        color: #94a3b8 !important;
        font-weight: 600 !important;
        margin-bottom: 10px !important;
        letter-spacing: 2px !important;
        text-shadow: none !important;
    }

    /* SLIDER TASARIMI */
    .stSlider > div > div > div > div {
        height: 16px !important;
        border-radius: 8px !important;
        background: linear-gradient(90deg, #ff0055 0%, #00f3ff 100%) !important;
    }
    .stSlider div[role="slider"] {
        height: 28px !important;
        width: 28px !important;
        background-color: white !important;
        box-shadow: 0 0 15px #00f3ff !important;
    }

    /* BUTON TASARIMI */
    div.stButton > button {
        background: rgba(0, 243, 255, 0.15);
        color: #00f3ff;
        border: 2px solid #00f3ff;
        height: 80px !important;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.8rem !important;
        font-weight: 900;
        letter-spacing: 5px;
        border-radius: 12px;
        margin-top: 15px;
    }
    div.stButton > button:hover {
        background: #00f3ff;
        color: black;
        box-shadow: 0 0 50px rgba(0, 243, 255, 0.9);
        transform: scale(1.01);
    }
    
    /* HUD Kartları */
    .hud-card { background: rgba(10, 10, 10, 0.9); border-left: 6px solid #00f3ff; padding: 30px; border-radius: 15px; border: 1px solid rgba(255,255,255,0.1); }
    .hud-value { font-family: 'Rajdhani'; font-size: 4rem; font-weight: 700; color: white; line-height: 1; }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 40px; }
    .stTabs [data-baseweb="tab"] { font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 2. VERİ YÜKLEME
# ------------------------------------------------------------------------------
@st.cache_resource
def get_model(): return pickle.load(open('araba_fiyat_modeli.pkl', 'rb'))

@st.cache_data
def get_data(): 
    df_processed = pd.read_pickle('processed_data.pkl')
    df_clean = pd.read_csv('clean_data.csv')
    
    # --- BÜYÜK HARF DÖNÜŞÜMÜ (Uppercase) ---
    df_clean['brand'] = df_clean['brand'].astype(str).str.upper()
    df_clean['model'] = df_clean['model'].astype(str).str.upper()
    
    return df_processed, df_clean

try:
    model = get_model()
    df, df_clean = get_data() 
    expected_columns = df.drop(columns=['price', 'price_log']).columns.tolist()
except:
    st.error("⚠️ SİSTEM HATASI: Veri dosyaları eksik.")
    st.stop()

# ------------------------------------------------------------------------------
# 3. HEADER
# ------------------------------------------------------------------------------
c1, c2 = st.columns([1, 10])
with c1: st.markdown("<div style='font-size: 70px; text-align:center; text-shadow: 0 0 30px #00f3ff;'>⚡</div>", unsafe_allow_html=True)
with c2:
    st.markdown("<h1><span style='color: white;'>AUTO</span> <span style='color: #00f3ff;'>//</span> <span style='color: white;'>ARBITRAGE</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; margin-top: -20px; letter-spacing: 4px; font-size: 1rem;'>AI POWERED PRICING ARCHITECTURE v3.1</p>", unsafe_allow_html=True)

st.markdown("<hr style='border-color: #333;'>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 4. KONTROL PANELİ (DÜZELTİLDİ: BOŞ KUTU KALDIRILDI)
# ------------------------------------------------------------------------------
# Not: Buradaki <div style...> satırı silindi. Artık kutular doğrudan ekrana basılıyor.

# SATIR 1
r1_c1, r1_c2, r1_c3 = st.columns(3)
with r1_c1:
    unique_brands = sorted(df_clean['brand'].unique().tolist())
    selected_brand = st.selectbox("MARKA", unique_brands)
with r1_c2:
    filtered_models = sorted(df_clean[df_clean['brand'] == selected_brand]['model'].unique().tolist())
    selected_model = st.selectbox("MODEL", filtered_models)
with r1_c3:
    year = st.number_input("MODEL YILI", 1990, 2025, 2021)

st.markdown("<div style='height: 30px'></div>", unsafe_allow_html=True)

# SATIR 2
r2_c1, r2_c2, r2_c3 = st.columns(3)
with r2_c1:
    km = st.number_input("KİLOMETRE", 0, 1000000, 45000, step=5000)
with r2_c2:
    cols_fuel = [col.replace('fuel_type_', '').capitalize() for col in expected_columns if 'fuel_type_' in col]
    unique_fuel = sorted(list(set(cols_fuel + ["Gasoline", "Diesel", "Lpg", "Hybrid", "Electric"])))
    selected_fuel = st.selectbox("YAKIT", unique_fuel)
with r2_c3:
    cols_trans = [col.replace('transmission_', '').capitalize() for col in expected_columns if 'transmission_' in col]
    unique_trans = sorted(list(set(cols_trans + ["Manual", "Automatic", "Tiptronic", "Semi-automatic"])))
    selected_trans = st.selectbox("VİTES", unique_trans)

st.markdown("<div style='height: 30px'></div>", unsafe_allow_html=True)

# SATIR 3
r3_c1, r3_c2 = st.columns([2, 1])

with r3_c1:
    st.markdown("<label style='font-size: 1.1rem; color: #94a3b8; letter-spacing:1px;'>MOTOR HACMİ (L)</label>", unsafe_allow_html=True)
    engine_volume = st.slider("", 0.8, 6.0, 1.6, 0.1) 

with r3_c2:
    predict_btn = st.button("HESAPLA")

# Buradaki kapanış div'i de silindi

# ------------------------------------------------------------------------------
# 5. HESAPLAMA MOTORU
# ------------------------------------------------------------------------------
if predict_btn:
    input_data = pd.DataFrame(columns=expected_columns)
    input_data.loc[0] = 0 
    
    input_data['year'] = year
    input_data['km'] = km
    input_data['engine_volume'] = engine_volume
    
    # .lower() kullanarak modeli bozmadan eşleştirme yapıyoruz
    brand_key = f"brand_{selected_brand.lower()}"
    if brand_key in input_data.columns: input_data[brand_key] = 1

    fuel_key = f"fuel_type_{selected_fuel}"
    fuel_key_lower = f"fuel_type_{selected_fuel.lower()}"
    if fuel_key in input_data.columns: input_data[fuel_key] = 1
    elif fuel_key_lower in input_data.columns: input_data[fuel_key_lower] = 1

    trans_key = f"transmission_{selected_trans}"
    trans_key_lower = f"transmission_{selected_trans.lower()}"
    if trans_key in input_data.columns: input_data[trans_key] = 1
    elif trans_key_lower in input_data.columns: input_data[trans_key_lower] = 1
        
    # Frekans hesabı (Büyük harfli veri seti üzerinden)
    model_count = df_clean[df_clean['model'] == selected_model].shape[0]
    total_count = df_clean.shape[0]
    model_freq = model_count / total_count
    
    if 'model_freq_enc' in input_data.columns: input_data['model_freq_enc'] = model_freq
    other_freq_cols = [c for c in expected_columns if '_freq' in c and c != 'model_freq_enc']
    for col in other_freq_cols: input_data[col] = df[col].mean()

    prediction_log = model.predict(input_data)
    price = np.expm1(prediction_log)[0]
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- HUD ---
    tab_val, tab_tech = st.tabs(["// PİYASA DEĞERİ", "// TEKNİK VERİ"])
    
    with tab_val:
        row1_col1, row1_col2 = st.columns([1, 1.5])
        with row1_col1:
            st.markdown(f"""
            <div class="hud-card">
                <div class="hud-title">TAHMİNİ DEĞER</div>
                <div class="hud-value" style="color: #00f3ff;">₺{price:,.0f}</div>
                <div class="hud-sub">SAPMA PAYI: ±%4</div>
            </div>
            <div style="height: 20px;"></div>
            <div class="hud-card" style="border-left-color: #ff0055;">
                <div class="hud-title">GÜVEN ARALIĞI</div>
                <div class="hud-value" style="font-size: 2.8rem;">₺{price*0.96:,.0f} <span style="font-size:1.5rem; color:#666;">---</span> {price*1.04:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
            
        with row1_col2:
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = price,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "MARKET POSITION", 'font': {'size': 14, 'color': "#666", 'family': "Orbitron"}},
                number = {'font': {'color': "white", 'family': "Rajdhani", 'size': 50}},
                gauge = {
                    'axis': {'range': [price*0.5, price*1.5], 'tickwidth': 1, 'tickcolor': "#333"},
                    'bar': {'color': "#00f3ff", 'thickness': 1},
                    'bgcolor': "rgba(0,0,0,0)",
                    'borderwidth': 0,
                    'steps': [{'range': [price*0.5, price*0.8], 'color': '#111'}, {'range': [price*0.8, price*1.2], 'color': '#222'}, {'range': [price*1.2, price*1.5], 'color': '#111'}],
                    'threshold': {'line': {'color': "#ff0055", 'width': 5}, 'thickness': 1, 'value': price}
                }))
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font={'color': "white"}, margin=dict(t=40, b=20, l=30, r=30), height=400)
            st.plotly_chart(fig, use_container_width=True)

    with tab_tech:
        st.markdown(f"""
        <div style="font-family: 'Rajdhani'; color: #aaa; border: 1px solid #333; padding: 25px; font-size: 1.2rem;">
            > ANALİZ: {pd.Timestamp.now().strftime('%H:%M:%S')}<br>
            > ARAÇ: <span style="color:white">{selected_brand} {selected_model}</span><br>
            > MODEL FREKANSI: {model_freq:.5f}<br>
            > DURUM: <span style="color: #00f3ff;">BAŞARILI</span>
        </div>
        """, unsafe_allow_html=True)
        st.download_button("📥 LOG KAYDINI İNDİR", data=f"Price: {price}", file_name="arbitrage_log.txt")

else:
    st.markdown("<br><br><div style='text-align: center; opacity: 0.7;'><h3 style='color: #94a3b8; letter-spacing: 5px;'>VALUATION ENGINE READY</h3><div style='margin: 0 auto; width: 60px; height: 60px; border: 4px solid #333; border-top: 4px solid #00f3ff; border-radius: 50%; animation: spin 2s linear infinite;'></div><style>@keyframes spin {0% {transform: rotate(0deg);} 100% {transform: rotate(360deg);}}</style></div>", unsafe_allow_html=True)

st.markdown("<div style='position: fixed; bottom: 10px; right: 10px; color: #333; font-size: 10px; font-family: Orbitron;'>POWERED BY AUTO // ARBITRAGE</div>", unsafe_allow_html=True)