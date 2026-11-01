import re
from urllib.parse import quote
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="K&K Connections | Personal Matrimonial Services in Ahmedabad",page_icon="💗",layout="wide")
WHATSAPP="919825117413"
SECONDARY_WHATSAPP="919173013877"
PAGES=["Home","Our Story","How It Works","Global Connections","Register Interest","Fees & Contact"]
st.markdown("""<style>
.stApp{background:#fffaf7;color:#39232b}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#fff4ee,#f8e7e3)}
[data-testid="stSidebar"] .stRadio label{font-size:15px}
h1,h2,h3{font-family:Georgia,serif;color:#6d2c42}
.block-container{padding-top:2rem;max-width:1200px}
.hero{background:linear-gradient(108deg,rgba(95,26,47,.98),rgba(133,55,72,.93));border-radius:22px;padding:55px 48px;color:#fff;position:relative;overflow:hidden}
.hero:after{content:"❀";position:absolute;right:1%;bottom:-22%;font-size:310px;opacity:.08;color:#ffe4c9;pointer-events:none}
.hero h1{color:white;font-size:clamp(38px,5vw,66px);line-height:1.1;max-width:850px;margin:16px 0}
.hero p{font-size:19px;max-width:650px;color:#fff0eb;line-height:1.65}
.eyebrow{letter-spacing:2.6px;font-size:12px;text-transform:uppercase;color:#f4cba9;font-weight:700}
.kk-logo{text-align:center;padding:14px 0 12px}
.kk-monogram{font-family:Georgia,serif;font-size:58px;color:#6d2c42;line-height:1}
.kk-sub{font-family:Georgia,serif;font-style:italic;font-size:23px;color:#8b5362}
.kk-small{font-size:10px;letter-spacing:2px;color:#805d64;margin-top:10px}
.section-card{background:linear-gradient(120deg,#fff2ec,#f8e3df);border:1px solid #f1dcd6;border-radius:19px;padding:28px 32px;margin:16px 0}
.section-card p{font-size:16px;line-height:1.8}
.section-card h2{font-size:clamp(28px,3vw,42px);margin:8px 0 14px}
.kicker{font-size:12px;letter-spacing:2.2px;text-transform:uppercase;color:#985c64;font-weight:700}
.quote{font-family:Georgia,serif;font-style:italic;font-size:21px;color:#8a3d54;border-left:3px solid #c49b7d;padding-left:15px;margin-top:18px}
.trust{display:flex;gap:12px;flex-wrap:wrap;margin:16px 0}
.trust span{flex:1;min-width:150px;background:#f9eae6;border-radius:13px;padding:16px;text-align:center;color:#743448}
.steps{display:flex;gap:12px;flex-wrap:wrap;margin:15px 0}
.step{flex:1;min-width:185px;background:#f8ebe6;padding:20px;border-radius:15px}
.step strong{color:#6d2c42;font-size:18px}
.step p{line-height:1.5;font-size:14px}
.step-num{background:#8c455a;color:white;padding:7px 11px;border-radius:50%;margin-right:8px}
.cta{background:#712c43;border-radius:18px;padding:27px 32px;color:white;margin:20px 0}
.cta h2{color:white;margin:0 0 8px}
.cta p{color:#fff0eb}
.footer{color:#967b80;font-size:13px;text-align:center;padding:14px}
@media(max-width:650px){.hero{padding:32px 23px}.section-card{padding:22px}.block-container{padding-top:1rem}}
</style>""",unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="kk-logo"><div style="color:#c49b7d">──── ♡ ────</div><div class="kk-monogram">K&amp;K</div><div class="kk-sub">Connections</div><div class="kk-small">PERSONALISED MATRIMONIAL SERVICES<br>INDIA &amp; WORLDWIDE</div></div>',unsafe_allow_html=True)
    page=st.radio("Explore",PAGES,index=4 if st.session_state.pop("go_register",False) else 0)
    st.markdown('<div style="text-align:center;margin-top:24px;color:#926c72;font-family:Georgia,serif;font-style:italic">Personal introductions.<br>Private conversations.<br>Meaningful connections.</div>',unsafe_allow_html=True)

def contact_button(label="Chat with Kamini on WhatsApp",message="Hello K&K Connections, I would like to know more about your matrimonial services."):
    st.link_button(label,f"https://wa.me/{WHATSAPP}?text={quote(message)}",type="primary")

def map_figure(height=380):
    cities={"Ahmedabad":(23.02,72.57),"Sydney":(-33.87,151.21),"London":(51.51,-0.13),"Toronto":(43.65,-79.38),"New York":(40.71,-74.01),"Dubai":(25.20,55.27),"Singapore":(1.35,103.82),"Auckland":(-36.85,174.76)}
    fig=go.Figure()
    for city,(lat,lon) in list(cities.items())[1:]:
        fig.add_trace(go.Scattergeo(lat=[23.02,lat],lon=[72.57,lon],mode="lines",line=dict(width=1.5,color="#d6a369"),opacity=.8,hoverinfo="skip",showlegend=False))
    fig.add_trace(go.Scattergeo(lat=[v[0] for v in cities.values()],lon=[v[1] for v in cities.values()],text=list(cities),mode="markers+text",textposition="top center",marker=dict(size=7,color="#8d4355"),hoverinfo="skip",showlegend=False))
    fig.update_geos(showland=True,landcolor="#edd9d3",showocean=True,oceancolor="#fff8f5",showcoastlines=False,showframe=False,projection_type="natural earth",bgcolor="#fff8f5")
    fig.update_layout(height=height,margin=dict(l=0,r=0,t=0,b=0),paper_bgcolor="#fff8f5")
    return fig

def show_map(height=380):
    st.plotly_chart(map_figure(height),use_container_width=True,config={"staticPlot":True,"displayModeBar":False,"responsive":True})

def story(full=False):
    st.markdown("""<section class="section-card"><div class="kicker">Our story · The people behind K&amp;K</div><h2>Meet Kamini &amp; Komal</h2><div class="kicker">Two women. One shared journey.</div><p>Our journey began more than two and a half decades ago, brought together by a shared passion for clothing, creativity and the joy of connecting with people.</p><p>What started in fashion has grown into something closer to our hearts — helping individuals and families find meaningful companionship.</p><p>With K&amp;K Connections, we are taking that journey a little further. For us, matchmaking is not simply about finding someone who looks right on paper. It is about discovering a person who understands your world, shares your values and, most importantly, <b>matches your vibe.</b></p><p class="quote">Because the best connections are not just made — they are felt.</p></section>""",unsafe_allow_html=True)
    if full:
        st.write("Based in Ahmedabad, we welcome enquiries from individuals and families in India and abroad. Our approach is personal, respectful and centred on understanding each person's preferences.")

def steps():
    st.markdown("""<div class="steps"><div class="step"><span class="step-num">01</span><strong>Enquire</strong><p>Tell us a little about yourself and your expectations.</p></div><div class="step"><span class="step-num">02</span><strong>Consult</strong><p>Discuss your preferences, service options and next steps privately.</p></div><div class="step"><span class="step-num">03</span><strong>Connect</strong><p>Explore suitable introductions with care, consent and discretion.</p></div></div>""",unsafe_allow_html=True)

if page=="Home":
    st.markdown("""<section class="hero"><div class="eyebrow">Kamini &amp; Komal · Personal matrimonial services</div><h1>Beyond matchmaking.<br>Find your kind of connection.</h1><p>Thoughtful introductions, shared values and a life partner who matches your vibe.</p></section>""",unsafe_allow_html=True)
    left,right=st.columns(2)
    with left:
        if st.button("♡  Register Your Interest",type="primary",use_container_width=True):
            st.session_state["go_register"]=True
            st.rerun()
    with right: contact_button("💬 Chat on WhatsApp")
    st.markdown('<div class="trust"><span>♡ Personalised introductions and family-focused guidance</span><span>◎ Connecting Indian families across borders</span></div>',unsafe_allow_html=True)
    story()
    st.header("Connections Across Borders")
    st.write("From Ahmedabad to Indian communities worldwide.")
    show_map(310)
    st.caption("Routes are illustrative of our service focus, not records of international matches.")
    st.markdown('<div class="cta"><h2>Let’s begin with a conversation.</h2><p>Speak with Kamini or Komal about our services and your preferences.</p></div>',unsafe_allow_html=True)
    contact_button()
elif page=="Our Story":
    st.title("Our Story")
    story(full=True)
    contact_button()
elif page=="How It Works":
    st.title("How K&K Works")
    st.write("Personal guidance rather than a public directory of profiles.")
    steps()
    st.markdown('<div class="section-card"><h2>What to expect</h2><p>We begin by understanding your expectations and explaining our service. Any potential introductions are handled privately. Fees and terms are discussed before you decide whether to proceed.</p></div>',unsafe_allow_html=True)
    st.info("A match, engagement or marriage cannot be guaranteed.")
    contact_button("Ask about the process")
elif page=="Global Connections":
    st.title("Connections Across Borders")
    st.write("From Ahmedabad to Indian communities worldwide.")
    show_map(480)
    st.caption("The routes are illustrative and do not represent actual client records or completed matches.")
elif page=="Register Interest":
    st.title("Begin Your Journey")
    st.write("Prepare a private WhatsApp enquiry. No login or public profile required.")
    st.info("This form does not store submissions in a database. You decide whether to send your prepared message through WhatsApp.")
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
            st.caption("No data is sent until you choose to send your message.")
else:
    st.title("Fees & Contact")
    st.write("K&K uses an initial-fee and success-based-fee model. Please request the current amounts, deliverables, refund terms and conditions directly before paying.")
    st.warning("Do not send payments to unverified numbers or QR codes. Confirm payment details directly with the team.")
    st.markdown("**K&K Connections — Ahmedabad, Gujarat, India**")
    st.write("Kamini Shah: +91 98251 17413")
    st.write("Komal Thakkar: +91 91730 13877")
    contact_button()
    st.subheader("Privacy")
    st.write("We request only basic contact details for an initial enquiry. No public profiles or account creation. Please avoid sharing ID documents, photographs or sensitive information in your initial message. Ask the team how your details are handled before providing further information.")
st.divider()
st.markdown('<div class="footer">© K&amp;K Connections · Personal matrimonial introductions · Ahmedabad, India</div>',unsafe_allow_html=True)
