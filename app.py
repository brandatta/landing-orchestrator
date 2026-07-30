
import streamlit as st


st.set_page_config(
    page_title="Brandatta Orchestrator",
    page_icon="◼",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ---------------------------------------------------------------------
# Configuración general
# ---------------------------------------------------------------------

CONTACT_EMAIL = "contacto@brandatta.com"
DEMO_URL = f"mailto:{CONTACT_EMAIL}?subject=Solicitud%20de%20demostraci%C3%B3n%20-%20Brandatta%20Orchestrator"
PROCESS_URL = f"mailto:{CONTACT_EMAIL}?subject=An%C3%A1lisis%20de%20proceso%20-%20Brandatta%20Orchestrator"


# ---------------------------------------------------------------------
# Estilos
# ---------------------------------------------------------------------

st.markdown(
    """
    <style>
        :root {
            --bg: #f4f6f8;
            --surface: #ffffff;
            --surface-soft: #eef2f5;
            --text: #14212b;
            --muted: #5d6b76;
            --line: #dce3e8;
            --primary: #0a6ed1;
            --primary-dark: #074f9a;
            --dark: #071b2b;
            --success: #18864b;
            --shadow: 0 16px 48px rgba(9, 30, 66, 0.10);
        }

        html {
            scroll-behavior: smooth;
        }

        .stApp {
            background:
                radial-gradient(circle at 85% 5%, rgba(10, 110, 209, 0.11), transparent 27rem),
                linear-gradient(180deg, #ffffff 0%, var(--bg) 30%, #ffffff 100%);
            color: var(--text);
        }

        [data-testid="stHeader"] {
            background: rgba(255,255,255,0.88);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid rgba(220, 227, 232, 0.85);
        }

        [data-testid="stToolbar"] {
            right: 1rem;
        }

        .block-container {
            max-width: 1220px;
            padding-top: 1.5rem;
            padding-bottom: 4rem;
        }

        .brandbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 2rem;
            padding: 0.3rem 0 1.4rem;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            font-weight: 760;
            font-size: 1.02rem;
            letter-spacing: -0.02em;
        }

        .brand-mark {
            width: 34px;
            height: 34px;
            border-radius: 8px;
            background:
                linear-gradient(135deg, #0a6ed1 0%, #54b4ff 100%);
            box-shadow: 0 8px 22px rgba(10, 110, 209, 0.25);
            position: relative;
        }

        .brand-mark:before,
        .brand-mark:after {
            content: "";
            position: absolute;
            background: rgba(255,255,255,0.92);
            border-radius: 2px;
        }

        .brand-mark:before {
            width: 16px;
            height: 4px;
            left: 9px;
            top: 9px;
        }

        .brand-mark:after {
            width: 4px;
            height: 16px;
            left: 15px;
            top: 9px;
        }

        .eyebrow {
            color: var(--primary);
            text-transform: uppercase;
            font-size: 0.76rem;
            font-weight: 760;
            letter-spacing: 0.12em;
            margin-bottom: 0.9rem;
        }

        .hero {
            background:
                linear-gradient(120deg, rgba(7, 27, 43, 0.98), rgba(8, 61, 106, 0.97)),
                var(--dark);
            border-radius: 28px;
            padding: clamp(2rem, 5vw, 5rem);
            color: white;
            box-shadow: var(--shadow);
            overflow: hidden;
            position: relative;
            margin-bottom: 5rem;
        }

        .hero:after {
            content: "";
            position: absolute;
            width: 420px;
            height: 420px;
            right: -130px;
            top: -180px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(83, 181, 255, .32), transparent 65%);
        }

        .hero-grid {
            display: grid;
            grid-template-columns: minmax(0, 1.1fr) minmax(320px, .9fr);
            gap: 3rem;
            align-items: center;
            position: relative;
            z-index: 2;
        }

        .hero h1 {
            font-size: clamp(2.6rem, 5.4vw, 5.2rem);
            line-height: 0.98;
            letter-spacing: -0.055em;
            margin: 0 0 1.5rem;
            max-width: 850px;
        }

        .hero p {
            font-size: clamp(1.02rem, 1.7vw, 1.28rem);
            line-height: 1.62;
            color: rgba(255,255,255,.78);
            max-width: 760px;
            margin: 0 0 1.8rem;
        }

        .button-row {
            display: flex;
            flex-wrap: wrap;
            gap: .85rem;
            margin-top: 1.8rem;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: .55rem;
            min-height: 46px;
            padding: .78rem 1.25rem;
            border-radius: 8px;
            font-weight: 720;
            text-decoration: none !important;
            transition: .2s ease;
        }

        .btn-primary {
            background: #ffffff;
            color: var(--dark) !important;
        }

        .btn-primary:hover {
            transform: translateY(-1px);
            box-shadow: 0 10px 25px rgba(0,0,0,.18);
        }

        .btn-secondary {
            color: white !important;
            border: 1px solid rgba(255,255,255,.32);
            background: rgba(255,255,255,.06);
        }

        .btn-secondary:hover {
            background: rgba(255,255,255,.12);
        }

        .orchestration-panel {
            border: 1px solid rgba(255,255,255,.16);
            background: rgba(255,255,255,.08);
            border-radius: 18px;
            padding: 1.1rem;
            backdrop-filter: blur(10px);
        }

        .panel-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: .84rem;
            color: rgba(255,255,255,.68);
            margin-bottom: 1rem;
        }

        .status-pill {
            color: #b7f6cd;
            background: rgba(34,197,94,.13);
            border: 1px solid rgba(134,239,172,.24);
            border-radius: 999px;
            padding: .32rem .62rem;
            font-size: .72rem;
            font-weight: 700;
        }

        .flow-item {
            display: grid;
            grid-template-columns: 34px 1fr auto;
            gap: .75rem;
            align-items: center;
            padding: .85rem .8rem;
            border-radius: 10px;
            background: rgba(255,255,255,.07);
            margin-bottom: .55rem;
        }

        .flow-number {
            width: 30px;
            height: 30px;
            display: grid;
            place-items: center;
            border-radius: 8px;
            background: rgba(83,181,255,.17);
            color: #9fd5ff;
            font-size: .77rem;
            font-weight: 760;
        }

        .flow-title {
            font-size: .88rem;
            font-weight: 690;
        }

        .flow-subtitle {
            font-size: .73rem;
            color: rgba(255,255,255,.54);
            margin-top: .1rem;
        }

        .flow-check {
            color: #7ee2a3;
            font-weight: 900;
        }

        .section {
            padding: 1.5rem 0 4.5rem;
        }

        .section-heading {
            max-width: 800px;
            margin-bottom: 2.2rem;
        }

        .section-heading h2 {
            font-size: clamp(2rem, 3.5vw, 3.4rem);
            line-height: 1.08;
            letter-spacing: -0.04em;
            margin: 0 0 1rem;
        }

        .section-heading p {
            color: var(--muted);
            font-size: 1.07rem;
            line-height: 1.72;
            margin: 0;
        }

        .feature-grid,
        .benefit-grid,
        .usecase-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
        }

        .feature-card,
        .benefit-card,
        .usecase-card {
            background: rgba(255,255,255,.86);
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 1.5rem;
            min-height: 210px;
            box-shadow: 0 8px 28px rgba(9,30,66,.045);
        }

        .card-kicker {
            width: 42px;
            height: 42px;
            display: grid;
            place-items: center;
            border-radius: 10px;
            background: rgba(10,110,209,.10);
            color: var(--primary);
            font-weight: 850;
            margin-bottom: 1.1rem;
        }

        .feature-card h3,
        .benefit-card h3,
        .usecase-card h3 {
            margin: 0 0 .65rem;
            font-size: 1.12rem;
            letter-spacing: -0.02em;
        }

        .feature-card p,
        .benefit-card p,
        .usecase-card p {
            color: var(--muted);
            line-height: 1.62;
            margin: 0;
            font-size: .94rem;
        }

        .split-section {
            display: grid;
            grid-template-columns: minmax(0, .95fr) minmax(340px, 1.05fr);
            gap: 2.2rem;
            align-items: center;
        }

        .enterprise-box {
            background: var(--dark);
            color: white;
            border-radius: 22px;
            padding: 2rem;
            box-shadow: var(--shadow);
        }

        .enterprise-box p {
            color: rgba(255,255,255,.68);
            line-height: 1.65;
        }

        .system-tags {
            display: flex;
            flex-wrap: wrap;
            gap: .6rem;
            margin-top: 1.3rem;
        }

        .system-tag {
            border: 1px solid rgba(255,255,255,.16);
            background: rgba(255,255,255,.07);
            border-radius: 999px;
            padding: .58rem .85rem;
            font-size: .84rem;
            color: rgba(255,255,255,.9);
        }

        .macro {
            background: linear-gradient(180deg, #ffffff, #f6f8fa);
            border: 1px solid var(--line);
            border-radius: 20px;
            padding: 1.35rem;
        }

        .macro-step {
            display: grid;
            grid-template-columns: 38px 1fr;
            gap: .85rem;
            align-items: start;
            padding: .95rem;
            background: white;
            border: 1px solid var(--line);
            border-radius: 12px;
            margin-bottom: .75rem;
        }

        .macro-step:last-child {
            margin-bottom: 0;
        }

        .macro-step-index {
            width: 36px;
            height: 36px;
            display: grid;
            place-items: center;
            background: var(--primary);
            color: white;
            border-radius: 9px;
            font-size: .78rem;
            font-weight: 800;
        }

        .macro-step strong {
            display: block;
            margin-bottom: .18rem;
            color: var(--text);
        }

        .macro-step span {
            color: var(--muted);
            font-size: .88rem;
        }

        .quote-band {
            background: var(--surface-soft);
            border-left: 4px solid var(--primary);
            padding: 1.35rem 1.5rem;
            border-radius: 0 14px 14px 0;
            color: var(--text);
            font-size: 1.05rem;
            line-height: 1.65;
        }

        .cta-panel {
            background:
                linear-gradient(125deg, rgba(10,110,209,.98), rgba(4,69,132,.98));
            border-radius: 24px;
            color: white;
            padding: clamp(2rem, 4vw, 4rem);
            margin-top: 2.5rem;
            box-shadow: var(--shadow);
        }

        .cta-panel h2 {
            font-size: clamp(2rem, 3.5vw, 3.2rem);
            letter-spacing: -0.04em;
            margin: 0 0 1rem;
            max-width: 820px;
        }

        .cta-panel p {
            color: rgba(255,255,255,.76);
            line-height: 1.65;
            max-width: 800px;
        }

        .fineprint {
            color: var(--muted);
            font-size: .78rem;
            line-height: 1.5;
        }

        .footer {
            padding: 3rem 0 1rem;
            color: var(--muted);
            font-size: .86rem;
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            flex-wrap: wrap;
        }

        div[data-testid="stForm"] {
            background: white;
            border: 1px solid var(--line);
            border-radius: 18px;
            padding: 1.4rem;
            box-shadow: 0 10px 35px rgba(9,30,66,.06);
        }

        div[data-testid="stExpander"] {
            border: 1px solid var(--line);
            background: rgba(255,255,255,.84);
            border-radius: 12px;
            margin-bottom: .65rem;
        }

        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox [data-baseweb="select"] {
            border-radius: 8px;
        }

        .stButton > button,
        .stFormSubmitButton > button {
            border-radius: 8px;
            min-height: 44px;
            font-weight: 720;
            border: none;
            background: var(--primary);
            color: white;
        }

        .stButton > button:hover,
        .stFormSubmitButton > button:hover {
            background: var(--primary-dark);
            color: white;
            border: none;
        }

        @media (max-width: 900px) {
            .hero-grid,
            .split-section {
                grid-template-columns: 1fr;
            }

            .feature-grid,
            .benefit-grid,
            .usecase-grid {
                grid-template-columns: 1fr;
            }

            .hero {
                border-radius: 20px;
                margin-bottom: 3.5rem;
            }

            .brandbar {
                align-items: flex-start;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------
# Navegación / marca
# ---------------------------------------------------------------------

st.markdown(
    """
    <div class="brandbar">
        <div class="brand">
            <div class="brand-mark"></div>
            <div>Brandatta Orchestrator</div>
        </div>
        <div style="color:#5d6b76;font-size:.88rem;">
            Orquestación empresarial
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------

st.markdown(
    f"""
    <section class="hero">
        <div class="hero-grid">
            <div>
                <div class="eyebrow" style="color:#8fcbff;">Brandatta Orchestrator</div>
                <h1>Conecte procesos, datos y sistemas desde una única plataforma</h1>
                <p>
                    Simplifique la operación de procesos empresariales que involucran
                    SAP, bases de datos, archivos y servicios distribuidos.
                    Programe, ejecute, supervise y audite flujos operativos desde un
                    entorno centralizado.
                </p>
                <div class="button-row">
                    <a class="btn btn-primary" href="{DEMO_URL}">
                        Solicitar una demostración
                    </a>
                    <a class="btn btn-secondary" href="#contacto">
                        Analizar un proceso
                    </a>
                </div>
            </div>

            <div class="orchestration-panel">
                <div class="panel-header">
                    <span>Macro · Actualización operativa</span>
                    <span class="status-pill">Ejecución completada</span>
                </div>

                <div class="flow-item">
                    <div class="flow-number">01</div>
                    <div>
                        <div class="flow-title">Extracción desde SAP</div>
                        <div class="flow-subtitle">Origen: SAP S/4HANA</div>
                    </div>
                    <div class="flow-check">✓</div>
                </div>

                <div class="flow-item">
                    <div class="flow-number">02</div>
                    <div>
                        <div class="flow-title">Procesamiento de datos</div>
                        <div class="flow-subtitle">Stored Procedures · SQL Server</div>
                    </div>
                    <div class="flow-check">✓</div>
                </div>

                <div class="flow-item">
                    <div class="flow-number">03</div>
                    <div>
                        <div class="flow-title">Generación de reporte</div>
                        <div class="flow-subtitle">Archivo consolidado</div>
                    </div>
                    <div class="flow-check">✓</div>
                </div>

                <div class="flow-item">
                    <div class="flow-number">04</div>
                    <div>
                        <div class="flow-title">Distribución</div>
                        <div class="flow-subtitle">Repositorio remoto y correo</div>
                    </div>
                    <div class="flow-check">✓</div>
                </div>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------
# Problema y propuesta de valor
# ---------------------------------------------------------------------

st.markdown(
    """
    <section class="section">
        <div class="section-heading">
            <div class="eyebrow">Procesos integrados</div>
            <h2>Transforme tareas aisladas en procesos empresariales coordinados</h2>
            <p>
                Una operación puede comenzar en SAP, continuar en una base de datos,
                generar archivos, transferirlos a otro entorno y finalizar con el
                envío de un reporte. Aunque estas acciones forman parte de un mismo
                proceso, suelen administrarse mediante herramientas independientes,
                scripts, tareas programadas y controles manuales.
            </p>
        </div>

        <div class="quote-band">
            Brandatta Orchestrator proporciona una capa central de coordinación
            para integrar estas acciones dentro de un flujo único, controlado y
            auditable, sin reemplazar la infraestructura ni la lógica de negocio existente.
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------
# Capacidades
# ---------------------------------------------------------------------

features = [
    (
        "01",
        "Programación centralizada",
        "Administre desde un mismo entorno procesos que antes dependían de cron, Task Scheduler, scripts independientes o schedulers distribuidos.",
    ),
    (
        "02",
        "Ejecución de Stored Procedures",
        "Ejecute la lógica almacenada en MySQL y SQL Server e incorpórela dentro de procesos más amplios, secuenciales y auditables.",
    ),
    (
        "03",
        "Transferencia de archivos",
        "Traslade archivos de forma bidireccional entre unidades locales, servidores y repositorios remotos.",
    ),
    (
        "04",
        "Macros operativas",
        "Combine múltiples tareas dentro de una única secuencia, con un orden de ejecución definido y una trazabilidad común.",
    ),
    (
        "05",
        "Monitoreo de procesos",
        "Consulte el estado de las ejecuciones y detecte con rapidez la etapa en la que se produjo una demora o interrupción.",
    ),
    (
        "06",
        "Auditoría centralizada",
        "Mantenga un historial de los procesos ejecutados, sus resultados y los pasos que formaron parte de cada operación.",
    ),
]

feature_html = "".join(
    f"""
    <div class="feature-card">
        <div class="card-kicker">{number}</div>
        <h3>{title}</h3>
        <p>{description}</p>
    </div>
    """
    for number, title, description in features
)

st.markdown(
    f"""
    <section class="section">
        <div class="section-heading">
            <div class="eyebrow">Capacidades</div>
            <h2>Obtenga una visión completa de sus procesos</h2>
            <p>
                Centralice la ejecución de tareas distribuidas entre diferentes
                sistemas y entornos tecnológicos. Conozca el estado de cada proceso,
                reduzca la dependencia de controles manuales y facilite el diagnóstico.
            </p>
        </div>

        <div class="feature-grid">
            {feature_html}
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------
# Integraciones y macro
# ---------------------------------------------------------------------

st.markdown(
    """
    <section class="section">
        <div class="split-section">
            <div class="enterprise-box">
                <div class="eyebrow" style="color:#8fcbff;">Infraestructura existente</div>
                <h2 style="font-size:2.35rem;letter-spacing:-.04em;margin-top:0;">
                    Integre los sistemas que ya utiliza
                </h2>
                <p>
                    Brandatta Orchestrator se conecta con la infraestructura existente
                    y permite aprovechar la lógica implementada en cada organización.
                    No es necesario reemplazar los sistemas actuales: la plataforma
                    los incorpora dentro de procesos centralizados.
                </p>

                <div class="system-tags">
                    <span class="system-tag">SAP R/3</span>
                    <span class="system-tag">SAP S/4HANA</span>
                    <span class="system-tag">SAP Business One</span>
                    <span class="system-tag">MySQL</span>
                    <span class="system-tag">Microsoft SQL Server</span>
                    <span class="system-tag">Archivos locales</span>
                    <span class="system-tag">Repositorios remotos</span>
                </div>
            </div>

            <div>
                <div class="eyebrow">Ejemplo de macro</div>
                <div class="macro">
                    <div class="macro-step">
                        <div class="macro-step-index">01</div>
                        <div>
                            <strong>Obtener información desde SAP</strong>
                            <span>Iniciar la operación desde el ERP correspondiente.</span>
                        </div>
                    </div>

                    <div class="macro-step">
                        <div class="macro-step-index">02</div>
                        <div>
                            <strong>Ejecutar procesos de transformación</strong>
                            <span>Aplicar Stored Procedures en MySQL o SQL Server.</span>
                        </div>
                    </div>

                    <div class="macro-step">
                        <div class="macro-step-index">03</div>
                        <div>
                            <strong>Generar y transferir archivos</strong>
                            <span>Publicar resultados en el repositorio definido.</span>
                        </div>
                    </div>

                    <div class="macro-step">
                        <div class="macro-step-index">04</div>
                        <div>
                            <strong>Notificar el resultado</strong>
                            <span>Enviar reportes y mantener evidencia de la ejecución.</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------
# Casos de uso
# ---------------------------------------------------------------------

use_cases = [
    (
        "BI",
        "Actualizaciones de Business Intelligence",
        "Coordine la extracción, transformación, actualización de tablas, generación de archivos y distribución de reportes.",
    ),
    (
        "SAP",
        "Integraciones SAP y bases de datos",
        "Centralice procesos que trasladan información entre SAP, MySQL, SQL Server y otros componentes operativos.",
    ),
    (
        "CL",
        "Cierres operativos y contables",
        "Ejecute secuencialmente los procesos requeridos para cierres diarios, mensuales o anuales.",
    ),
    (
        "RP",
        "Generación y distribución de reportes",
        "Automatice la preparación de información, creación de archivos y envío a usuarios internos o externos.",
    ),
    (
        "AR",
        "Intercambio de archivos",
        "Gestione transferencias entre servidores, unidades locales y repositorios remotos como parte de un proceso completo.",
    ),
    (
        "DT",
        "Regularización de datos",
        "Programe procedimientos que corrigen, consolidan o normalizan información antes de su utilización.",
    ),
]

use_case_html = "".join(
    f"""
    <div class="usecase-card">
        <div class="card-kicker">{code}</div>
        <h3>{title}</h3>
        <p>{description}</p>
    </div>
    """
    for code, title, description in use_cases
)

st.markdown(
    f"""
    <section class="section">
        <div class="section-heading">
            <div class="eyebrow">Casos de uso</div>
            <h2>Diseñado para procesos empresariales críticos</h2>
            <p>
                Comience con un proceso específico y amplíe progresivamente el alcance
                de la solución hacia otras áreas, sistemas y operaciones.
            </p>
        </div>

        <div class="usecase-grid">
            {use_case_html}
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------
# Beneficios
# ---------------------------------------------------------------------

benefits = [
    (
        "TR",
        "Mayor trazabilidad",
        "Acceda a una visión centralizada de los procesos y a la evidencia de cada ejecución.",
    ),
    (
        "CO",
        "Mayor control operativo",
        "Comprenda qué etapas se completaron, dónde se interrumpió una ejecución y qué procesos pudieron verse afectados.",
    ),
    (
        "DI",
        "Diagnóstico más rápido",
        "Reduzca el tiempo necesario para localizar fallas y determinar acciones de recuperación.",
    ),
    (
        "RE",
        "Procesos reutilizables",
        "Convierta acciones técnicas recurrentes en secuencias configurables, repetibles y auditables.",
    ),
    (
        "DP",
        "Menor dependencia",
        "Disminuya la dependencia de servidores aislados, controles manuales y conocimiento concentrado.",
    ),
    (
        "IN",
        "Inversión protegida",
        "Aproveche los sistemas, Stored Procedures y desarrollos que su organización ya utiliza.",
    ),
]

benefit_html = "".join(
    f"""
    <div class="benefit-card">
        <div class="card-kicker">{code}</div>
        <h3>{title}</h3>
        <p>{description}</p>
    </div>
    """
    for code, title, description in benefits
)

st.markdown(
    f"""
    <section class="section">
        <div class="section-heading">
            <div class="eyebrow">Valor operativo</div>
            <h2>Reduzca la complejidad de su operación</h2>
            <p>
                Pase de tareas técnicas distribuidas a procesos empresariales
                centralizados, repetibles y supervisados.
            </p>
        </div>

        <div class="benefit-grid">
            {benefit_html}
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------
# CTA
# ---------------------------------------------------------------------

st.markdown(
    """
    <section class="cta-panel">
        <div class="eyebrow" style="color:#c5e3ff;">Brandatta Orchestrator</div>
        <h2>Convierta sus procesos en operaciones controladas</h2>
        <p>
            Descubra cómo centralizar, automatizar y auditar los procesos que
            conectan SAP, bases de datos, Stored Procedures, archivos y reportes.
        </p>
        <div class="button-row">
            <a class="btn btn-primary" href="#contacto">Analizar un proceso</a>
            <a class="btn btn-secondary" href="mailto:contacto@brandatta.com?subject=Solicitud%20de%20demostraci%C3%B3n%20-%20Brandatta%20Orchestrator">
                Solicitar una demostración
            </a>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------
# Formulario
# ---------------------------------------------------------------------

st.markdown('<div id="contacto"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <section class="section" style="padding-top:4.5rem;">
        <div class="section-heading">
            <div class="eyebrow">Contacto</div>
            <h2>Analice un proceso junto con Brandatta</h2>
            <p>
                Seleccione un proceso que hoy dependa de múltiples sistemas,
                tareas o controles. La información permitirá realizar un primer
                diagnóstico de orquestación.
            </p>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

with st.form("contact_form", clear_on_submit=False):
    col1, col2 = st.columns(2)

    with col1:
        nombre = st.text_input("Nombre y apellido *")
        empresa = st.text_input("Empresa *")
        email = st.text_input("Correo corporativo *")

    with col2:
        cargo = st.text_input("Cargo")
        frecuencia = st.selectbox(
            "Frecuencia del proceso",
            [
                "Seleccione una opción",
                "En tiempo real",
                "Varias veces por día",
                "Diaria",
                "Semanal",
                "Mensual",
                "Bajo demanda",
            ],
        )
        sistemas = st.text_input(
            "Sistemas involucrados",
            placeholder="Ej.: SAP S/4HANA, MySQL, SFTP",
        )

    proceso = st.text_area(
        "Descripción del proceso actual *",
        placeholder=(
            "Describa brevemente cómo comienza el proceso, qué pasos ejecuta, "
            "qué sistemas intervienen y cuál es el resultado esperado."
        ),
        height=150,
    )

    dificultad = st.text_area(
        "Principal dificultad o punto de falla",
        placeholder=(
            "Ej.: falta de visibilidad, múltiples schedulers, errores difíciles "
            "de diagnosticar, controles manuales o reprocesos."
        ),
        height=110,
    )

    aceptar = st.checkbox(
        "Acepto que Brandatta utilice esta información para contactarme por esta solicitud."
    )

    submitted = st.form_submit_button("Enviar solicitud", use_container_width=True)

    if submitted:
        missing = []

        if not nombre.strip():
            missing.append("nombre")
        if not empresa.strip():
            missing.append("empresa")
        if not email.strip() or "@" not in email:
            missing.append("correo válido")
        if not proceso.strip():
            missing.append("descripción del proceso")
        if not aceptar:
            missing.append("aceptación de contacto")

        if missing:
            st.error("Complete los siguientes campos: " + ", ".join(missing) + ".")
        else:
            st.success(
                "La solicitud fue validada correctamente. "
                "Conecte este formulario con su servicio de correo, CRM o API para enviarla."
            )
            st.code(
                {
                    "nombre": nombre,
                    "empresa": empresa,
                    "email": email,
                    "cargo": cargo,
                    "frecuencia": frecuencia,
                    "sistemas": sistemas,
                    "proceso": proceso,
                    "dificultad": dificultad,
                },
                language="python",
            )

st.markdown(
    """
    <p class="fineprint">
        Nota técnica: este ejemplo valida el formulario en pantalla, pero no envía
        los datos a un backend. En producción puede conectarse con una API,
        un webhook, un CRM, una base de datos o un servicio de correo.
    </p>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------
# Preguntas frecuentes
# ---------------------------------------------------------------------

st.markdown(
    """
    <section class="section">
        <div class="section-heading">
            <div class="eyebrow">Preguntas frecuentes</div>
            <h2>Información sobre la solución</h2>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

faq = [
    (
        "¿Brandatta Orchestrator reemplaza los sistemas existentes?",
        "No. La plataforma se integra con los sistemas y bases de datos que la organización ya utiliza. Su función es coordinar, programar y supervisar las acciones ejecutadas sobre ellos.",
    ),
    (
        "¿Es necesario modificar los Stored Procedures actuales?",
        "No. Los procedimientos existentes pueden incorporarse dentro de los procesos y macros configurados en la plataforma.",
    ),
    (
        "¿Qué es una macro?",
        "Una macro es una secuencia de acciones que se ejecutan como parte de un mismo proceso. Puede incluir procedimientos almacenados, transferencias de archivos, validaciones y notificaciones.",
    ),
    (
        "¿Se pueden programar ejecuciones automáticas?",
        "Sí. Los procesos pueden configurarse para ejecutarse automáticamente según la frecuencia y las condiciones definidas por la organización.",
    ),
    (
        "¿Es posible auditar las ejecuciones?",
        "Sí. La plataforma registra el estado y el resultado de cada proceso, facilitando el seguimiento, el análisis de errores y la trazabilidad operativa.",
    ),
    (
        "¿Se puede comenzar con un único proceso?",
        "Sí. La implementación puede comenzar con un proceso prioritario y extenderse posteriormente hacia otras áreas, sistemas y casos de uso.",
    ),
]

for question, answer in faq:
    with st.expander(question):
        st.write(answer)


# ---------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------

st.markdown(
    f"""
    <footer class="footer">
        <div>
            <strong style="color:#14212b;">Brandatta Orchestrator</strong><br>
            Orquestación de procesos empresariales.
        </div>
        <div>
            <a href="mailto:{CONTACT_EMAIL}" style="color:#0a6ed1;text-decoration:none;">
                {CONTACT_EMAIL}
            </a>
        </div>
        <div>© 2026 Brandatta</div>
    </footer>
    """,
    unsafe_allow_html=True,
)
