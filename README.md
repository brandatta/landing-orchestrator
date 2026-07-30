# Brandatta Orchestrator — Landing Streamlit

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
streamlit run app.py
```

## Personalización

En `app.py` puede modificar:

- `CONTACT_EMAIL`
- textos y llamadas a la acción
- colores en el bloque CSS
- sistemas soportados
- casos de uso
- conexión del formulario con una API, CRM, webhook o base de datos
