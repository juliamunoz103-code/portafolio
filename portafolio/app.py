import streamlit as st
import requests

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Julia Muñoz · Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Projects data ─────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "title": "Hospital Dashboard",
        "emoji": "🏥",
        "desc": "Dashboard interactivo con indicadores hospitalarios clave: ocupación, tiempos de espera y métricas de calidad clínica visualizadas en tiempo real.",
        "tags": ["Streamlit", "Pandas", "Plotly", "Healthcare"],
        "url": "https://hospital-dashboard-i5hakypywznrju2j4hxdfe.streamlit.app/",
        "color": "#6C63FF",
        "bg": "#F0EFFE",
    },
    {
        "title": "Diabetes Predictor",
        "emoji": "🧬",
        "desc": "Modelo de machine learning que predice riesgo de diabetes a partir de variables clínicas. Interfaz intuitiva para explorar predicciones y probabilidades.",
        "tags": ["Scikit-learn", "ML", "Salud", "Predicción"],
        "url": "https://diabetes-predictor-nftrywymihqfxj7njksayk.streamlit.app/",
        "color": "#0FB77A",
        "bg": "#E6FAF3",
    },
    {
        "title": "Data Science Assistant",
        "emoji": "🤖",
        "desc": "Asistente de IA para análisis de datos con lenguaje natural. Genera visualizaciones, estadísticas y responde preguntas sobre tus datasets.",
        "tags": ["IA", "NLP", "Análisis", "Generativo"],
        "url": "https://data-science-assistant.streamlit.app/",
        "color": "#FF6B6B",
        "bg": "#FFF0F0",
    },
]

GITHUB_USER = "juliamunoz103-code"

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Outfit:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 4rem !important; max-width: 1100px !important; }

/* ── Hero ── */
.hero-wrap {
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: center;
    gap: 2rem;
    padding: 3rem 0 2.5rem;
    border-bottom: 1px solid #E5E5E5;
    margin-bottom: 3rem;
}
.hero-tag {
    font-size: 11px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #999;
    margin-bottom: 0.5rem;
    font-family: 'Outfit', sans-serif;
}
.hero-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.02em;
    color: #111;
    margin-bottom: 0.75rem;
}
.hero-name span {
    background: linear-gradient(135deg, #6C63FF, #FF6B6B);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-bio {
    font-size: 1.05rem;
    color: #555;
    line-height: 1.7;
    max-width: 520px;
    font-weight: 300;
}
.hero-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 1.5rem;
}
.pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border-radius: 100px;
    font-size: 13px;
    font-weight: 500;
    text-decoration: none;
    border: 1.5px solid #E0E0E0;
    color: #333;
    background: white;
    transition: all 0.2s;
    cursor: pointer;
}
.pill:hover { border-color: #6C63FF; color: #6C63FF; }
.avatar-box {
    width: 120px;
    height: 120px;
    border-radius: 24px;
    overflow: hidden;
    border: 3px solid #F0EFFE;
    box-shadow: 0 0 0 6px #FAF9FF;
    flex-shrink: 0;
}
.avatar-box img { width: 100%; height: 100%; object-fit: cover; }
.avatar-initials {
    width: 120px;
    height: 120px;
    border-radius: 24px;
    background: linear-gradient(135deg, #6C63FF, #FF6B6B);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Syne', sans-serif;
    font-size: 2.5rem;
    font-weight: 800;
    color: white;
}

/* ── Stats ── */
.stats-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-bottom: 3rem;
}
.stat-card {
    background: #FAFAFA;
    border: 1px solid #EFEFEF;
    border-radius: 16px;
    padding: 1.25rem 1.5rem;
    text-align: center;
}
.stat-n {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #111;
    line-height: 1;
}
.stat-l {
    font-size: 12px;
    color: #999;
    margin-top: 4px;
    font-weight: 400;
}

/* ── Section header ── */
.section-header {
    display: flex;
    align-items: baseline;
    gap: 12px;
    margin-bottom: 1.5rem;
}
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #111;
}
.section-line {
    flex: 1;
    height: 1px;
    background: #E5E5E5;
}

/* ── Project cards ── */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    margin-bottom: 3.5rem;
}
.project-card {
    border-radius: 20px;
    border: 1px solid #EEEEEE;
    background: white;
    overflow: hidden;
    transition: transform 0.2s, box-shadow 0.2s;
    cursor: pointer;
}
.project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.08);
}
.card-accent {
    height: 5px;
}
.card-body {
    padding: 1.5rem;
}
.card-emoji {
    font-size: 2rem;
    margin-bottom: 0.75rem;
    display: block;
}
.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #111;
    margin-bottom: 0.5rem;
}
.card-desc {
    font-size: 13.5px;
    color: #666;
    line-height: 1.65;
    margin-bottom: 1rem;
    font-weight: 300;
}
.tags-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 1.25rem;
}
.tag {
    font-size: 11px;
    padding: 3px 10px;
    border-radius: 100px;
    font-weight: 500;
    border: 1px solid;
}
.launch-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    text-decoration: none;
    font-size: 13px;
    font-weight: 500;
    padding: 8px 18px;
    border-radius: 100px;
    color: white;
    transition: opacity 0.2s;
}
.launch-btn:hover { opacity: 0.85; }

/* ── Repos ── */
.repo-card {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1rem 1.25rem;
    border: 1px solid #EEEEEE;
    border-radius: 14px;
    background: white;
    margin-bottom: 10px;
    cursor: pointer;
    transition: border-color 0.15s, background 0.15s;
    text-decoration: none;
}
.repo-card:hover { border-color: #C5C0FF; background: #FAFAFF; }
.repo-icon {
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: #F0EFFE;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
}
.repo-name {
    font-weight: 600;
    font-size: 14px;
    color: #6C63FF;
    margin-bottom: 2px;
}
.repo-desc { font-size: 12.5px; color: #777; line-height: 1.5; }
.repo-meta { display: flex; gap: 12px; margin-top: 6px; font-size: 11px; color: #aaa; align-items: center; }
.lang-dot { width: 8px; height: 8px; border-radius: 50%; display: inline-block; }

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 2rem 0 1rem;
    border-top: 1px solid #EEEEEE;
    margin-top: 2rem;
    color: #BBBBBB;
    font-size: 13px;
}
.footer a { color: #6C63FF; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ── GitHub data ───────────────────────────────────────────────────────────────
@st.cache_data(ttl=3600)
def fetch_github(user):
    try:
        u = requests.get(f"https://api.github.com/users/{user}", timeout=5).json()
        r = requests.get(
            f"https://api.github.com/users/{user}/repos?per_page=30&sort=updated",
            timeout=5
        ).json()
        return u, r if isinstance(r, list) else []
    except Exception:
        return {}, []

user_data, repos = fetch_github(GITHUB_USER)

name     = user_data.get("name") or "Julia Muñoz"
bio      = user_data.get("bio") or "Data Scientist apasionada por convertir datos en soluciones reales."
avatar   = user_data.get("avatar_url") or ""
pub_repos = user_data.get("public_repos") or len(repos)
followers = user_data.get("followers") or "—"

# ── Hero ──────────────────────────────────────────────────────────────────────
avatar_html = (
    f'<div class="avatar-box"><img src="{avatar}" alt="Avatar"></div>'
    if avatar else
    '<div class="avatar-initials">JM</div>'
)

st.markdown(f"""
<div class="hero-wrap">
  <div>
    <div class="hero-tag">✦ Data Science · Machine Learning · Streamlit</div>
    <h1 class="hero-name">Hola, soy<br><span>{name}</span></h1>
    <p class="hero-bio">{bio}</p>
    <div class="hero-pills">
      <a class="pill" href="https://github.com/{GITHUB_USER}" target="_blank">⟡ GitHub</a>
      <a class="pill" href="mailto:contacto@julia.com">✉ Contacto</a>
    </div>
  </div>
  {avatar_html}
</div>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="stats-row">
  <div class="stat-card"><div class="stat-n">{pub_repos}</div><div class="stat-l">Repositorios</div></div>
  <div class="stat-card"><div class="stat-n">3</div><div class="stat-l">Apps en producción</div></div>
  <div class="stat-card"><div class="stat-n">{followers}</div><div class="stat-l">Seguidores</div></div>
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
        f'<span class="tag" style="color:{p["color"]};border-color:{p["color"]}30;background:{p["bg"]}">{t}</span>'
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
        <a class="launch-btn" href="{p['url']}" target="_blank" style="background:{p['color']}">
          Abrir app →
        </a>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── GitHub Repos ──────────────────────────────────────────────────────────────
LANG_COLORS = {
    "Python": "#3572A5", "JavaScript": "#F1E05A", "HTML": "#E34C26",
    "Jupyter Notebook": "#DA5B0B", "R": "#198CE7", "CSS": "#563D7C",
}
LANG_EMOJIS = {
    "Python": "🐍", "JavaScript": "🌐", "HTML": "🔶",
    "Jupyter Notebook": "📓", "R": "📊", "CSS": "🎨",
}

if repos:
    st.markdown("""
    <div class="section-header" style="margin-top:1rem">
      <span class="section-title">Repositorios</span>
      <div class="section-line"></div>
    </div>
    """, unsafe_allow_html=True)

    public_repos = [r for r in repos if not r.get("fork") and isinstance(r, dict)]
    for r in public_repos[:12]:
        lang = r.get("language") or ""
        lang_dot = f'<span class="lang-dot" style="background:{LANG_COLORS.get(lang,"#CCC")}"></span> {lang}' if lang else ""
        stars = r.get("stargazers_count", 0)
        icon = LANG_EMOJIS.get(lang, "📁")
        desc = r.get("description") or "Sin descripción"
        st.markdown(f"""
        <a class="repo-card" href="{r.get('html_url','#')}" target="_blank">
          <div class="repo-icon">{icon}</div>
          <div style="flex:1;min-width:0">
            <div class="repo-name">{r.get('name','')}</div>
            <div class="repo-desc">{desc}</div>
            <div class="repo-meta">
              {lang_dot}
              {'⭐ ' + str(stars) if stars else ''}
            </div>
          </div>
        </a>
        """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="footer">
  Hecho con ♥ en Streamlit &nbsp;·&nbsp;
  <a href="https://github.com/{GITHUB_USER}" target="_blank">@{GITHUB_USER}</a>
</div>
""", unsafe_allow_html=True)
