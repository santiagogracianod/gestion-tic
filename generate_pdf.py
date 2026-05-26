from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import PageBreak

# ── Color palette ──────────────────────────────────────────────────────────────
VERDE      = colors.HexColor('#3B6D11')
VERDE_L    = colors.HexColor('#EAF3DE')
VERDE_M    = colors.HexColor('#639922')
ROJO       = colors.HexColor('#993C1D')
ROJO_L     = colors.HexColor('#FAECE7')
AZUL       = colors.HexColor('#185FA5')
AZUL_L     = colors.HexColor('#E6F1FB')
AMBAR      = colors.HexColor('#854F0B')
AMBAR_L    = colors.HexColor('#FAEEDA')
GRIS_OSC   = colors.HexColor('#2C2C2A')
GRIS_MED   = colors.HexColor('#5F5E5A')
GRIS_L     = colors.HexColor('#F1EFE8')
GRIS_BRD   = colors.HexColor('#D3D1C7')
BLANCO     = colors.white
NEGRO      = colors.black

W, H = A4

# ── Document ───────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    '/home/santiago/Documents/UDEA/Gestion tic/entrega2/DOFA_CAME_NeoBankX.pdf',
    pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2.2*cm, bottomMargin=2.2*cm,
)

# ── Styles ─────────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

def S(name, **kw):
    s = ParagraphStyle(name, **kw)
    return s

cover_title = S('CoverTitle', fontSize=28, textColor=BLANCO,
                leading=34, alignment=TA_CENTER, fontName='Helvetica-Bold')
cover_sub   = S('CoverSub',   fontSize=14, textColor=colors.HexColor('#C0DD97'),
                leading=20, alignment=TA_CENTER, fontName='Helvetica')
cover_info  = S('CoverInfo',  fontSize=10, textColor=colors.HexColor('#D3D1C7'),
                leading=15, alignment=TA_CENTER, fontName='Helvetica')

sec_title   = S('SecTitle',   fontSize=15, textColor=VERDE, leading=20,
                fontName='Helvetica-Bold', spaceAfter=4)
sec_body    = S('SecBody',    fontSize=9.5, textColor=GRIS_OSC, leading=14,
                fontName='Helvetica', alignment=TA_JUSTIFY)
bold_body   = S('BoldBody',   fontSize=9.5, textColor=GRIS_OSC, leading=14,
                fontName='Helvetica-Bold')
small_gray  = S('SmallGray',  fontSize=8, textColor=GRIS_MED, leading=12,
                fontName='Helvetica')
cell_title  = S('CellTitle',  fontSize=9, textColor=BLANCO, leading=12,
                fontName='Helvetica-Bold', alignment=TA_CENTER)
cell_body   = S('CellBody',   fontSize=8.2, textColor=GRIS_OSC, leading=12,
                fontName='Helvetica')
cell_item   = S('CellItem',   fontSize=8, textColor=GRIS_OSC, leading=12,
                fontName='Helvetica', leftIndent=6)
conclusion  = S('Conclusion', fontSize=9.5, textColor=GRIS_OSC, leading=14,
                fontName='Helvetica', alignment=TA_JUSTIFY, leftIndent=10,
                borderPadding=(6,6,6,6))
label_ext   = S('LabelExt',   fontSize=8.5, textColor=GRIS_MED, leading=12,
                fontName='Helvetica-Bold', alignment=TA_CENTER)
action_num  = S('ActNum',     fontSize=16, textColor=BLANCO, leading=20,
                fontName='Helvetica-Bold', alignment=TA_CENTER)
action_ttl  = S('ActTitle',   fontSize=10, textColor=GRIS_OSC, leading=14,
                fontName='Helvetica-Bold')
action_desc = S('ActDesc',    fontSize=8.8, textColor=GRIS_MED, leading=13,
                fontName='Helvetica', alignment=TA_JUSTIFY)
kpi_s       = S('KPI',        fontSize=7.5, textColor=AZUL, leading=11,
                fontName='Helvetica-Bold')
footer_s    = S('Footer',     fontSize=7.5, textColor=GRIS_MED, leading=10,
                fontName='Helvetica', alignment=TA_CENTER)

# ── Page callbacks ─────────────────────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    # Header bar
    canvas.setFillColor(VERDE)
    canvas.rect(0, H - 1.1*cm, W, 1.1*cm, fill=1, stroke=0)
    canvas.setFillColor(BLANCO)
    canvas.setFont('Helvetica-Bold', 8)
    canvas.drawString(2*cm, H - 0.65*cm, 'NeoBankX · Análisis DOFA, Matriz CAME y Acciones Estratégicas')
    canvas.setFont('Helvetica', 8)
    canvas.drawRightString(W - 2*cm, H - 0.65*cm, 'Plan Estratégico de TI · 2026')
    # Footer
    canvas.setFillColor(GRIS_BRD)
    canvas.rect(0, 0, W, 0.8*cm, fill=1, stroke=0)
    canvas.setFillColor(GRIS_MED)
    canvas.setFont('Helvetica', 7)
    canvas.drawCentredString(W/2, 0.28*cm, f'Página {doc.page} ')
    canvas.restoreState()

def on_cover(canvas, doc):
    canvas.saveState()
    # Full green background
    canvas.setFillColor(VERDE)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    # Decorative circles
    canvas.setFillColor(colors.HexColor('#4A8A18'))
    canvas.circle(W - 3*cm, H - 3*cm, 6*cm, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor('#2D5A0E'))
    canvas.circle(3*cm, 3*cm, 4*cm, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor('#4A8A18'))
    canvas.circle(W/2, H*0.35, 0.6*cm, fill=1, stroke=0)
    # Footer strip
    canvas.setFillColor(colors.HexColor('#27500A'))
    canvas.rect(0, 0, W, 2.5*cm, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor('#C0DD97'))
    canvas.setFont('Helvetica', 8)
    canvas.drawCentredString(W/2, 0.9*cm, 'Universidad de Antioquia · Facultad de Ingeniería · 2026')
    canvas.restoreState()

# ── Helper: bullet ─────────────────────────────────────────────────────────────
def bullet(text, style=cell_item, color=VERDE_M, indent=8):
    return Paragraph(f'<font color="#{color.hexval()[2:]}" size="10">&#x2022;</font>  {text}', style)

def tag(text, bg, fg):
    return f'<font color="#{fg.hexval()[2:]}" size="7"><b> {text} </b></font>'

# ── Build story ────────────────────────────────────────────────────────────────
story = []

# ══════════════════════════════════════════════════════════════════════════════
# COVER PAGE
# ══════════════════════════════════════════════════════════════════════════════
story.append(Spacer(1, 4.5*cm))
story.append(Paragraph('NeoBankX', cover_title))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph('Segunda entrega<br/>Grupo 2 - Caso 2', cover_sub))
story.append(Spacer(1, 1.2*cm))
story.append(HRFlowable(width='60%', thickness=0.5, color=colors.HexColor('#639922'), spaceAfter=1.2*cm))
story.append(Paragraph('Plan Estratégico de Tecnologías de la Información (PETI)', cover_info))
story.append(Spacer(1, 0.4*cm))
story.append(Paragraph('Caso de Estudio · Sector Fintech · Latinoamérica', cover_info))
story.append(Spacer(1, 2*cm))
story.append(Paragraph('Integrantes', cover_sub))
story.append(Paragraph('Santiago Graciano', cover_info))
story.append(Paragraph('Ricardo Contreras', cover_info))
story.append(Paragraph('Juan Jose Jaramillo', cover_info))
story.append(Spacer(1, 2*cm))
story.append(Paragraph('Abril 2026', cover_info))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1: INTRO & CONTEXT
# ══════════════════════════════════════════════════════════════════════════════
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('1. Contexto del Análisis', sec_title))
story.append(HRFlowable(width='100%', thickness=0.5, color=VERDE_M, spaceAfter=0.3*cm))
story.append(Paragraph(
    'NeoBankX es una fintech latinoamericana que ofrece servicios financieros 100% digitales. '
    'Ante el crecimiento de los neobancos, la presión regulatoria y la necesidad de diferenciación competitiva, '
    'la organización ha iniciado una transformación digital basada en Open Banking, APIs, analítica avanzada '
    'y scoring alternativo con inteligencia artificial.',
    sec_body))
story.append(Spacer(1, 0.25*cm))
story.append(Paragraph(
    'El presente análisis DOFA se construye considerando tres dimensiones críticas identificadas en el caso: '
    '<b>(1) altos niveles de fraude digital</b>, <b>(2) baja fidelización de clientes</b> y '
    '<b>(3) dificultades de escalabilidad de la infraestructura</b>. A partir de este diagnóstico, '
    'la Matriz CAME traduce los hallazgos en estrategias concretas y las acciones estratégicas '
    'definen la hoja de ruta hacia los resultados esperados.',
    sec_body))
story.append(Spacer(1, 0.5*cm))

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2: DOFA MATRIX
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph('2. Análisis DOFA', sec_title))
story.append(HRFlowable(width='100%', thickness=0.5, color=VERDE_M, spaceAfter=0.3*cm))
story.append(Paragraph(
    'El análisis DOFA identifica factores internos (fortalezas y debilidades) y externos '
    '(oportunidades y amenazas) considerando el contexto competitivo, tecnológico y organizacional '
    'de NeoBankX.',
    sec_body))
story.append(Spacer(1, 0.35*cm))

usable_w = W - 4*cm  # 17 cm
col_w = usable_w / 2

def dofa_cell(title, bg, fg, items):
    paras = [Paragraph(title, ParagraphStyle('CH', fontSize=9, textColor=fg,
              fontName='Helvetica-Bold', leading=12, alignment=TA_CENTER))]
    paras.append(Spacer(1, 4))
    for item in items:
        paras.append(Paragraph(f'\u2022  {item}', ParagraphStyle('CI', fontSize=8,
                     textColor=GRIS_OSC, fontName='Helvetica', leading=12, leftIndent=4)))
        paras.append(Spacer(1, 2))
    return paras

header_int = Paragraph('FACTORES INTERNOS', label_ext)
header_ext = Paragraph('FACTORES EXTERNOS', label_ext)
lbl_pos    = Paragraph('POSITIVO', label_ext)
lbl_neg    = Paragraph('NEGATIVO', label_ext)

fortalezas_items = [
    'Buena base en Infraestructura TI: NeoBankX cuenta con una infraestructura basada en cloud y microservicios, lo que le permite adaptarlo a cambios en la demanda a futuro.',
    'Capacidad de analítica avanzada: La organización posee capacidades iniciales en el uso de datos e inteligencia artificial, lo que representa una base para la toma de decisiones más precisas',
    'Enfoque en experiencia digital: El modelo de negocio está orientado a canales digitales, lo que permite una interacción directa y continua con el cliente',
]
debilidades_items = [
    'Bajo nivel de madurez en gestión de fraude: Los procesos actuales no permiten una deteccion eficiente en tiempo real, generando vulnerabilidad operativa',
    'Limitada explotación de datos: La organización no utiliza plenamente su informacion para personalizar servicios y mejorar la experiencia del cliente',
    'Desalineación organizacional: Se evidencian dificultades en la adopción de nuevas tecnologías y resistencia al cambio',
    'Procesos TI no completamente optimizados: Existen oportunidades de mejora en la integracion y automatización de procesos ',
    'Dificultad para escalar infraestructura ante crecimiento de usuarios ',
]
oportunidades_items = [
    'Crecimiento del sector fintech: La expansión del sector en Latinoamérica genera oportunidades de captación de nuevos clientes',
    'Open Banking y APIs: La apertura de APIs permite la integración con terceros y la creación de nuevos modelos de negocio',
    'Avances en inteligencia artificial: Tecnologías disponibles que pueden mejorar procesos, productos, scoring alternativo y experiencia del cliente',
    'Mayor adopción digital: Incremento en la confianza y uso de servicios financieros digitales por parte de los usuarios',
]
amenazas_items = [
    'Ciberataques: El incremento de amenazas digitales representa un riesgo constante para la seguridad y continuidad de los servicios',
    'Regulación estricta: El entorno regulatorio puede limitar la innovación y aumentar costos operativos',
    'Competencia intensiva: Otras fintech y bancos digitales compiten por el mismo segmento de mercado',
    'Evolución tecnológica acelerada: Puede generar obsolescencia si no se adapta oportunamente',
    'Concentración tecnológica y dependencia de proveedores cloud',
]

dofa_data = [
    ['', Paragraph('POSITIVO', label_ext), Paragraph('NEGATIVO', label_ext)],
    [
        Paragraph('INTERNO', label_ext),
        dofa_cell('FORTALEZAS', VERDE, VERDE, fortalezas_items),
        dofa_cell('DEBILIDADES', ROJO, ROJO, debilidades_items),
    ],
    [
        Paragraph('EXTERNO', label_ext),
        dofa_cell('OPORTUNIDADES', AZUL, AZUL, oportunidades_items),
        dofa_cell('AMENAZAS', AMBAR, AMBAR, amenazas_items),
    ],
]

dofa_table = Table(dofa_data, colWidths=[1.2*cm, col_w - 0.6*cm, col_w - 0.6*cm],
                   repeatRows=1)
dofa_table.setStyle(TableStyle([
    # Header row
    ('BACKGROUND', (1,0), (1,0), VERDE_L),
    ('BACKGROUND', (2,0), (2,0), ROJO_L),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    # Fortalezas cell
    #('BACKGROUND', (1,1), (1,1), VERDE_L),
    ('TOPPADDING', (1,1), (1,1), 6),
    ('BOTTOMPADDING', (1,1), (1,1), 6),
    ('LEFTPADDING', (1,1), (1,1), 8),
    ('RIGHTPADDING', (1,1), (1,1), 6),
    # Debilidades cell
    #('BACKGROUND', (2,1), (2,1), ROJO_L),
    ('TOPPADDING', (2,1), (2,1), 6),
    ('BOTTOMPADDING', (2,1), (2,1), 6),
    ('LEFTPADDING', (2,1), (2,1), 8),
    ('RIGHTPADDING', (2,1), (2,1), 6),
    # Oportunidades cell
    #('BACKGROUND', (1,2), (1,2), AZUL_L),
    ('TOPPADDING', (1,2), (1,2), 6),
    ('BOTTOMPADDING', (1,2), (1,2), 6),
    ('LEFTPADDING', (1,2), (1,2), 8),
    ('RIGHTPADDING', (1,2), (1,2), 6),
    # Amenazas cell
    #('BACKGROUND', (2,2), (2,2), AMBAR_L),
    ('TOPPADDING', (2,2), (2,2), 6),
    ('BOTTOMPADDING', (2,2), (2,2), 6),
    ('LEFTPADDING', (2,2), (2,2), 8),
    ('RIGHTPADDING', (2,2), (2,2), 6),
    # Label column
    #('BACKGROUND', (0,1), (0,2), GRIS_L),
    ('TOPPADDING', (0,0), (0,-1), 4),
    ('BOTTOMPADDING', (0,0), (0,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('VALIGN', (0,0), (0,-1), 'MIDDLE'),
    ('VALIGN', (1,0), (-1,0), 'MIDDLE'),
    # Grid
    ('GRID', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ('ROWBACKGROUNDS', (0,0), (0,-1), [GRIS_L]),
    ('TOPPADDING', (0,0), (-1,0), 5),
    ('BOTTOMPADDING', (0,0), (-1,0), 5),
]))

story.append(dofa_table)
story.append(Spacer(1, 2*cm))

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3: CAME MATRIX
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph('3. Matriz CAME', sec_title))
story.append(HRFlowable(width='100%', thickness=0.5, color=VERDE_M, spaceAfter=0.3*cm))
story.append(Paragraph(
    'La Matriz CAME traduce el diagnóstico DOFA en estrategias concretas. Cada cuadrante responde '
    'directamente a los factores identificados, estableciendo el marco estratégico del PETI.',
    sec_body))
story.append(Spacer(1, 0.35*cm))

def came_cell(letra, palabra, relacion, color_bg, color_acc, description, acciones):
    content = []
    # Header
    content.append(Paragraph(
        f'<b>{letra}</b> — {palabra}',
        ParagraphStyle('CH2', fontSize=9.5, textColor=color_acc,
                       fontName='Helvetica-Bold', leading=13)))
    content.append(Paragraph(
        f'<i>Relación DOFA: {relacion}</i>',
        ParagraphStyle('CH3', fontSize=7.5, textColor=GRIS_MED,
                       fontName='Helvetica', leading=11)))
    content.append(Spacer(1, 5))
    content.append(Paragraph(description,
        ParagraphStyle('CD', fontSize=8.2, textColor=GRIS_OSC,
                       fontName='Helvetica', leading=12, alignment=TA_JUSTIFY)))
    content.append(Spacer(1, 5))
    for a in acciones:
        content.append(Paragraph(f'\u2022  {a}',
            ParagraphStyle('CA', fontSize=8, textColor=GRIS_OSC,
                           fontName='Helvetica', leading=12, leftIndent=4)))
        content.append(Spacer(1, 1.5))
    return content

came_data = [
    [
        came_cell('C', 'CORREGIR', 'Debilidades → Eliminar',
                  ROJO_L, ROJO,
                  'Intervención directa sobre las debilidades más críticas para reducir vulnerabilidades operativas y organizacionales:',
                  ['Implementar sistemas de detección de fraude en tiempo real con ML',
                   'Fortalecer habilidades del equipo TI en analítica y DevSecOps',
                   'Programa de gestión del cambio para superar resistencia cultural a la IA',
                   'Redefinir el rol del área de cumplimiento como habilitador de innovación']),
        came_cell('A', 'AFRONTAR', 'Amenazas → Minimizar',
                  AMBAR_L, AMBAR,
                  'Medidas defensivas para reducir la exposición a las amenazas externas identificadas en el entorno competitivo y regulatorio:',
                  ['Adoptar arquitectura de ciberseguridad integral ',
                   'Garantizar cumplimiento regulatorio proactivo y anticipado',
                   'Estrategia multi-cloud para reducir dependencia de proveedores únicos',
                   'Monitorear en entorno competitivo fintech en LATAM']),
    ],
    [
        came_cell('M', 'MANTENER', 'Fortalezas → Consolidar',
                  VERDE_L, VERDE,
                  'Preservar y madurar las capacidades diferenciales que constituyen ventajas competitivas actuales de NeoBankX:',
                  ['Consolidar la arquitectura cloud-native y de microservicios',
                   'Sostener y madurar las capacidades analíticas e IA existentes',
                   'Preservar el enfoque digital-first como modelo de negocio central']),
        came_cell('E', 'EXPLOTAR', 'Oportunidades → Aprovechar',
                  AZUL_L, AZUL,
                  'Capitalizar las oportunidades del entorno para ampliar la propuesta de valor y ganar participación en el mercado fintech latinoamericano:',
                  ['Desarrollar APIs para integración con terceros en Open Banking',
                   'Expandir servicios financieros personalizados con IA en LATAM',
                   'Innovar en la aprobación crediticia con  componentes de IA',
                   'Crear nuevos productos financieros basados en analítica predictiva']),
    ],
]

came_table = Table(came_data, colWidths=[col_w, col_w])
came_table.setStyle(TableStyle([
    #('BACKGROUND', (0,0), (0,0), ROJO_L),
    #('BACKGROUND', (1,0), (1,0), AMBAR_L),
    ('BACKGROUND', (1,0), (1,0), VERDE_L),
    ('BACKGROUND', (0,1), (0,1), VERDE_L),
    #('BACKGROUND', (1,1), (1,1), AZUL_L),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('GRID', (0,0), (-1,-1), 0.5, GRIS_BRD),
]))

story.append(came_table)
story.append(Spacer(1, 0.5*cm))

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4: STRATEGIC ACTIONS
# ══════════════════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('4. Acciones Estratégicas', sec_title))
story.append(HRFlowable(width='100%', thickness=0.5, color=VERDE_M, spaceAfter=0.3*cm))
story.append(Paragraph(
    'Las acciones estratégicas se derivan directamente del análisis DOFA y de la Matriz CAME, '
    'estableciendo iniciativas concretas, viables y alineadas con los resultados esperados por NeoBankX: '
    '<b>reducción del fraude en 35%</b>, <b>aprobación crediticia más precisa</b> y '
    '<b>nuevos productos financieros personalizados</b>.',
    sec_body))
story.append(Spacer(1, 0.35*cm))

actions = [
    {
        'num': '1', 'color': ROJO, 'bg': ROJO_L,
        'title': 'Fortalecimiento de la Seguridad Digital',
        'desc': ('Implementar un sistema de detección de fraude en tiempo real basado en machine learning, '
                 'capaz de analizar patrones transaccionales y comportamentales. Complementar con una '
                 'arquitectura de seguridad  que garantice la protección de los datos y transacciones.'),
        'meta': 'Reducción del fraude en 35%',
        'dofa': 'Corrige D1 · Afronta A1 · Mantiene F1',
    },
    {
        'num': '2', 'color': AZUL, 'bg': AZUL_L,
        'title': 'Desarrollo de Capacidades de Personalización',
        'desc': ('Implementar motores de recomendación y segmentación avanzada que adapten productos '
                 'y servicios financieros al perfil de comportamiento de cada cliente, utilizando los '
                 'datos transaccionales y de interacción digital como fuente principal.'),
        'meta': 'Nuevos productos financieros personalizados',
        'dofa': 'Corrige D2 · Explota O3, O4 · Mantiene F2',
    },
    {
        'num': '3', 'color': VERDE, 'bg': VERDE_L,
        'title': 'Implementación de Modelos Predictivos',
        'desc': ('Desarrollar o implementar modelos de analítica predictiva que permitan anticipar necesidades del cliente '
                 'y perfeccionar los motores de decisión crediticia. El scoring alternativo con IA '
                 'mejorará la precisión en aprobaciones y reducirá el riesgo de cartera.'),
        'meta': 'Aprobación crediticia más precisa',
        'dofa': 'Explota O3 · Mantiene F4 · Corrige D2',
    },
    {
        'num': '4', 'color': AMBAR, 'bg': AMBAR_L,
        'title': 'Escalabilidad Tecnológica e Infraestructura',
        'desc': ('Fortalecer y escalar la infraestructura cloud-native y de microservicios para garantizar '
                 'alta disponibilidad, resiliencia y capacidad de respuesta ante el crecimiento acelerado '
                 'de usuarios. Implementar estrategia multi-cloud para evitar dependencia de proveedor único.'),
        'meta': 'Soporte al crecimiento de usuarios',
        'dofa': 'Corrige D6 · Mantiene F1 · Afronta A5',
    },
    {
        'num': '5', 'color': AZUL, 'bg': AZUL_L,
        'title': 'Integración con Ecosistemas Digitales (Open Banking)',
        'desc': ('Desarrollar e implementar APIs abiertas que faciliten la integración con terceros '
                 'en el marco del Open Banking. Crear nuevos modelos de negocio colaborativos que '
                 'amplíen la oferta de productos financieros personalizados y el alcance al mercado LATAM.'),
        'meta': 'Nuevos productos financieros personalizados',
        'dofa': 'Explota O2, O1 · Mantiene F3',
    },
    {
        'num': '6', 'color': VERDE, 'bg': VERDE_L,
        'title': 'Transformación Organizacional y Gestión del Cambio',
        'desc': ('Ejecutar un programa de gestión del cambio que aborde los conflictos entre equipos '
                 'tradicionales de riesgo y científicos de datos. Redefinir el rol del área de cumplimiento '
                 'como habilitador de innovación. Adoptar prácticas DevSecOps y fortalecer la cultura '
                 'organizacional orientada a datos, superando la resistencia e inseguridad frente a la IA.'),
        'meta': 'Habilitador transversal de todas las acciones',
        'dofa': 'Corrige D3, D5 · Afronta cambio cultural',
    },
]

for i, ac in enumerate(actions):
    num_para   = Paragraph(ac['num'],
        ParagraphStyle('AN', fontSize=16, textColor=BLANCO,
                       fontName='Helvetica-Bold', alignment=TA_CENTER, leading=20))
    title_para = Paragraph(ac['title'],
        ParagraphStyle('AT', fontSize=10, textColor=GRIS_OSC,
                       fontName='Helvetica-Bold', leading=14))
    desc_para  = Paragraph(ac['desc'],
        ParagraphStyle('AD', fontSize=8.5, textColor=GRIS_MED,
                       fontName='Helvetica', leading=13, alignment=TA_JUSTIFY))
    meta_para  = Paragraph(f'<b>Meta:</b> {ac["meta"]}',
        ParagraphStyle('AM', fontSize=8, textColor=AZUL,
                       fontName='Helvetica', leading=12))
    #dofa_para  = Paragraph(f'<b>DOFA:</b> {ac["dofa"]}',
     #   ParagraphStyle('ADO', fontSize=7.5, textColor=GRIS_MED,
      #                 fontName='Helvetica', leading=11))

    row = Table(
        [[num_para, [title_para, Spacer(1,4), desc_para, Spacer(1,5), meta_para, Spacer(1,2)]]],
        colWidths=[1.1*cm, usable_w - 1.1*cm]
    )
    row.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), ac['color']),
        ('BACKGROUND', (1,0), (1,0), ac['bg']),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (0,0), 4),
        ('RIGHTPADDING', (0,0), (0,0), 4),
        ('LEFTPADDING', (1,0), (1,0), 10),
        ('RIGHTPADDING', (1,0), (1,0), 10),
        ('ROUNDEDCORNERS', [6,6,6,6]),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
        ('VALIGN', (0,0), (0,0), 'MIDDLE'),
    ]))
    story.append(KeepTogether([row, Spacer(1, 0.2*cm)]))

story.append(Spacer(1, 0.3*cm))

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5: CONCLUSIONS
# ══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph('5. Conclusión', sec_title))
story.append(HRFlowable(width='100%', thickness=0.5, color=VERDE_M, spaceAfter=0.3*cm))

conclusiones = [
    ('Diagnóstico integral y contextualizado',
     'El análisis DOFA permitió identificar de manera integral los principales retos y oportunidades de NeoBankX, considerando la madurez tecnológica, los procesos de TI y el entorno competitivo. A partir de este diagnóstico, la matriz CAME traduce estos hallazgos en estrategias concretas, mientras que las acciones definidas establecen una hoja de ruta para fortalecer la seguridad, mejorar la personalización y avanzar hacia un modelo predictivo.'),
    
]

for title_c, body_c in conclusiones:
    box = Table([[
        Paragraph(title_c,
            ParagraphStyle('CT', fontSize=9, textColor=VERDE,
                           fontName='Helvetica-Bold', leading=13)),
        Paragraph(body_c,
            ParagraphStyle('CB', fontSize=8.5, textColor=GRIS_OSC,
                           fontName='Helvetica', leading=13, alignment=TA_JUSTIFY)),
    ]], colWidths=[3.5*cm, usable_w - 3.5*cm])
    box.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (0,0), 10),
        ('LEFTPADDING', (1,0), (1,0), 12),
        ('RIGHTPADDING', (1,0), (1,0), 10),
        ('BACKGROUND', (0,0), (0,0), VERDE_L),
        ('BACKGROUND', (1,0), (1,0), GRIS_L),
        ('LINEAFTER', (0,0), (0,-1), 2, VERDE_M),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ]))
    story.append(KeepTogether([box, Spacer(1, 0.2*cm)]))

story.append(Spacer(1, 0.4*cm))

# ── References ─────────────────────────────────────────────────────────────────
'''story.append(Paragraph('Referencias Bibliográficas', sec_title))
story.append(HRFlowable(width='100%', thickness=0.5, color=VERDE_M, spaceAfter=0.2*cm))
refs = [
   # 'Porter, M. E., &amp; Heppelmann, J. E. (2015). How smart, connected products are transforming companies. <i>Harvard Business Review, 93</i>(10), 96–114.',
    #'McKinsey &amp; Company. (2021). <i>Global banking annual review 2021: The great divergence</i>. McKinsey &amp; Company.',
    #'Chapman, J. (2022). <i>Zero Trust Security: An Enterprise Guide</i>. Apress.',
]
for r in refs:
    story.append(Paragraph(r,
        ParagraphStyle('REF', fontSize=8, textColor=GRIS_MED,
                       fontName='Helvetica', leading=13, leftIndent=10,
                       firstLineIndent=-10, spaceAfter=4)))
'''
# ── Build PDF ──────────────────────────────────────────────────────────────────
def on_first_page(canvas, doc):
    on_cover(canvas, doc)

def on_later_pages(canvas, doc):
    on_page(canvas, doc)

doc.build(story,
          onFirstPage=on_first_page,
          onLaterPages=on_later_pages)

print('PDF generado exitosamente.')
