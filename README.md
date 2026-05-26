# Generador de PDF — DOFA / CAME NeoBankX

Script en Python que genera el documento `DOFA_CAME_NeoBankX.pdf` usando la librería `reportlab`.

---

## Requisitos previos

- Python 3.10 o superior
- pip

---

## Paso a paso

### 1. Abrir una terminal en la carpeta del proyecto

```bash
cd "/home/santiago/Documents/UDEA/Gestion tic"
```

### 2. Crear el entorno virtual (solo la primera vez)

```bash
python3 -m venv venv
```

### 3. Activar el entorno virtual

```bash
source venv/bin/activate
```

> En Windows sería: `venv\Scripts\activate`

### 4. Instalar la dependencia (solo la primera vez)

```bash
pip install reportlab
```

### 5. Ejecutar el script

```bash
python entrega2/generate_pdf.py
```

Si todo va bien verás:

```
PDF generado exitosamente.
```

### 6. Abrir el PDF generado

```bash
xdg-open entrega2/DOFA_CAME_NeoBankX.pdf
```

El archivo queda guardado en:

```
entrega2/DOFA_CAME_NeoBankX.pdf
```

---

## Estructura del proyecto

```
Gestion tic/
├── venv/                        # Entorno virtual (no subir a git)
└── entrega2/
    ├── generate_pdf.py          # Script principal
    ├── DOFA_CAME_NeoBankX.pdf   # PDF generado
    └── README.md                # Este archivo
```

---

## Notas

- Cada vez que abras una nueva terminal debes activar el entorno virtual con `source venv/bin/activate` antes de ejecutar el script.
- Si modificas el script y vuelves a ejecutarlo, el PDF se sobreescribe automáticamente.
