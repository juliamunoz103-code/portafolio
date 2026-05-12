import streamlit as st
import requests

st.set_page_config(
    page_title="Julia Muñoz · Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PROJECTS = [
    {
        "title": "Hospital Dashboard",
        "emoji": "🏥",
        "desc": "Dashboard interactivo con indicadores hospitalarios clave: ocupación, tiempos de espera y métricas de calidad clínica.",
        "tags": ["Streamlit", "Pandas", "Plotly", "Healthcare"],
        "url": "https://hospital-dashboard-i5hakypywznrju2j4hxdfe.streamlit.app/",
        "color": "#6C63FF",
        "bg": "#F0EFFE",
        "text": "#4B44CC",
    },
    {
        "title": "Diabetes Predictor",
        "emoji": "🧬",
        "desc": "Modelo de machine learning que predice riesgo de diabetes a partir de variables clínicas.",
        "tags": ["Scikit-learn", "ML", "Salud", "Predicción"],
        "url": "https://diabetes-predictor-nftrywymihqfxj7njksayk.streamlit.app/",
        "color": "#0FB77A",
        "bg": "#E6FAF3",
        "text": "#0A8A5C",
    },
    {
        "title": "Data Science Assistant",
        "emoji": "🤖",
        "desc": "Asistente de IA para análisis de datos con lenguaje natural. Genera visualizaciones y estadísticas.",
        "tags": ["IA", "NLP", "Análisis", "Generativo"],
        "url": "https://data-science-assistant.streamlit.app/",
        "color": "#FF6B6B",
        "bg": "#FFF0F0",
        "text": "#CC4444",
    },
    {
        "title": "IngBioCalc Pro",
        "emoji": "🧬",
        "desc": "Calculadora avanzada para Ingeniería Biomédica: matrices, estadística, vectores, fórmulas con LaTeX y chatbot IA con Claude.",
        "tags": ["Biomédica", "Streamlit", "Matemáticas", "IA"],
        "url": "https://ingbiocalc-pro-qiumwmpvncvazz2kmiya8c.streamlit.app/",
        "repo_url": "https://github.com/juliamunoz103-code/ingbiocalc-pro",
        "color": "#F59E0B",
        "bg": "#FFFBEB",
        "text": "#B45309",
    },
]

GITHUB_USER = "juliamunoz103-code"
EMAIL = "julia.munozgzz@gmail.com"
BIO = "Data Scientist | Estudiante de Ingeniería Biomédica (UANL) | Python · SQL · ML | Bilingüe"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@800;900&family=Outfit:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }

/* Fondo blanco */
.stApp { background-color: #FFFFFF !important; }
.block-container { padding: 2rem 3rem 4rem !important; max-width: 1050px !important; }

.hero-wrap { padding: 3rem 0 2.5rem; border-bottom: 1px solid #E5E5E5; margin-bottom: 2.5rem; }
.hero-tag { font-size: 11px; letter-spacing: 0.15em; text-transform: uppercase; color: #AAA; margin-bottom: 0.75rem; }
.hero-name {
    font-family: 'Nunito', sans-serif;
    font-size: 4rem;
    font-weight: 900;
    line-height: 1.15;
    letter-spacing: 0em;
    margin-bottom: 0.75rem;
    background: linear-gradient(135deg, #6C63FF, #FF6B6B);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: inline-block;
}
.hero-bio { font-size: 1rem; color: #666; line-height: 1.7; max-width: 540px; font-weight: 300; margin-bottom: 1.5rem; }
.hero-links { display: flex; flex-wrap: wrap; gap: 8px; }
.pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 18px;
    border-radius: 100px;
    font-size: 13px;
    font-weight: 500;
    text-decoration: none;
    border: 1.5px solid #DDD;
    color: #444;
    background: transparent;
    transition: all 0.2s;
}
.pill:hover { border-color: #6C63FF; color: #6C63FF; }

.stats-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 2.5rem; }
.stat-card { background: #F7F7F7; border: 1px solid #EEEEEE; border-radius: 16px; padding: 1.25rem; text-align: center; }
.stat-n { font-family: 'Nunito', sans-serif; font-size: 2rem; font-weight: 800; color: #111; line-height: 1; }
.stat-l { font-size: 12px; color: #999; margin-top: 4px; }

.section-header { display: flex; align-items: center; gap: 12px; margin-bottom: 1.25rem; }
.section-title { font-family: 'Nunito', sans-serif; font-size: 1.3rem; font-weight: 700; color: #111; white-space: nowrap; }
.section-line { flex: 1; height: 1px; background: #E5E5E5; }

.projects-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 3rem; }
.project-card { border-radius: 18px; border: 1px solid #EEEEEE; background: #FFFFFF; overflow: hidden; transition: transform 0.2s, box-shadow 0.2s; }
.project-card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.07); }
.card-accent { height: 4px; }
.card-body { padding: 1.25rem; }
.card-emoji { font-size: 1.75rem; margin-bottom: 0.6rem; display: block; }
.card-title { font-family: 'Nunito', sans-serif; font-size: 1rem; font-weight: 700; color: #111; margin-bottom: 0.4rem; }
.card-desc { font-size: 13px; color: #888; line-height: 1.6; margin-bottom: 0.9rem; font-weight: 300; }
.tags-row { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 1rem; }
.tag { font-size: 11px; padding: 3px 10px; border-radius: 100px; font-weight: 500; border: 1px solid; }
.launch-btn { display: inline-flex; align-items: center; gap: 6px; text-decoration: none; font-size: 13px; font-weight: 600; padding: 7px 16px; border-radius: 100px; color: #FFFFFF !important; -webkit-text-fill-color: #FFFFFF !important; }

.repos-wrap { border: 1px solid #EEEEEE; border-radius: 16px; overflow: hidden; background: #FAFAFA; }
.repo-item { padding: 0.7rem 1.25rem; border-bottom: 1px solid #EEEEEE; display: flex; align-items: center; justify-content: space-between; }
.repo-item:last-child { border-bottom: none; }
.repo-item-name { font-size: 14px; color: #6C63FF; font-weight: 500; text-decoration: none; }
.repo-item-name:hover { text-decoration: underline; }
.repo-item-lang { font-size: 11px; color: #BBB; }

.footer { text-align: center; padding: 2rem 0 1rem; border-top: 1px solid #EEEEEE; margin-top: 2rem; color: #BBB; font-size: 13px; }
.footer a { color: #6C63FF; text-decoration: none; }
</style>
""", unsafe_allow_html=True)


@st.cache_data(ttl=3600)
def fetch_github(user):
    try:
        u = requests.get(f"https://api.github.com/users/{user}", timeout=5).json()
        r = requests.get(
            f"https://api.github.com/users/{user}/repos?per_page=30&sort=updated",
            timeout=5,
        ).json()
        return u, r if isinstance(r, list) else []
    except Exception:
        return {}, []


user_data, repos = fetch_github(GITHUB_USER)
pub_repos = user_data.get("public_repos") or len(repos)
followers = user_data.get("followers", "—")

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero-wrap">
  <div class="hero-tag">✦ Data Science · Machine Learning · Biomedical Engineering</div>
  <div class="hero-name">Julia Muñoz</div>
  <p class="hero-bio">{BIO}</p>
  <div class="hero-links">
    <a class="pill" href="https://github.com/{GITHUB_USER}" target="_blank">⟡ GitHub</a>
  </div>
</div>
""", unsafe_allow_html=True)





# ── Projects ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-header">
  <span class="section-title">Proyectos</span>
  <div class="section-line"></div>
</div>
<div class="projects-grid">
""", unsafe_allow_html=True)

cards_html = ""
for p in PROJECTS:
    tags_html = "".join(
        f'<span class="tag" style="color:{p["text"]};border-color:{p["color"]}44;background:{p["bg"]}">{t}</span>'
        for t in p["tags"]
    )
    repo_btn = (
        f'<a class="pill" href="{p["repo_url"]}" target="_blank" style="margin-left:8px;font-size:12px;">⟡ Repo</a>'
        if p.get("repo_url") else ""
    )
    cards_html += f"""
<div class="project-card">
  <div class="card-accent" style="background:{p['color']}"></div>
  <div class="card-body">
    <span class="card-emoji">{p['emoji']}</span>
    <div class="card-title">{p['title']}</div>
    <p class="card-desc">{p['desc']}</p>
    <div class="tags-row">{tags_html}</div>
    <div style="display:flex;align-items:center;flex-wrap:wrap;gap:6px;">
      <a class="launch-btn" href="{p['url']}" target="_blank" style="background:{p['color']}">Abrir app →</a>
      {repo_btn}
    </div>
  </div>
</div>"""

st.markdown(cards_html + "</div>", unsafe_allow_html=True)

# ── Repos ─────────────────────────────────────────────────────────────────────
if repos:
    st.markdown("""
    <div class="section-header" style="margin-top:0.5rem">
      <span class="section-title">Repositorios</span>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    public_repos = [r for r in repos if isinstance(r, dict) and not r.get("fork")]

    items_html = ""
    for r in public_repos[:15]:
        lang = r.get("language") or ""
        url = r.get("html_url", "#")
        name = r.get("name", "")
        items_html += (
            f'<div class="repo-item">'
            f'<a href="{url}" target="_blank" class="repo-item-name">{name}</a>'
            f'<span class="repo-item-lang">{lang}</span>'
            f'</div>'
        )

    st.markdown(f'<div class="repos-wrap">{items_html}</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="footer">
  Hecho con ♥ en Streamlit &nbsp;·&nbsp;
  <a href="https://github.com/{GITHUB_USER}" target="_blank">@{GITHUB_USER}</a>
  &nbsp;·&nbsp;
  <a href="mailto:{EMAIL}">{EMAIL}</a>
</div>
""", unsafe_allow_html=True)
