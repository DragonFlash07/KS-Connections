import streamlit as st
from urllib.parse import quote
import re
import plotly.graph_objects as go

st.set_page_config(page_title="K&K Connections | Meaningful Matchmaking", page_icon="💗", layout="wide")
WHATSAPP = "919825117413"  # Verify public business number before launch.
st.markdown("""<style>
.stApp{background:#fff9f6;color:#39232b}
h1,h2,h3{font-family:Georgia,serif;color:#632f43}
[data-testid="stSidebar"]{background:#f6e8e4}
.hero{background:linear-gradient(120deg,#5d2d40,#a45b68);padding:65px 45px;border-radius:22px;color:#fff}
.hero h1{color:#fff;font-size:clamp(36px,5vw,68px);line-height:1.1}
.hero p{font-size:19px;max-width:700px}
.eyebrow{letter-spacing:3px;font-size:12px;text-transform:uppercase;color:#e7bd9e}
.panel{background:#f7eae5;border-radius:16px;padding:24px;margin:14px 0}
.founder-card{background:linear-gradient(130deg,#fff3ef,#f5e2df);border:1px solid #ead4d0;border-radius:22px;padding:34px 38px;margin:24px 0 30px;box-shadow:0 8px 24px rgba(91,43,60,.045)}
.founder-kicker{font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#a46c66;font-weight:700}
.founder-card h2{font-family:Georgia,serif;font-size:clamp(29px,3vw,44px);margin:10px 0 8px;color:#632f43}
.founder-card p{font-size:17px;line-height:1.8;color:#563b43;max-width:900px}
.founder-quote{font-family:Georgia,serif;font-style:italic;font-size:21px!important;color:#8b455b!important;border-left:3px solid #cba27d;padding-left:18px;margin-top:22px}
.founder-names{font-size:14px;letter-spacing:1.3px;font-weight:700;color:#8b455b;margin-top:14px}
 .kk-logo{text-align:center;padding:10px 0 18px}.kk-logo-name{font-family:Georgia,serif;font-size:24px;font-weight:600;color:#632f43;margin-top:-5px} </style>""", unsafe_allow_html=True)
LOGO = """<div class="kk-logo" aria-label="K&K Connections logo"><svg width="86" height="76" viewBox="0 0 86 76" role="img" aria-label="KK monogram"><path d="M15 9 H70" stroke="#c99c6a" stroke-width="1"/><path d="M38 6 Q43 -1 48 6 Q43 13 38 6" fill="none" stroke="#b7886b" stroke-width="1.4"/><text x="43" y="57" text-anchor="middle" font-family="Georgia,serif" font-size="34" fill="#673145" letter-spacing="-3">K&amp;K</text><path d="M20 66 H66" stroke="#c99c6a" stroke-width="1"/></svg><div class="kk-logo-name">K&K Connections</div></div>"""
with st.sidebar:
    st.markdown(LOGO,unsafe_allow_html=True)
    st.caption("Matchmaking with heart · India & worldwide")
    page=st.radio("Explore",["Home","Global Connections","About & Services","Register Interest","Fees & Contact"])
    st.caption("Personal introductions. Private conversations.")

if page=="Home":
    st.markdown('<div class="hero"><div class="eyebrow">Personal matrimonial introductions</div><h1>Where meaningful<br>connections begin.</h1><p>Thoughtful matchmaking for individuals and families in India and across the world — guided by care, respect and personal attention.</p></div>',unsafe_allow_html=True)
    st.write("")
    a,b=st.columns(2)
    with a: st.info("💗 Personalised introductions and family-focused guidance")
    with b: st.info("🌏 Connecting Indian families across borders")
    st.markdown('<section class="founder-card"><div class="founder-kicker">Our story · The people behind K&amp;K</div><h2>Meet Kamini &amp; Komal</h2><div class="founder-names">TWO WOMEN. ONE SHARED JOURNEY.</div><p>Our story began more than two and a half decades ago, brought together by a shared passion for clothing, creativity and the joy of connecting with people. What started as a journey in fashion has grown into something close to our hearts: helping people find meaningful companionship.</p><p>With K&amp;K Connections, we are taking that journey a little further. For us, matchmaking is not simply about finding someone who looks right on paper. It is about discovering a person who understands your world, shares your values and, most importantly, matches your vibe.</p><p>Rooted in Ahmedabad and open to conversations with families across India and beyond, we bring a personal, thoughtful and respectful approach to every introduction.</p><p class="founder-quote">Because the best connections are not just made — they are felt.</p></section>',unsafe_allow_html=True)
    st.subheader("A personal journey, not a profile directory")
    st.write("Tell us about your hopes, speak with our team, and explore suitable introductions privately. We believe meaningful connections begin with understanding.")
    st.link_button("Speak to K&K Connections on WhatsApp",f"https://wa.me/{WHATSAPP}")
elif page=="Global Connections":
    st.title("Connections Across Borders")
    st.write("From Ahmedabad to Indian communities worldwide. Routes are illustrative and do not represent actual client records.")
    cities={"Ahmedabad":(23.02,72.57),"Sydney":(-33.87,151.21),"London":(51.51,-0.13),"Toronto":(43.65,-79.38),"New York":(40.71,-74.01),"Dubai":(25.20,55.27),"Singapore":(1.35,103.82),"Auckland":(-36.85,174.76)}
    fig=go.Figure()
    for city,(lat,lon) in list(cities.items())[1:]:
        fig.add_trace(go.Scattergeo(lat=[23.02,lat],lon=[72.57,lon],mode="lines",line=dict(width=1.7,color="#d6a369"),opacity=.8,hoverinfo="skip",showlegend=False))
    fig.add_trace(go.Scattergeo(lat=[v[0] for v in cities.values()],lon=[v[1] for v in cities.values()],text=list(cities),mode="markers+text",textposition="top center",marker=dict(size=7,color="#8d4355"),hoverinfo="text",showlegend=False))
    fig.update_geos(showland=True,landcolor="#eaded6",showocean=True,oceancolor="#fff9f6",showcoastlines=False,showframe=False,projection_type="natural earth",bgcolor="#fff9f6")
    fig.update_layout(height=490,margin=dict(l=0,r=0,t=10,b=0),paper_bgcolor="#fff9f6")
    st.plotly_chart(fig,use_container_width=True,config={"staticPlot":True,"displayModeBar":False,"responsive":True})
    st.caption("Illustrative world connections · Static display")
    st.caption("Global connections are an aspiration and service focus, not a claim of established international matches.")
elif page=="About & Services":
    st.title("Matchmaking with heart")
    st.write("K&K Connections is a personalised matrimonial consultancy based in Ahmedabad, Gujarat, serving Indian families locally and internationally.")
    for title,desc in [("01 · Reach out","Contact us to discuss your matrimonial enquiry."),("02 · Personal consultation","We learn about your expectations and preferences."),("03 · Thoughtful introductions","Potential introductions are discussed privately and respectfully."),("04 · Family guidance","We support conversations at a pace comfortable for everyone.")]:
        st.markdown(f'<div class="panel"><h3>{title}</h3><p>{desc}</p></div>',unsafe_allow_html=True)
    st.markdown('<section class="founder-card"><div class="founder-kicker">The founders</div><h2>Kamini &amp; Komal</h2><p>After more than 25 years on a shared journey that began with a love of clothing and creativity, Kamini and Komal founded K&amp;K Connections to bring the same personal touch to matrimonial introductions. They believe a lasting partnership goes beyond a checklist — it begins with shared values, mutual understanding and a genuine connection.</p><p class="founder-quote">Finding someone who matches your vibe.</p></section>',unsafe_allow_html=True)
    st.info("We do not guarantee a match, engagement, or marriage.")
elif page=="Register Interest":
    st.title("Begin your journey")
    st.write("Prepare a WhatsApp enquiry. No login or public profile is needed.")
    st.info("This form does not save a submission to a database. You choose whether to send your prepared message through WhatsApp.")
    with st.form("interest"):
        name=st.text_input("Your name *",max_chars=100)
        who=st.radio("Enquiring for",["Myself","A family member"],horizontal=True)
        country=st.selectbox("Country of residence",["India","Australia","United Kingdom","Canada","United States","UAE","Singapore","New Zealand","Other"])
        phone=st.text_input("Phone / WhatsApp *",max_chars=20)
        service=st.selectbox("How can we help?",["Personal matchmaking","Initial consultation","Services and fees"])
        consent=st.checkbox("I confirm I am 18 or older and consent to sharing these details with K&K Connections for this enquiry.")
        submitted=st.form_submit_button("Prepare WhatsApp enquiry",type="primary")
    if submitted:
        if not name.strip() or not re.fullmatch(r"\+?[0-9 ()-]{8,20}",phone.strip()) or not consent:
            st.error("Enter your name, a valid phone number, and confirm consent.")
        else:
            msg=f"Hello K&K Connections, I would like to enquire.\nName: {name.strip()}\nFor: {who}\nCountry: {country}\nPhone: {phone.strip()}\nService: {service}"
            st.success("Your enquiry is prepared. Review it before sending.")
            st.link_button("Open WhatsApp to send",f"https://wa.me/{WHATSAPP}?text={quote(msg)}",type="primary")
            st.caption("WhatsApp handles information under its own privacy terms. No data is sent until you choose to send it.")
else:
    st.title("Fees & Contact")
    st.write("Fees and service options are discussed during your consultation. Please request current pricing and terms before making any payment.")
    st.warning("Do not send payments to unverified numbers or QR codes. Official UPI details will be provided directly after consultation.")
    st.markdown("**K&K Connections — Ahmedabad, Gujarat, India**")
    st.markdown("**Contact:** +91 98251 17413 ")
    st.link_button("Contact on WhatsApp",f"https://wa.me/{WHATSAPP}")
    st.subheader("Privacy")
    st.write("We request only basic contact information for initial enquiries. No public profiles or account creation. Please avoid sharing ID documents, photographs or sensitive personal information in the initial enquiry. You may contact us to ask about how your information is handled.")
st.divider()
st.caption("© K&K Connections · Personal matchmaking · Ahmedabad, India")
