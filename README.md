# Brandatta Orchestrator

Landing institucional desarrollada con Streamlit.

## Estructura del repositorio

```text
brandatta-orchestrator/
├── .streamlit/
│   └── config.toml
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## Ejecutar localmente

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Subir a GitHub desde la terminal

```bash
git init
git add .
git commit -m "Landing inicial de Brandatta Orchestrator"
git branch -M main
git remote add origin https://github.com/USUARIO/NOMBRE-REPOSITORIO.git
git push -u origin main
```

También se pueden cargar los archivos desde **Add file > Upload files** en GitHub.

## Publicar en Streamlit Community Cloud

1. Ingresar a Streamlit Community Cloud.
2. Seleccionar **Create app** o **New app**.
3. Elegir el repositorio de GitHub.
4. Seleccionar la rama `main`.
5. Indicar `app.py` como archivo principal.
6. Presionar **Deploy**.

## Configuración

El correo comercial se define al comienzo de `app.py`:

```python
CONTACT_EMAIL = "contacto@brandatta.com"
```

El formulario incluido valida los datos en pantalla, pero todavía no los almacena ni envía. Para producción se puede conectar con una API, base de datos, webhook, CRM o servicio de correo.

## Archivos sensibles

No subir claves ni contraseñas al repositorio. Para credenciales privadas, utilizar `.streamlit/secrets.toml` de forma local y configurar los secretos desde Streamlit Community Cloud.
