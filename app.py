import streamlit as st
from urllib.parse import quote
import re
import plotly.graph_objects as go

st.set_page_config(page_title="KS Connections | Meaningful Matchmaking", page_icon="💗", layout="wide")
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
</style>""", unsafe_allow_html=True)
with st.sidebar:
    st.title("KS Connections")
    st.caption("Matchmaking with heart · India & worldwide")
    page=st.radio("Explore",["Home","Global Connections","About & Services","Register Interest","Fees & Contact"])
    st.caption("Personal introductions. Private conversations.")

if page=="Home":
    st.markdown('<div class="hero"><div class="eyebrow">Personal matrimonial introductions</div><h1>Where meaningful<br>connections begin.</h1><p>Thoughtful matchmaking for individuals and families in India and across the world — guided by care, respect and personal attention.</p></div>',unsafe_allow_html=True)
    st.write("")
    a,b=st.columns(2)
    with a: st.info("💗 Personalised introductions and family-focused guidance")
    with b: st.info("🌏 Connecting Indian families across borders")
    st.subheader("A personal journey, not a profile directory")
    st.write("Tell us about your hopes, speak with our team, and explore suitable introductions privately. We believe meaningful connections begin with understanding.")
    st.link_button("Speak to KS Connections on WhatsApp",f"https://wa.me/{WHATSAPP}")
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
    st.plotly_chart(fig,use_container_width=True)
    st.caption("Global connections are an aspiration and service focus, not a claim of established international matches.")
elif page=="About & Services":
    st.title("Matchmaking with heart")
    st.write("KS Connections is a personalised matrimonial consultancy based in Ahmedabad, Gujarat, serving Indian families locally and internationally.")
    for title,desc in [("01 · Reach out","Contact us to discuss your matrimonial enquiry."),("02 · Personal consultation","We learn about your expectations and preferences."),("03 · Thoughtful introductions","Potential introductions are discussed privately and respectfully."),("04 · Family guidance","We support conversations at a pace comfortable for everyone.")]:
        st.markdown(f'<div class="panel"><h3>{title}</h3><p>{desc}</p></div>',unsafe_allow_html=True)
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
        consent=st.checkbox("I confirm I am 18 or older and consent to sharing these details with KS Connections for this enquiry.")
        submitted=st.form_submit_button("Prepare WhatsApp enquiry",type="primary")
    if submitted:
        if not name.strip() or not re.fullmatch(r"\+?[0-9 ()-]{8,20}",phone.strip()) or not consent:
            st.error("Enter your name, a valid phone number, and confirm consent.")
        else:
            msg=f"Hello KS Connections, I would like to enquire.\nName: {name.strip()}\nFor: {who}\nCountry: {country}\nPhone: {phone.strip()}\nService: {service}"
            st.success("Your enquiry is prepared. Review it before sending.")
            st.link_button("Open WhatsApp to send",f"https://wa.me/{WHATSAPP}?text={quote(msg)}",type="primary")
            st.caption("WhatsApp handles information under its own privacy terms. No data is sent until you choose to send it.")
else:
    st.title("Fees & Contact")
    st.write("Fees and service options are discussed during your consultation. Please request current pricing and terms before making any payment.")
    st.warning("Do not send payments to unverified numbers or QR codes. Official UPI details will be provided directly after consultation.")
    st.markdown("**KS Connections — Ahmedabad, Gujarat, India**")
    st.markdown("**Contact:** +91 98251 17413 (verify before public launch)")
    st.link_button("Contact on WhatsApp",f"https://wa.me/{WHATSAPP}")
    st.subheader("Privacy")
    st.write("We request only basic contact information for initial enquiries. No public profiles or account creation. Please avoid sharing ID documents, photographs or sensitive personal information in the initial enquiry. You may contact us to ask about how your information is handled.")
st.divider()
st.caption("© KS Connections · Personal matchmaking · Ahmedabad, India")
