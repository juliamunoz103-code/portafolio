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
]

GITHUB_USER = "juliamunoz103-code"
BIO = "Data Scientist | Estudiante de Ingeniería Biomédica (UANL) | Python · SQL · ML | Bilingüe"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Outfit:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 4rem !important; max-width: 1050px !important; }

.hero-wrap { padding: 3rem 0 2.5rem; border-bottom: 1px solid #2a2a2a; margin-bottom: 2.5rem; }
.hero-tag { font-size: 11px; letter-spacing: 0.15em; text-transform: uppercase; color: #666; margin-bottom: 0.5rem; }
.hero-name { font-family: 'Syne', sans-serif; font-size: 3.5rem; font-weight: 800; line-height: 1.05; letter-spacing: -0.02em; margin-bottom: 0.75rem; background: linear-gradient(135deg, #6C63FF, #FF6B6B); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; display: inline-block; }
.hero-bio { font-size: 1rem; color: #888; line-height: 1.7; max-width: 540px; font-weight: 300; margin-bottom: 1.5rem; }
.hero-links { display: flex; flex-wrap: wrap; gap: 8px; }
.pill { display: inline-flex; align-items: center; gap: 6px; padding: 7px 16px; border-radius: 100px; font-size: 13px; font-weight: 500; text-decoration: none; border: 1px solid #333; color: #CCC; background: transparent; }

.stats-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 2.5rem; }
.stat-card { background: #161616; border: 1px solid #222; border-radius: 16px; padding: 1.25rem; text-align: center; }
.stat-n { font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; color: #F0F0F0; line-height: 1; }
.stat-l { font-size: 12px; color: #666; margin-top: 4px; }

.section-header { display: flex; align-items: center; gap: 12px; margin-bottom: 1.25rem; }
.section-title { font-family: 'Syne', sans-serif; font-size: 1.3rem; font-weight: 700; color: #F0F0F0; white-space: nowrap; }
.section-line { flex: 1; height: 1px; background: #222; }

.projects-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 3rem; }
.project-card { border-radius: 18px; border: 1px solid #222; background: #111; overflow: hidden; }
.card-accent { height: 4px; }
.card-body { padding: 1.25rem; }
.card-emoji { font-size: 1.75rem; margin-bottom: 0.6rem; display: block; }
.card-title { font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700; color: #F0F0F0; margin-bottom: 0.4rem; }
.card-desc { font-size: 13px; color: #777; line-height: 1.6; margin-bottom: 0.9rem; font-weight: 300; }
.tags-row { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 1rem; }
.tag { font-size: 11px; padding: 3px 10px; border-radius: 100px; font-weight: 500; border: 1px solid; }
.launch-btn { display: inline-flex; align-items: center; gap: 6px; text-decoration: none; font-size: 13px; font-weight: 500; padding: 7px 16px; border-radius: 100px; color: white; }

.repos-wrap { display: flex; flex-direction: column; gap: 0; }
.repo-item { padding: 0.6rem 0; border-bottom: 1px solid #1E1E1E; display: flex; align-items: center; justify-content: space-between; }
.repo-item:last-child { border-bottom: none; }
.repo-item-name { font-size: 14px; color: #9B94FF; font-weight: 500; }
.repo-item-lang { font-size: 11px; color: #555; }

.footer { text-align: center; padding: 2rem 0 1rem; border-top: 1px solid #1E1E1E; margin-top: 2rem; color: #444; font-size: 13px; }
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
    <a class="pill" href="mailto:contacto@julia.com">✉ Contacto</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="stats-row">
  <div class="stat-card"><div class="stat-n">{pub_repos}</div><div class="stat-l">Repositorios públicos</div></div>
  <div class="stat-card"><div class="stat-n">3</div><div class="stat-l">Apps en producción</div></div>
  <div class="stat-card"><div class="stat-n">{followers}</div><div class="stat-l">Seguidores en GitHub</div></div>
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

for p in PROJECTS:
    tags_html = "".join(
        f'<span class="tag" style="color:{p["text"]};border-color:{p["color"]}44;background:{p["bg"]}22">{t}</span>'
        for t in p["tags"]
    )
    st.markdown(f"""
<div class="project-card">
  <div class="card-accent" style="background:{p['color']}"></div>
  <div class="card-body">
    <span class="card-emoji">{p['emoji']}</span>
    <div class="card-title">{p['title']}</div>
    <p class="card-desc">{p['desc']}</p>
    <div class="tags-row">{tags_html}</div>
    <a class="launch-btn" href="{p['url']}" target="_blank" style="background:{p['color']}">Abrir app →</a>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── Repos — solo títulos en tabla limpia ──────────────────────────────────────
if repos:
    st.markdown("""
    <div class="section-header" style="margin-top:0.5rem">
      <span class="section-title">Repositorios</span>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    public_repos = [r for r in repos if isinstance(r, dict) and not r.get("fork")]

    # Construir toda la lista en un solo bloque HTML
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
</div>
""", unsafe_allow_html=True)
