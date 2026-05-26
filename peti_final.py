from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

# ── Paleta de colores ─────────────────────────────────────────────────────────
VERDE      = colors.HexColor('#3B6D11')
VERDE_L    = colors.HexColor('#EAF3DE')
VERDE_M    = colors.HexColor('#639922')
ROJO       = colors.HexColor('#993C1D')
ROJO_L     = colors.HexColor('#FAECE7')
AZUL       = colors.HexColor('#185FA5')
AZUL_L     = colors.HexColor('#E6F1FB')
AMBAR      = colors.HexColor('#854F0B')
AMBAR_L    = colors.HexColor('#FAEEDA')
MORADO     = colors.HexColor('#5B2D8E')
MORADO_L   = colors.HexColor('#F0E8F8')
GRIS_OSC   = colors.HexColor('#2C2C2A')
GRIS_MED   = colors.HexColor('#5F5E5A')
GRIS_L     = colors.HexColor('#F1EFE8')
GRIS_BRD   = colors.HexColor('#D3D1C7')
BLANCO     = colors.white

W, H = A4
OUTPUT = '/home/santiago/Documents/UDEA/Gestion tic/entrega2/PETI_Final_NeoBankX.pdf'

# ── Documento ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2.2*cm, bottomMargin=2.2*cm,
)

# ── Estilos ───────────────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

cover_title = S('CoverTitle', fontSize=30, textColor=BLANCO,
                leading=36, alignment=TA_CENTER, fontName='Helvetica-Bold')
cover_sub   = S('CoverSub',   fontSize=13, textColor=colors.HexColor('#C0DD97'),
                leading=18, alignment=TA_CENTER, fontName='Helvetica')
cover_info  = S('CoverInfo',  fontSize=10, textColor=colors.HexColor('#D3D1C7'),
                leading=15, alignment=TA_CENTER, fontName='Helvetica')
sec_title   = S('SecTitle',   fontSize=14, textColor=VERDE, leading=18,
                fontName='Helvetica-Bold', spaceAfter=4)
sub_title   = S('SubTitle',   fontSize=11, textColor=AZUL, leading=15,
                fontName='Helvetica-Bold', spaceAfter=3, spaceBefore=6)
sec_body    = S('SecBody',    fontSize=9.5, textColor=GRIS_OSC, leading=14,
                fontName='Helvetica', alignment=TA_JUSTIFY)
bold_body   = S('BoldBody',   fontSize=9.5, textColor=GRIS_OSC, leading=14,
                fontName='Helvetica-Bold')
small_gray  = S('SmallGray',  fontSize=8, textColor=GRIS_MED, leading=12,
                fontName='Helvetica')
cell_body   = S('CellBody',   fontSize=8.5, textColor=GRIS_OSC, leading=12,
                fontName='Helvetica')
cell_item   = S('CellItem',   fontSize=8, textColor=GRIS_OSC, leading=12,
                fontName='Helvetica', leftIndent=6)
label_ext   = S('LabelExt',   fontSize=8.5, textColor=GRIS_MED, leading=12,
                fontName='Helvetica-Bold', alignment=TA_CENTER)
toc_item    = S('TocItem',    fontSize=10, textColor=GRIS_OSC, leading=16,
                fontName='Helvetica')
toc_num     = S('TocNum',     fontSize=10, textColor=VERDE, leading=16,
                fontName='Helvetica-Bold')

usable_w = W - 4*cm  # 17 cm

# ── Callbacks de página ───────────────────────────────────────────────────────
def on_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(VERDE)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor('#4A8A18'))
    canvas.circle(W - 3*cm, H - 3*cm, 6*cm, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor('#2D5A0E'))
    canvas.circle(3*cm, 3*cm, 4*cm, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor('#27500A'))
    canvas.rect(0, 0, W, 2.5*cm, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor('#C0DD97'))
    canvas.setFont('Helvetica', 8)
    canvas.drawCentredString(W/2, 0.9*cm, 'Universidad de Antioquia · Facultad de Ingeniería · 2026')
    canvas.restoreState()

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(VERDE)
    canvas.rect(0, H - 1.1*cm, W, 1.1*cm, fill=1, stroke=0)
    canvas.setFillColor(BLANCO)
    canvas.setFont('Helvetica-Bold', 8)
    canvas.drawString(2*cm, H - 0.65*cm, 'NeoBankX · Plan Estratégico de Tecnologías de la Información (PETI)')
    canvas.setFont('Helvetica', 8)
    canvas.drawRightString(W - 2*cm, H - 0.65*cm, 'Entrega Final · 2026')
    canvas.setFillColor(GRIS_BRD)
    canvas.rect(0, 0, W, 0.8*cm, fill=1, stroke=0)
    canvas.setFillColor(GRIS_MED)
    canvas.setFont('Helvetica', 7)
    canvas.drawCentredString(W/2, 0.28*cm, f'Página {doc.page}')
    canvas.restoreState()

# ── Helpers ───────────────────────────────────────────────────────────────────
def bullet(text, color=VERDE_M, size=10, indent=6):
    return Paragraph(
        f'<font color="#{color.hexval()[2:]}" size="{size}">&#x2022;</font>  {text}',
        cell_item)

def section_header(story, number, title):
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(f'{number}. {title}', sec_title))
    story.append(HRFlowable(width='100%', thickness=0.5, color=VERDE_M, spaceAfter=0.3*cm))

def info_box(left_label, left_content, right_content, left_color=VERDE_L, right_color=GRIS_L):
    t = Table([[
        Paragraph(left_label, S('LH', fontSize=9, textColor=VERDE,
                                fontName='Helvetica-Bold', leading=13)),
        Paragraph(right_content, sec_body),
    ]], colWidths=[3.5*cm, usable_w - 3.5*cm])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (0,0), 10),
        ('LEFTPADDING', (1,0), (1,0), 12),
        ('RIGHTPADDING', (1,0), (1,0), 10),
        ('BACKGROUND', (0,0), (0,0), left_color),
        ('BACKGROUND', (1,0), (1,0), right_color),
        ('LINEAFTER', (0,0), (0,-1), 2, VERDE_M),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ]))
    return t

def colored_row(items_data, col_widths, bg_colors, text_colors=None):
    """Helper para filas de tabla con colores por celda"""
    pass

# ══════════════════════════════════════════════════════════════════════════════
story = []

# ─── PORTADA ─────────────────────────────────────────────────────────────────
story.append(Spacer(1, 3.5*cm))
story.append(Paragraph('NeoBankX', cover_title))
story.append(Spacer(1, 0.4*cm))
story.append(Paragraph('Entrega Final · Grupo 2 - Caso 2', cover_sub))
story.append(Spacer(1, 1.0*cm))
story.append(HRFlowable(width='60%', thickness=0.5,
                         color=colors.HexColor('#639922'), spaceAfter=1.0*cm))
story.append(Paragraph('Plan Estratégico de Tecnologías de la Información (PETI)', cover_info))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Caso de Estudio · Sector Fintech · Latinoamérica', cover_info))
story.append(Spacer(1, 2.0*cm))
story.append(Paragraph('Integrantes', cover_sub))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('Santiago Graciano David', cover_info))
story.append(Paragraph('Ricardo Contreras Garzón', cover_info))
story.append(Paragraph('Juan José Jaramillo', cover_info))
story.append(Spacer(1, 1.5*cm))
story.append(Paragraph('Mayo 2026', cover_info))
story.append(PageBreak())

# ─── TABLA DE CONTENIDO ──────────────────────────────────────────────────────
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('Tabla de Contenido', sec_title))
story.append(HRFlowable(width='100%', thickness=0.5, color=VERDE_M, spaceAfter=0.4*cm))

toc_entries = [
    ('1.', 'Resumen Ejecutivo'),
    ('2.', 'Direccionamiento Estratégico'),
    ('   2.1', 'Misión, Visión y Objetivos Estratégicos'),
    ('3.', 'Cadena de Valor y Stack Tecnológico'),
    ('   3.1', 'Cadena de Valor Típica del Sector'),
    ('   3.2', 'Cadena de Valor Optimizada con TI'),
    ('   3.3', 'Capacidades Digitales y Stack Tecnológico'),
    ('4.', 'Diagnóstico Estratégico (DOFA + CAME)'),
    ('5.', 'OKRs y Acciones Estratégicas de TI'),
    ('6.', 'Modelo de Operación de TI'),
    ('7.', 'Estructura Organizacional de TI'),
    ('8.', 'Estimaciones del PETI (Tiempos, Recursos, Costos)'),
    ('9.', 'Marcos de Referencia Aplicados'),
    ('   9.1', 'DM-Book (DAMA DMBOK) — Marco Principal'),
    ('   9.2', 'COBIT 2019 — Marco Complementario'),
    ('   9.3', 'Justificación: Estructura, Procesos y Personas'),
    ('10.', 'Conclusiones y Recomendaciones'),
]
for num, name in toc_entries:
    is_main = not num.startswith('   ')
    row = Table([[
        Paragraph(num, S('TN', fontSize=10 if is_main else 9,
                          textColor=VERDE if is_main else GRIS_MED,
                          fontName='Helvetica-Bold', leading=16)),
        Paragraph(name, S('TT', fontSize=10 if is_main else 9,
                           textColor=GRIS_OSC if is_main else GRIS_MED,
                           fontName='Helvetica-Bold' if is_main else 'Helvetica',
                           leading=16)),
    ]], colWidths=[1.2*cm, usable_w - 1.2*cm])
    row.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3 if is_main else 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3 if is_main else 1),
        ('LEFTPADDING', (1,0), (1,0), 6 if is_main else 18),
        ('BACKGROUND', (0,0), (-1,-1), VERDE_L if is_main else BLANCO),
        ('LINEBELOW', (0,0), (-1,0), 0.3, GRIS_BRD),
    ]))
    story.append(row)

story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 1: RESUMEN EJECUTIVO
# ══════════════════════════════════════════════════════════════════════════════
section_header(story, '1', 'Resumen Ejecutivo')

resumen_box = Table([[
    Paragraph(
        'El presente documento constituye la <b>Entrega Final del Plan Estratégico de Tecnologías de la '
        'Información (PETI)</b> para NeoBankX, una fintech latinoamericana que opera servicios financieros '
        '100% digitales. Este PETI consolida el trabajo desarrollado durante el semestre, '
        'integrando el direccionamiento estratégico, el diagnóstico situacional, la planificación táctica '
        'y la hoja de ruta de implementación.',
        sec_body),
]], colWidths=[usable_w])
resumen_box.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), AZUL_L),
    ('TOPPADDING', (0,0), (-1,-1), 12),
    ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ('BOX', (0,0), (-1,-1), 1, AZUL),
]))
story.append(resumen_box)
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph(
    'NeoBankX enfrenta tres problemas críticos: <b>altos niveles de fraude digital</b>, '
    '<b>baja fidelización de clientes</b> y <b>dificultades para escalar su infraestructura</b>. '
    'Adicionalmente, afronta retos organizacionales profundos: conflictos entre equipos '
    'tradicionales de riesgo y científicos de datos, adopción de DevSecOps, redefinición del '
    'cumplimiento regulatorio y resistencia a la IA.',
    sec_body))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(
    'Este PETI establece la hoja de ruta estratégica para los próximos 36 meses, articulando '
    'el modelo de operación de TI, la estructura organizacional propuesta, los marcos de referencia '
    'aplicados —liderados por el <b>DM-Book (DAMA DMBOK)</b> como marco principal y complementado '
    'por <b>COBIT 2019</b>— y las estimaciones de inversión necesarias para alcanzar los '
    'resultados esperados.',
    sec_body))
story.append(Spacer(1, 0.35*cm))

# Métricas clave
metricas = [
    ('35%', 'Reducción\ndel Fraude'),
    ('99.9%', 'Disponibilidad\nde Servicios'),
    ('25%', 'Incremento\ndel NPS'),
    ('3x', 'Escalabilidad\nde Usuarios'),
]
met_data = [[
    Table([[
        Paragraph(v, S('MV', fontSize=18, textColor=AZUL, fontName='Helvetica-Bold',
                        alignment=TA_CENTER, leading=22)),
        Paragraph(l, S('ML', fontSize=7.5, textColor=GRIS_MED, fontName='Helvetica',
                         alignment=TA_CENTER, leading=10)),
    ]], colWidths=[usable_w/4 - 0.3*cm])
    for v, l in metricas
]]
met_table = Table([met_data[0]], colWidths=[usable_w/4]*4)
met_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), VERDE_L),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ('INNERGRID', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(met_table)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 2: DIRECCIONAMIENTO ESTRATÉGICO
# ══════════════════════════════════════════════════════════════════════════════
section_header(story, '2', 'Direccionamiento Estratégico')

story.append(Paragraph(
    'El direccionamiento estratégico establece la identidad corporativa y los propósitos '
    'organizacionales que orientan toda la planificación de TI. Para NeoBankX, estos elementos '
    'fueron diseñados a partir del análisis del sector fintech latinoamericano y los referentes '
    'del mercado como Nubank y PayPal.',
    sec_body))
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph('2.1 Misión, Visión y Objetivos Estratégicos', sub_title))
story.append(Spacer(1, 0.2*cm))

mv_items = [
    ('Misión', VERDE, VERDE_L,
     'Brindar servicios y experiencias financieras digitales simples, seguras y personalizadas '
     'que respondan a las necesidades de cada cliente, respaldados por tecnología de vanguardia, '
     'con foco en el relacionamiento a largo plazo.'),
    ('Visión', AZUL, AZUL_L,
     'Consolidarnos como la institución financiera digital de mayor confianza en Latinoamérica, '
     'distinguida por la solidez de su seguridad, la precisión de sus decisiones y la capacidad '
     'de anticiparse a las necesidades financieras de sus clientes antes de que ellos mismos '
     'las expresen.'),
]
for label, col, bg, texto in mv_items:
    t = Table([[
        Paragraph(label, S('MVL', fontSize=10, textColor=col, fontName='Helvetica-Bold',
                            leading=14, alignment=TA_CENTER)),
        Paragraph(texto, sec_body),
    ]], colWidths=[2.2*cm, usable_w - 2.2*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), bg),
        ('BACKGROUND', (1,0), (1,0), GRIS_L),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (0,0), 6),
        ('LEFTPADDING', (1,0), (1,0), 12),
        ('RIGHTPADDING', (1,0), (1,0), 10),
        ('LINEAFTER', (0,0), (0,-1), 2, col),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ]))
    story.append(KeepTogether([t, Spacer(1, 0.2*cm)]))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('<b>Objetivos Estratégicos Generales</b>', bold_body))
story.append(Spacer(1, 0.2*cm))

objetivos = [
    ('OE1', VERDE,
     'Fortalecer la confianza y el relacionamiento a largo plazo con los clientes de NeoBankX, '
     'mediante la implementación de servicios financieros personalizados sustentados en analítica '
     'avanzada, orientados a incrementar la fidelización, reducir la tasa de abandono y '
     'disminuir el fraude digital en un 35%. <i>(Alineado a la Misión)</i>'),
    ('OE2', AZUL,
     'Posicionar a NeoBankX como referente de seguridad y confianza en la industria financiera '
     'digital latinoamericana, a través de arquitecturas robustas, cumplimiento regulatorio '
     'riguroso y procesos de decisión transparentes que protejan el patrimonio y la privacidad '
     'de cada cliente. <i>(Alineado a la Visión)</i>'),
]
for num, col, texto in objetivos:
    t = Table([[
        Paragraph(num, S('ON', fontSize=9, textColor=BLANCO, fontName='Helvetica-Bold',
                          alignment=TA_CENTER, leading=13)),
        Paragraph(texto, sec_body),
    ]], colWidths=[1.2*cm, usable_w - 1.2*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), col),
        ('BACKGROUND', (1,0), (1,0), GRIS_L),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('VALIGN', (0,0), (0,0), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (1,0), (1,0), 12),
        ('RIGHTPADDING', (1,0), (1,0), 10),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ]))
    story.append(KeepTogether([t, Spacer(1, 0.2*cm)]))

story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 3: CADENA DE VALOR + STACK TECNOLÓGICO
# ══════════════════════════════════════════════════════════════════════════════
section_header(story, '3', 'Cadena de Valor y Stack Tecnológico')

story.append(Paragraph('3.1 Cadena de Valor Típica del Sector Fintech', sub_title))
story.append(Paragraph(
    'La cadena de valor del sector fintech se organiza alrededor de actividades primarias que '
    'generan valor directo al cliente y actividades de soporte que habilitan la operación. '
    'Para NeoBankX, estas actividades han sido identificadas y posteriormente optimizadas con TI.',
    sec_body))
story.append(Spacer(1, 0.3*cm))

act_prim = [
    'Investigación de mercado y conocimiento del consumidor',
    'Desarrollo e innovación de productos financieros',
    'Desarrollo y mantenimiento de la plataforma digital',
    'Gestión de transacciones en tiempo real',
    'Soporte y servicios al cliente omnicanal',
    'Gestión de riesgos y cumplimiento normativo',
    'Seguridad de datos y prevención del fraude',
    'Evaluación crediticia y scoring',
    'Retención y fidelización de clientes',
]
act_soporte = [
    'Tecnologías de la Información (TI)',
    'Gestión de Recursos Humanos',
    'Gestión financiera',
    'Cumplimiento legal y normativo',
    'Análisis de datos e inteligencia empresarial',
    'Gestión de la ciberseguridad',
    'Imagen de marca y relaciones públicas',
]

prim_col = [bullet(a, VERDE_M) for a in act_prim]
sop_col  = [bullet(a, AZUL)    for a in act_soporte]

cv_table = Table([[
    [Paragraph('Actividades Primarias', S('CVH', fontSize=9, textColor=VERDE,
                fontName='Helvetica-Bold', leading=13)),
     Spacer(1, 4)] + prim_col,
    [Paragraph('Actividades de Soporte', S('CVH', fontSize=9, textColor=AZUL,
                fontName='Helvetica-Bold', leading=13)),
     Spacer(1, 4)] + sop_col,
]], colWidths=[usable_w/2 - 0.1*cm, usable_w/2 - 0.1*cm])
cv_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('BACKGROUND', (0,0), (0,0), VERDE_L),
    ('BACKGROUND', (1,0), (1,0), AZUL_L),
    ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ('INNERGRID', (0,0), (-1,-1), 0.5, GRIS_BRD),
]))
story.append(cv_table)
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph('3.2 Cadena de Valor Optimizada con TI', sub_title))
story.append(Paragraph(
    'La optimización de la cadena de valor mediante TI transforma cada actividad en una '
    'fuente de ventaja competitiva digital para NeoBankX:', sec_body))
story.append(Spacer(1, 0.25*cm))

opt_data = [
    ['Actividad', 'Transformación con TI', 'Valor Estratégico'],
    ['Adquisición de clientes', 'Analítica avanzada para segmentación\ny marketing personalizado', 'Clientes con mayor afinidad\ny potencial de fidelización'],
    ['Onboarding digital', 'Automatizado, biométrico y seguro\ncon KYC digital', 'Reducción de fraude en apertura\ny mejor experiencia'],
    ['Evaluación crediticia', 'Scoring alternativo con ML\ne IA sobre datos no tradicionales', 'Decisiones más precisas,\nrápidas e inclusivas'],
    ['Procesamiento transaccional', 'Tiempo real, microservicios,\nAPI-first y event-driven', 'Alta escalabilidad\ny resiliencia'],
    ['Gestión de riesgos/fraude', 'Detección en tiempo real\ncon modelos ML supervisados', 'Prevención proactiva\n(-35% fraude)'],
    ['Atención al cliente', 'Experiencia omnicanal,\nchatbots con IA y app móvil', 'Mejora NPS y reducción\ncostos de atención'],
    ['Fidelización', 'Personalización continua\ny motores de recomendación', 'Incremento retención\ny cross-selling'],
]

opt_col_w = [usable_w*0.28, usable_w*0.38, usable_w*0.34]
opt_style = S('OT', fontSize=8.2, textColor=GRIS_OSC, fontName='Helvetica', leading=12)
opt_rows = []
for i, row in enumerate(opt_data):
    if i == 0:
        opt_rows.append([Paragraph(c, S('OH', fontSize=8.5, textColor=BLANCO,
                         fontName='Helvetica-Bold', leading=12, alignment=TA_CENTER))
                         for c in row])
    else:
        opt_rows.append([Paragraph(c, opt_style) for c in row])

opt_table = Table(opt_rows, colWidths=opt_col_w)
opt_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), VERDE),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [BLANCO, GRIS_L]),
    ('GRID', (0,0), (-1,-1), 0.4, GRIS_BRD),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),
]))
story.append(opt_table)
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph('3.3 Capacidades Digitales y Stack Tecnológico', sub_title))

cap_data = [
    ['Capa', 'Tecnologías / Herramientas', 'Propósito en NeoBankX'],
    ['Infraestructura\nCloud', 'AWS / GCP · Kubernetes · Terraform\nDocker · Multi-cloud strategy', 'Escalabilidad, resiliencia\ny alta disponibilidad (99.9%)'],
    ['Backend /\nMicroservicios', 'Python · Node.js · Go\nKafka · REST & GraphQL APIs', 'Procesamiento transaccional\nen tiempo real'],
    ['IA & ML', 'TensorFlow · scikit-learn · MLflow\nDatabricks · Feature Store', 'Fraude, scoring crediticio\ny personalización'],
    ['Data Platform', 'Snowflake · Apache Spark · dbt\nAirflow · Delta Lake', 'Gobierno del dato (DM-Book)\ny analítica avanzada'],
    ['Seguridad', 'Zero Trust · SIEM · Vault\nOAuth2/OIDC · WAF', 'Ciberseguridad y cumplimiento\nPCI-DSS / regulatorio'],
    ['Open Banking\n& APIs', 'Kong API Gateway · OpenAPI 3.0\nOAuth2 · Webhooks', 'Integración con terceros\ny ecosistema fintech'],
    ['CI/CD /\nDevSecOps', 'GitHub Actions · SonarQube\nTerraform · OWASP DAST', 'Entrega continua\ny calidad de código'],
    ['Frontend /\nCanales', 'React Native · Flutter\nFirebase · CDN', 'App móvil y web\ncon UX de alto NPS'],
]

cap_col_w = [usable_w*0.18, usable_w*0.44, usable_w*0.38]
cap_rows = []
for i, row in enumerate(cap_data):
    if i == 0:
        cap_rows.append([Paragraph(c, S('CH', fontSize=8.5, textColor=BLANCO,
                         fontName='Helvetica-Bold', leading=12, alignment=TA_CENTER))
                         for c in row])
    else:
        cap_rows.append([Paragraph(c, S('CD', fontSize=8, textColor=GRIS_OSC,
                         fontName='Helvetica', leading=12)) for c in row])

cap_table = Table(cap_rows, colWidths=cap_col_w)
cap_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), AZUL),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [BLANCO, AZUL_L]),
    ('GRID', (0,0), (-1,-1), 0.4, GRIS_BRD),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),
]))
story.append(cap_table)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 4: DOFA + CAME
# ══════════════════════════════════════════════════════════════════════════════
section_header(story, '4', 'Diagnóstico Estratégico — DOFA y Matriz CAME')

story.append(Paragraph(
    'El análisis DOFA identifica los factores internos y externos que condicionan la capacidad '
    'de NeoBankX para ejecutar su transformación digital. La Matriz CAME traduce este diagnóstico '
    'en estrategias accionables.', sec_body))
story.append(Spacer(1, 0.3*cm))

col_w = usable_w / 2

def dofa_cell(title, color, items):
    content = [
        Paragraph(title, S('DCH', fontSize=9, textColor=color,
                            fontName='Helvetica-Bold', leading=12, alignment=TA_CENTER)),
        Spacer(1, 4),
    ]
    for item in items:
        content.append(Paragraph(f'\u2022  {item}',
            S('DCI', fontSize=7.8, textColor=GRIS_OSC, fontName='Helvetica', leading=11, leftIndent=4)))
        content.append(Spacer(1, 2))
    return content

fortalezas = [
    'Infraestructura cloud-native y microservicios adaptable a la demanda',
    'Capacidades iniciales de analítica avanzada e inteligencia artificial',
    'Modelo de negocio digital-first con interacción continua con el cliente',
]
debilidades = [
    'Bajo nivel de madurez en gestión de fraude en tiempo real',
    'Limitada explotación de datos para personalización de servicios',
    'Desalineación organizacional y resistencia al cambio tecnológico',
    'Procesos TI no completamente integrados ni automatizados',
    'Dificultad para escalar infraestructura ante crecimiento de usuarios',
]
oportunidades = [
    'Expansión del sector fintech en Latinoamérica y nuevos segmentos',
    'Open Banking y APIs: integración con terceros y nuevos modelos de negocio',
    'Avances en IA disponibles para mejorar scoring, fraude y personalización',
    'Mayor adopción y confianza del usuario en servicios financieros digitales',
]
amenazas = [
    'Incremento de ciberataques y amenazas digitales sofisticadas',
    'Regulación estricta que puede limitar la innovación y elevar costos',
    'Competencia intensiva de otras fintech y bancos digitales en LATAM',
    'Evolución tecnológica acelerada que puede generar obsolescencia',
    'Concentración tecnológica y dependencia de proveedores cloud únicos',
]

dofa_data = [
    ['', Paragraph('POSITIVO', label_ext), Paragraph('NEGATIVO', label_ext)],
    [Paragraph('INTERNO', label_ext), dofa_cell('FORTALEZAS', VERDE, fortalezas),
     dofa_cell('DEBILIDADES', ROJO, debilidades)],
    [Paragraph('EXTERNO', label_ext), dofa_cell('OPORTUNIDADES', AZUL, oportunidades),
     dofa_cell('AMENAZAS', AMBAR, amenazas)],
]
dofa_table = Table(dofa_data, colWidths=[1.2*cm, col_w - 0.6*cm, col_w - 0.6*cm])
dofa_table.setStyle(TableStyle([
    ('BACKGROUND', (1,0), (1,0), VERDE_L),
    ('BACKGROUND', (2,0), (2,0), ROJO_L),
    ('ROWBACKGROUNDS', (0,1), (0,2), [GRIS_L]),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('VALIGN', (0,0), (0,-1), 'MIDDLE'),
    ('VALIGN', (1,0), (-1,0), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (1,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('GRID', (0,0), (-1,-1), 0.5, GRIS_BRD),
]))
story.append(dofa_table)
story.append(Spacer(1, 0.5*cm))

story.append(Paragraph('Matriz CAME — Estrategias Derivadas', sub_title))

def came_cell(letra, palabra, relacion, color_acc, description, acciones):
    content = [
        Paragraph(f'<b>{letra}</b> — {palabra}',
            S('CCH', fontSize=9.5, textColor=color_acc, fontName='Helvetica-Bold', leading=13)),
        Paragraph(f'<i>Relación: {relacion}</i>',
            S('CCR', fontSize=7.5, textColor=GRIS_MED, fontName='Helvetica', leading=11)),
        Spacer(1, 5),
        Paragraph(description, S('CCD', fontSize=8.2, textColor=GRIS_OSC,
                                  fontName='Helvetica', leading=12, alignment=TA_JUSTIFY)),
        Spacer(1, 5),
    ]
    for a in acciones:
        content.append(Paragraph(f'\u2022  {a}',
            S('CCA', fontSize=7.8, textColor=GRIS_OSC, fontName='Helvetica',
               leading=12, leftIndent=4)))
        content.append(Spacer(1, 2))
    return content

came_data = [
    [
        came_cell('C', 'CORREGIR', 'Debilidades → Eliminar', ROJO,
                  'Intervención directa sobre las debilidades críticas:',
                  ['Implementar sistemas de detección de fraude en tiempo real con ML',
                   'Fortalecer equipo TI en analítica avanzada y DevSecOps',
                   'Programa de gestión del cambio y cultura data-driven',
                   'Redefinir el cumplimiento como habilitador de innovación']),
        came_cell('A', 'AFRONTAR', 'Amenazas → Minimizar', AMBAR,
                  'Medidas defensivas frente al entorno competitivo y regulatorio:',
                  ['Adoptar arquitectura de ciberseguridad Zero Trust integral',
                   'Garantizar cumplimiento regulatorio proactivo y anticipado',
                   'Estrategia multi-cloud para reducir dependencia de proveedores',
                   'Monitorear entorno competitivo fintech en LATAM continuamente']),
    ],
    [
        came_cell('M', 'MANTENER', 'Fortalezas → Consolidar', VERDE,
                  'Preservar las capacidades diferenciales actuales:',
                  ['Consolidar arquitectura cloud-native y de microservicios',
                   'Sostener y madurar capacidades analíticas e IA existentes',
                   'Preservar enfoque digital-first como modelo central']),
        came_cell('E', 'EXPLOTAR', 'Oportunidades → Aprovechar', AZUL,
                  'Capitalizar las oportunidades del entorno fintech:',
                  ['Desarrollar APIs para integración en Open Banking',
                   'Expandir servicios personalizados con IA en LATAM',
                   'Innovar en aprobación crediticia con scoring alternativo',
                   'Crear productos financieros basados en analítica predictiva']),
    ],
]
came_table = Table(came_data, colWidths=[col_w, col_w])
came_table.setStyle(TableStyle([
    ('BACKGROUND', (0,1), (0,1), VERDE_L),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('GRID', (0,0), (-1,-1), 0.5, GRIS_BRD),
]))
story.append(came_table)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 5: OKRs Y ACCIONES ESTRATÉGICAS
# ══════════════════════════════════════════════════════════════════════════════
section_header(story, '5', 'OKRs y Acciones Estratégicas de TI')

story.append(Paragraph(
    'Los OKRs (Objectives and Key Results) de TI están alineados con los objetivos estratégicos '
    'del negocio y se derivan directamente del diagnóstico DOFA. Cada objetivo define resultados '
    'clave medibles que permiten monitorear el avance del PETI.',
    sec_body))
story.append(Spacer(1, 0.35*cm))

okrs = [
    {
        'num': 'OKR 1', 'color': ROJO, 'bg': ROJO_L,
        'obj': 'Eliminar el fraude digital como riesgo crítico operativo para NeoBankX',
        'krs': [
            'KR1: Reducir el fraude digital en un <b>35%</b> en los próximos 12 meses mediante detección ML en tiempo real',
            'KR2: Alcanzar una precisión <b>>95%</b> en el modelo de detección de fraude transaccional',
            'KR3: Reducir el tiempo de respuesta ante incidentes de seguridad a <b>&lt;60 minutos</b>',
        ],
        'alineacion': 'OE1 · Corrige D1 · Afronta A1',
    },
    {
        'num': 'OKR 2', 'color': AZUL, 'bg': AZUL_L,
        'obj': 'Consolidar a NeoBankX como la fintech más personalizada y confiable de LATAM',
        'krs': [
            'KR1: Incrementar el NPS (Net Promoter Score) de clientes en <b>25%</b> en 18 meses',
            'KR2: Reducir la tasa de abandono de clientes en <b>20%</b> mediante personalización de servicios',
        ],
        'alineacion': 'OE1 · Corrige D2 · Explota O3, O4',
    },
    {
        'num': 'OKR 3', 'color': VERDE, 'bg': VERDE_L,
        'obj': 'Garantizar que la infraestructura de TI soporte el crecimiento sin comprometer la experiencia',
        'krs': [
            'KR1: Alcanzar disponibilidad del <b>99.9%</b> en todos los servicios críticos de la plataforma',
            'KR2: Soportar crecimiento del <b>200%</b> en usuarios activos sin degradación del servicio',
        ],
        'alineacion': 'OE2 · Corrige D5 · Mantiene F1',
    },
]

for okr in okrs:
    header = Table([[
        Paragraph(okr['num'], S('ON', fontSize=10, textColor=BLANCO, fontName='Helvetica-Bold',
                                  leading=14, alignment=TA_CENTER)),
        Paragraph(f'<b>Objetivo:</b> {okr["obj"]}', sec_body),
        Paragraph(f'<font size="7.5" color="#{GRIS_MED.hexval()[2:]}">{okr["alineacion"]}</font>',
                   S('OA', fontSize=7.5, textColor=GRIS_MED, fontName='Helvetica',
                      leading=11, alignment=TA_RIGHT)),
    ]], colWidths=[1.5*cm, usable_w - 4.5*cm, 3*cm])
    header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), okr['color']),
        ('BACKGROUND', (1,0), (-1,0), okr['bg']),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (1,0), (1,0), 10),
        ('RIGHTPADDING', (2,0), (2,0), 8),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ]))

    kr_rows = []
    for kr in okr['krs']:
        kr_rows.append([
            Paragraph('', sec_body),
            Paragraph(f'\u25B8  {kr}', S('KR', fontSize=8.5, textColor=GRIS_OSC,
                       fontName='Helvetica', leading=13, leftIndent=6)),
        ])
    kr_table = Table(kr_rows, colWidths=[1.5*cm, usable_w - 1.5*cm])
    kr_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GRIS_L),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (1,0), (1,0), 10),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
        ('LINEABOVE', (0,0), (-1,0), 0, GRIS_BRD),
    ]))

    story.append(KeepTogether([header, kr_table, Spacer(1, 0.3*cm)]))

story.append(Spacer(1, 0.2*cm))
story.append(Paragraph('<b>Acciones Estratégicas Derivadas del DOFA/CAME</b>', bold_body))
story.append(Spacer(1, 0.2*cm))

acciones = [
    ('1', ROJO, ROJO_L, 'Fortalecimiento de la Seguridad Digital',
     'Implementar un sistema de detección de fraude en tiempo real basado en machine learning, '
     'capaz de analizar patrones transaccionales y comportamentales. Complementar con una '
     'arquitectura de seguridad que garantice la protección de los datos y transacciones.',
     'Reducción del fraude en 35%'),
    ('2', AZUL, AZUL_L, 'Desarrollo de Capacidades de Personalización',
     'Implementar motores de recomendación y segmentación avanzada que adapten productos '
     'y servicios financieros al perfil de comportamiento de cada cliente, utilizando los '
     'datos transaccionales y de interacción digital como fuente principal.',
     'Nuevos productos financieros personalizados'),
    ('3', VERDE, VERDE_L, 'Implementación de Modelos Predictivos',
     'Desarrollar o implementar modelos de analítica predictiva que permitan anticipar necesidades del cliente '
     'y perfeccionar los motores de decisión crediticia. El scoring alternativo con IA '
     'mejorará la precisión en aprobaciones y reducirá el riesgo de cartera.',
     'Aprobación crediticia más precisa'),
    ('4', AMBAR, AMBAR_L, 'Escalabilidad Tecnológica e Infraestructura',
     'Fortalecer y escalar la infraestructura cloud-native y de microservicios para garantizar '
     'alta disponibilidad, resiliencia y capacidad de respuesta ante el crecimiento acelerado '
     'de usuarios. Implementar estrategia multi-cloud para evitar dependencia de proveedor único.',
     'Soporte al crecimiento de usuarios'),
    ('5', AZUL, AZUL_L, 'Integración con Ecosistemas Digitales (Open Banking)',
     'Desarrollar e implementar APIs abiertas que faciliten la integración con terceros '
     'en el marco del Open Banking. Crear nuevos modelos de negocio colaborativos que '
     'amplíen la oferta de productos financieros personalizados y el alcance al mercado LATAM.',
     'Nuevos productos financieros personalizados'),
    ('6', VERDE, VERDE_L, 'Transformación Organizacional y Gestión del Cambio',
     'Ejecutar un programa de gestión del cambio que aborde los conflictos entre equipos '
     'tradicionales de riesgo y científicos de datos. Redefinir el rol del área de cumplimiento '
     'como habilitador de innovación. Adoptar prácticas DevSecOps y fortalecer la cultura '
     'organizacional orientada a datos, superando la resistencia e inseguridad frente a la IA.',
     'Habilitador transversal de todas las acciones'),
]

for num, col, bg, title, desc, meta in acciones:
    row = Table([[
        Paragraph(num, S('AN', fontSize=14, textColor=BLANCO, fontName='Helvetica-Bold',
                          alignment=TA_CENTER, leading=18)),
        [Paragraph(title, S('AT', fontSize=9.5, textColor=GRIS_OSC, fontName='Helvetica-Bold', leading=13)),
         Spacer(1, 3),
         Paragraph(desc, S('AD', fontSize=8.3, textColor=GRIS_MED, fontName='Helvetica',
                             leading=12, alignment=TA_JUSTIFY)),
         Spacer(1, 4),
         Paragraph(f'<b>Meta:</b> {meta}', S('AM', fontSize=8, textColor=AZUL,
                    fontName='Helvetica', leading=12))],
    ]], colWidths=[1.1*cm, usable_w - 1.1*cm])
    row.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), col),
        ('BACKGROUND', (1,0), (1,0), bg),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('VALIGN', (0,0), (0,0), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (1,0), (1,0), 10),
        ('RIGHTPADDING', (1,0), (1,0), 10),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ]))
    story.append(KeepTogether([row, Spacer(1, 0.18*cm)]))

story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 6: MODELO DE OPERACIÓN DE TI
# ══════════════════════════════════════════════════════════════════════════════
section_header(story, '6', 'Modelo de Operación de TI')

story.append(Paragraph(
    'El Modelo de Operación de TI define <b>cómo opera el área de tecnología en NeoBankX</b>: '
    'su estructura de trabajo, los mecanismos de entrega, la relación con el negocio y el '
    'gobierno de los activos tecnológicos y de datos. Para una fintech data-driven como NeoBankX, '
    'se adopta un modelo centrado en <b>productos digitales</b> con equipos autónomos (squads) '
    'organizados por dominios de negocio.',
    sec_body))
story.append(Spacer(1, 0.35*cm))

# Los 4 pilares del modelo
pilares = [
    (VERDE, VERDE_L, 'Modelo de Entrega\nÁgil (DevSecOps)',
     'Equipos multidisciplinarios organizados en squads por dominio. '
     'Ciclos de entrega continuos con CI/CD (GitHub Actions). '
     'Integración de seguridad en cada fase del desarrollo (DevSecOps). '
     'Sprints de 2 semanas con revisiones y demos al negocio.'),
    (AZUL, AZUL_L, 'Gobierno del Dato\n(DM-Book)',
     'Oficina de Gobierno del Dato con roles definidos (Data Owner, Data Steward, Data Custodian). '
     'Políticas de calidad, seguridad y acceso al dato. '
     'Catálogo de datos centralizado y gestión de metadatos. '
     'Modelo de madurez DMBOK como referencia de evolución.'),
    (ROJO, ROJO_L, 'Gestión de Riesgos\ny Cumplimiento',
     'Cumplimiento regulatorio embebido en los procesos de TI. '
     'Área de Cumplimiento redefinida como habilitadora de innovación. '
     'Monitoreo continuo de riesgos tecnológicos con COBIT. '
     'Auditorías periódicas de calidad de datos y seguridad.'),
    (AMBAR, AMBAR_L, 'Relación TI–Negocio\n(Business Partnership)',
     'Product Owners de negocio embebidos en los squads tecnológicos. '
     'OKRs compartidos entre TI y cada área de negocio. '
     'Comité de Arquitectura para decisiones tecnológicas estratégicas. '
     'Revisiones trimestrales de portafolio de iniciativas TI.'),
]

pil_rows = []
row1 = []
row2 = []
for i, (col, bg, title, desc) in enumerate(pilares):
    cell_content = (
        [Paragraph(title, S('PT', fontSize=9, textColor=col, fontName='Helvetica-Bold',
                             leading=12, alignment=TA_CENTER)),
         Spacer(1, 6)]
        + [Paragraph(f'\u2022  {l}', S('PD', fontSize=8, textColor=GRIS_OSC, fontName='Helvetica',
                                        leading=12, leftIndent=4))
           for l in desc.split('. ') if l.strip()]
    )
    cell = Table([[cell_content]], colWidths=[usable_w/2 - 0.3*cm])
    cell.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1, col),
    ]))
    if i < 2:
        row1.append(cell)
    else:
        row2.append(cell)

pil_table1 = Table([row1], colWidths=[usable_w/2 - 0.1*cm, usable_w/2 - 0.1*cm])
pil_table1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                                  ('LEFTPADDING', (0,0), (-1,-1), 0),
                                  ('RIGHTPADDING', (0,0), (-1,-1), 0),
                                  ('TOPPADDING', (0,0), (-1,-1), 0),
                                  ('BOTTOMPADDING', (0,0), (-1,-1), 4),]))
pil_table2 = Table([row2], colWidths=[usable_w/2 - 0.1*cm, usable_w/2 - 0.1*cm])
pil_table2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                                  ('LEFTPADDING', (0,0), (-1,-1), 0),
                                  ('RIGHTPADDING', (0,0), (-1,-1), 0),
                                  ('TOPPADDING', (0,0), (-1,-1), 0),
                                  ('BOTTOMPADDING', (0,0), (-1,-1), 0),]))
story.append(pil_table1)
story.append(Spacer(1, 0.15*cm))
story.append(pil_table2)
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph('<b>Dominios de TI y Squads Operativos</b>', bold_body))
story.append(Spacer(1, 0.2*cm))

dominios_data = [
    ['Dominio / Squad', 'Responsabilidad Principal', 'Tecnologías Clave', 'OKR Relacionado'],
    ['Fraude & Seguridad', 'Detección ML de fraude, Zero Trust, SIEM, respuesta a incidentes', 'TensorFlow, Vault, SIEM', 'OKR 1'],
    ['Datos & IA', 'Gobierno del dato (DM-Book), pipelines analíticos, Feature Store, MLflow', 'Snowflake, Spark, dbt', 'OKR 1, 2'],
    ['Plataforma & Infra', 'Cloud multi-cloud, microservicios, Kubernetes, disponibilidad 99.9%', 'AWS/GCP, Terraform, K8s', 'OKR 3'],
    ['Producto Digital', 'App móvil, Open Banking APIs, UX, onboarding digital', 'React Native, Kong API GW', 'OKR 2'],
    ['DevSecOps & Calidad', 'CI/CD, automatización, testing de seguridad, SLA de despliegue', 'GitHub Actions, SonarQube', 'OKR 3'],
    ['Cumplimiento & Regulatorio', 'Regulación proactiva, trazabilidad de datos, auditorías TI', 'COBIT, ISO 27001', 'OKR 1, 2, 3'],
]

dom_col_w = [usable_w*0.2, usable_w*0.35, usable_w*0.25, usable_w*0.2]
dom_rows = []
for i, row in enumerate(dominios_data):
    style_fn = lambda t: S('DH' if i==0 else 'DB',
                            fontSize=8.5 if i==0 else 8,
                            textColor=BLANCO if i==0 else GRIS_OSC,
                            fontName='Helvetica-Bold' if i==0 else 'Helvetica',
                            leading=12, alignment=TA_CENTER if i==0 else TA_LEFT)
    dom_rows.append([Paragraph(c, style_fn(c)) for c in row])

dom_table = Table(dom_rows, colWidths=dom_col_w)
dom_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), VERDE),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [BLANCO, VERDE_L]),
    ('GRID', (0,0), (-1,-1), 0.4, GRIS_BRD),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),
]))
story.append(dom_table)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 7: ESTRUCTURA ORGANIZACIONAL DE TI
# ══════════════════════════════════════════════════════════════════════════════
section_header(story, '7', 'Estructura Organizacional de TI')

story.append(Paragraph(
    'La estructura organizacional propuesta para NeoBankX resuelve la tensión identificada '
    'en el caso entre los <b>equipos tradicionales de riesgo y los científicos de datos</b>, '
    'mediante una organización matricial orientada a productos con dominios especializados '
    'bajo una dirección tecnológica unificada. El <b>Gobierno del Dato</b> actúa como función '
    'transversal, habilitando la coherencia entre todos los dominios en línea con el DM-Book.',
    sec_body))
story.append(Spacer(1, 0.35*cm))

org_niveles = [
    # Nivel 0: CTO
    [('CTO / Chief Technology Officer', VERDE, usable_w,
      'Visión tecnológica, gobierno TI (COBIT), relación con Junta Directiva y CEO')],
    # Nivel 1: 5 VPs
    [
        ('VP Ingeniería\nde Plataforma', AZUL, usable_w/5 - 0.2*cm,
         'Cloud, microservicios,\nDevSecOps, SRE'),
        ('VP Datos & IA', AZUL, usable_w/5 - 0.2*cm,
         'ML, scoring, fraude,\nFeature Store'),
        ('VP Ciberseguridad\n& Cumplimiento', ROJO, usable_w/5 - 0.2*cm,
         'Zero Trust, SIEM,\nregulatorio'),
        ('VP Producto\nDigital', AZUL, usable_w/5 - 0.2*cm,
         'App, Open Banking,\nUX, APIs'),
        ('Oficina Gobierno\ndel Dato (DMBOK)', VERDE, usable_w/5 - 0.2*cm,
         'Data Owners,\nData Stewards'),
    ],
]

# CTO box
cto_data = org_niveles[0]
for label, col, w, desc in cto_data:
    t = Table([[
        Paragraph(label, S('CT', fontSize=11, textColor=BLANCO, fontName='Helvetica-Bold',
                            alignment=TA_CENTER, leading=15)),
        Paragraph(desc, S('CD2', fontSize=8, textColor=colors.HexColor('#C0DD97'),
                           fontName='Helvetica', alignment=TA_CENTER, leading=11)),
    ]], colWidths=[w * 0.4, w * 0.6])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), col),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#27500A')),
    ]))
    story.append(t)

story.append(Spacer(1, 0.15*cm))

# VP level — tabla plana para que todas las celdas tengan el mismo alto
vp_row = []
col_widths_vp = []
vp_colors = []
for label, col, w, desc in org_niveles[1]:
    vp_row.append([
        Paragraph(label, S('VT', fontSize=8.5, textColor=BLANCO, fontName='Helvetica-Bold',
                            alignment=TA_CENTER, leading=11)),
        Spacer(1, 4),
        Paragraph(desc, S('VD', fontSize=7.5, textColor=colors.HexColor('#C0DD97'),
                           fontName='Helvetica', alignment=TA_CENTER, leading=10)),
    ])
    col_widths_vp.append(w + 0.1*cm)
    vp_colors.append(col)

vp_table = Table([vp_row], colWidths=col_widths_vp)
bg_style = [('BACKGROUND', (i, 0), (i, 0), vp_colors[i]) for i in range(len(vp_colors))]
vp_table.setStyle(TableStyle(bg_style + [
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 5),
    ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ('INNERGRID', (0,0), (-1,-1), 1, colors.HexColor('#27500A')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#27500A')),
]))
story.append(vp_table)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph(
    'La <b>Oficina de Gobierno del Dato</b> (alineada con DM-Book) actúa como función transversal '
    'que conecta todos los dominios, garantizando que los datos sean tratados como activos '
    'estratégicos con calidad, trazabilidad y seguridad. Resuelve los conflictos entre equipos '
    'de riesgo y ciencia de datos mediante estructuras de decisión claras.',
    sec_body))
story.append(Spacer(1, 0.3*cm))

roles_data = [
    ['Rol', 'Descripción', 'Dominio Principal'],
    ['CTO', 'Responsable de la visión y gobierno tecnológico. Interlocutor con CEO y Junta', 'Toda la organización TI'],
    ['VP Ingeniería de Plataforma', 'Dirige cloud, microservicios, DevSecOps y confiabilidad (SRE)', 'Plataforma & Infra'],
    ['VP Datos & IA', 'Lidera la estrategia de datos, modelos ML y capacidades analíticas', 'Datos & IA'],
    ['VP Ciberseguridad & Cumplimiento', 'Gestiona seguridad, riesgos tecnológicos y regulatorio', 'Fraude & Seguridad'],
    ['VP Producto Digital', 'Dirige la experiencia de usuario, app, Open Banking y APIs', 'Producto Digital'],
    ['Chief Data Officer (CDO)', 'Lidera la Oficina de Gobierno del Dato (DM-Book)', 'Gobierno del Dato'],
    ['Data Owner', 'Responsable del dato por dominio de negocio', 'Por dominio'],
    ['Data Steward', 'Gestiona calidad, metadatos y políticas del dato día a día', 'Por dominio'],
]

rol_col_w = [usable_w*0.28, usable_w*0.46, usable_w*0.26]
rol_rows = []
for i, row in enumerate(roles_data):
    if i == 0:
        rol_rows.append([Paragraph(c, S('RH', fontSize=8.5, textColor=BLANCO,
                          fontName='Helvetica-Bold', leading=12)) for c in row])
    else:
        rol_rows.append([Paragraph(c, S('RB', fontSize=8, textColor=GRIS_OSC,
                          fontName='Helvetica', leading=12)) for c in row])

rol_table = Table(rol_rows, colWidths=rol_col_w)
rol_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), AZUL),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [BLANCO, AZUL_L]),
    ('GRID', (0,0), (-1,-1), 0.4, GRIS_BRD),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
]))
story.append(rol_table)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 8: ESTIMACIONES DEL PETI
# ══════════════════════════════════════════════════════════════════════════════
section_header(story, '8', 'Estimaciones del PETI — Tiempos, Recursos y Costos')

story.append(Paragraph(
    'Las estimaciones del PETI se organizan en una hoja de ruta de <b>36 meses</b> con tres '
    'horizontes de ejecución. Los proyectos se priorizan según su impacto en los OKRs, '
    'su complejidad técnica y la disponibilidad de capacidades organizacionales.',
    sec_body))
story.append(Spacer(1, 0.35*cm))

# Leyenda de horizontes
hor_data = [
    [Paragraph('Corto Plazo\n0–6 meses', S('HL', fontSize=9, textColor=BLANCO,
                fontName='Helvetica-Bold', alignment=TA_CENTER, leading=12)),
     Paragraph('Mediano Plazo\n6–18 meses', S('HL', fontSize=9, textColor=BLANCO,
                fontName='Helvetica-Bold', alignment=TA_CENTER, leading=12)),
     Paragraph('Largo Plazo\n18–36 meses', S('HL', fontSize=9, textColor=BLANCO,
                fontName='Helvetica-Bold', alignment=TA_CENTER, leading=12))],
    [Paragraph('Fundamentos críticos: fraude,\ninfra base y gobierno del dato', cell_body),
     Paragraph('Escala y personalización:\nML, Open Banking, DevSecOps', cell_body),
     Paragraph('Innovación y liderazgo:\nIA avanzada, nuevos productos', cell_body)],
]
hor_table = Table(hor_data, colWidths=[usable_w/3]*3)
hor_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,0), ROJO),
    ('BACKGROUND', (1,0), (1,0), AMBAR),
    ('BACKGROUND', (2,0), (2,0), VERDE),
    ('BACKGROUND', (0,1), (0,1), ROJO_L),
    ('BACKGROUND', (1,1), (1,1), AMBAR_L),
    ('BACKGROUND', (2,1), (2,1), VERDE_L),
    ('GRID', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),
]))
story.append(hor_table)
story.append(Spacer(1, 0.35*cm))

proyectos = [
    ['Proyecto', 'Horizonte', 'Equipo Requerido', 'Costo Est. (USD)', 'OKR'],
    ['1. Motor Antifraude ML en Tiempo Real',
     'Corto\n0–6m', '2 Data Scientists, 1 MLOps, 1 Sec Engineer', '$180,000 – $240,000', 'OKR 1'],
    ['2. Programa Gobierno del Dato (DM-Book)\nOficina CDO + roles Data Owner/Steward',
     'Corto\n0–6m', '1 CDO, 4 Data Stewards, 1 Arquitecto de Datos', '$120,000 – $160,000', 'OKR 1,2,3'],
    ['3. Fortalecimiento Infraestructura Cloud\nMulti-cloud + Kubernetes + SRE',
     'Corto\n0–6m', '2 Cloud Engineers, 1 SRE, 1 Arquitecto Cloud', '$200,000 – $280,000', 'OKR 3'],
    ['4. Motor de Personalización y Recomendación\nSegmentación avanzada + Feature Store',
     'Mediano\n6–18m', '3 Data Scientists, 2 Backend Engineers, 1 PM', '$220,000 – $300,000', 'OKR 2'],
    ['5. Plataforma Open Banking & APIs\nKong API Gateway + OpenAPI 3.0',
     'Mediano\n6–18m', '2 API Engineers, 1 Sec Engineer, 1 PM', '$150,000 – $200,000', 'OKR 2,3'],
    ['6. Implementación DevSecOps Completo\nCI/CD, testing automático, DAST',
     'Mediano\n6–18m', '1 DevSecOps Lead, 2 Engineers, 1 QA', '$100,000 – $140,000', 'OKR 3'],
    ['7. Programa Gestión del Cambio Organizacional\nCapacitación, cultura data-driven',
     'Transversal\n0–36m', '1 Change Manager, 1 L&D Specialist', '$80,000 – $120,000', 'Todos'],
    ['8. Scoring Crediticio IA Avanzado\nDatos no tradicionales + modelo explicable',
     'Largo\n18–36m', '3 Data Scientists, 1 Regulatorio, 1 PM', '$250,000 – $350,000', 'OKR 2'],
    ['9. Nuevos Productos Financieros Digitales\nPersonalización predictiva + BNPL + Inversión',
     'Largo\n18–36m', '2 Product Managers, 3 Engineers, 2 Data Sc.', '$300,000 – $450,000', 'OKR 2'],
]

col_widths_proy = [usable_w*0.30, usable_w*0.10, usable_w*0.27, usable_w*0.19, usable_w*0.14]
proy_rows = []
for i, row in enumerate(proyectos):
    if i == 0:
        proy_rows.append([Paragraph(c, S('PH', fontSize=8, textColor=BLANCO,
                          fontName='Helvetica-Bold', leading=11, alignment=TA_CENTER)) for c in row])
    else:
        horizon = row[1].split('\n')[0]
        h_color = ROJO_L if 'Corto' in horizon else (AMBAR_L if 'Mediano' in horizon else (VERDE_L if 'Largo' in horizon else AZUL_L))
        proy_rows.append([
            Paragraph(row[0], S('PB', fontSize=7.8, textColor=GRIS_OSC, fontName='Helvetica', leading=11)),
            Paragraph(row[1], S('PH2', fontSize=7.5, textColor=GRIS_OSC, fontName='Helvetica-Bold',
                                 alignment=TA_CENTER, leading=10)),
            Paragraph(row[2], S('PB', fontSize=7.5, textColor=GRIS_OSC, fontName='Helvetica', leading=11)),
            Paragraph(row[3], S('PC', fontSize=7.8, textColor=VERDE, fontName='Helvetica-Bold', leading=11)),
            Paragraph(row[4], S('PO', fontSize=7.5, textColor=AZUL, fontName='Helvetica-Bold',
                                 alignment=TA_CENTER, leading=11)),
        ])

proy_table = Table(proy_rows, colWidths=col_widths_proy)

row_styles = [
    ('BACKGROUND', (0,0), (-1,0), AZUL),
    ('GRID', (0,0), (-1,-1), 0.4, GRIS_BRD),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 5),
    ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ('ALIGN', (1,0), (1,-1), 'CENTER'),
    ('ALIGN', (3,0), (3,-1), 'CENTER'),
    ('ALIGN', (4,0), (4,-1), 'CENTER'),
]
# Color por horizonte
for i, row in enumerate(proyectos[1:], 1):
    h = row[1]
    if 'Corto' in h:
        row_styles.append(('BACKGROUND', (1,i), (1,i), ROJO_L))
    elif 'Mediano' in h:
        row_styles.append(('BACKGROUND', (1,i), (1,i), AMBAR_L))
    elif 'Largo' in h:
        row_styles.append(('BACKGROUND', (1,i), (1,i), VERDE_L))
    else:
        row_styles.append(('BACKGROUND', (1,i), (1,i), AZUL_L))
    if i % 2 == 0:
        row_styles.append(('BACKGROUND', (0,i), (0,i), GRIS_L))
        row_styles.append(('BACKGROUND', (2,i), (2,i), GRIS_L))

proy_table.setStyle(TableStyle(row_styles))
story.append(proy_table)
story.append(Spacer(1, 0.35*cm))

# Resumen de inversión
inv_data = [
    ['Horizonte', 'Inversión Estimada (USD)', '% del Total'],
    ['Corto Plazo (0–6 meses)', '$500,000 – $680,000', '35%'],
    ['Mediano Plazo (6–18 meses)', '$470,000 – $640,000', '33%'],
    ['Largo Plazo (18–36 meses)', '$550,000 – $800,000', '38%'],
    ['Gestión del Cambio (transversal)', '$80,000 – $120,000', '6%'],
    ['INVERSIÓN TOTAL ESTIMADA', '$1,400,000 – $2,000,000', '100%'],
]
inv_col_w = [usable_w*0.40, usable_w*0.35, usable_w*0.25]
inv_rows = []
for i, row in enumerate(inv_data):
    is_header = i == 0
    is_total = i == len(inv_data) - 1
    style_row = []
    for c in row:
        if is_header:
            style_row.append(Paragraph(c, S('IH', fontSize=9, textColor=BLANCO,
                              fontName='Helvetica-Bold', leading=12, alignment=TA_CENTER)))
        elif is_total:
            style_row.append(Paragraph(c, S('IT', fontSize=9, textColor=VERDE,
                              fontName='Helvetica-Bold', leading=12,
                              alignment=TA_RIGHT if row.index(c) > 0 else TA_LEFT)))
        else:
            style_row.append(Paragraph(c, S('IB', fontSize=8.5, textColor=GRIS_OSC,
                              fontName='Helvetica', leading=12,
                              alignment=TA_RIGHT if row.index(c) > 0 else TA_LEFT)))
    inv_rows.append(style_row)

inv_table = Table(inv_rows, colWidths=inv_col_w)
inv_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), VERDE),
    ('BACKGROUND', (0,-1), (-1,-1), VERDE_L),
    ('ROWBACKGROUNDS', (0,1), (-1,-2), [BLANCO, GRIS_L]),
    ('GRID', (0,0), (-1,-1), 0.4, GRIS_BRD),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('LINEABOVE', (0,-1), (-1,-1), 1.5, VERDE),
]))
story.append(Paragraph('<b>Resumen de Inversión por Horizonte</b>', bold_body))
story.append(Spacer(1, 0.15*cm))
story.append(inv_table)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 9: MARCOS DE REFERENCIA
# ══════════════════════════════════════════════════════════════════════════════
section_header(story, '9', 'Marcos de Referencia Aplicados')

story.append(Paragraph(
    'El PETI de NeoBankX se articula sobre dos marcos de referencia complementarios: '
    'el <b>DM-Book (DAMA DMBOK)</b> como marco principal que gobierna la dimensión de datos, '
    'y <b>COBIT 2019</b> como marco complementario para el gobierno de TI y la gestión de '
    'riesgos. Juntos cubren las tres dimensiones clave: <b>estructura, procesos y personas</b>.',
    sec_body))
story.append(Spacer(1, 0.4*cm))

# ── 9.1 DM-BOOK ──────────────────────────────────────────────────────────────
story.append(Paragraph('9.1 DM-Book (DAMA DMBOK) — Marco Principal', sub_title))

dmbook_intro = Table([[
    Paragraph(
        'El <b>DM-Book (Data Management Body of Knowledge)</b>, desarrollado por DAMA International, '
        'es el estándar global para la gestión profesional de datos. Para NeoBankX, organización '
        'intensiva en datos, es el marco habilitador de toda su capacidad analítica, de seguridad '
        'y de innovación. Su propósito es triple: <b>estandarizar</b> prácticas de gestión de datos, '
        '<b>profesionalizar</b> la disciplina y <b>habilitar</b> el tratamiento del dato como activo '
        'estratégico.',
        sec_body)
]], colWidths=[usable_w])
dmbook_intro.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), VERDE_L),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ('BOX', (0,0), (-1,-1), 1, VERDE),
]))
story.append(dmbook_intro)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph('<b>Objetivos del DM-Book en NeoBankX</b>', bold_body))
story.append(Spacer(1, 0.15*cm))

obj_dm = [
    ('Estratégico', VERDE, [
        'Establecer visión empresarial del dato que trascienda las áreas independientes',
        'Definir roles, responsabilidades y estructuras de decisión sobre los datos',
        'Alinear gestión del dato con estrategia corporativa y marcos regulatorios',
    ]),
    ('Táctico', AZUL, [
        'Garantizar calidad, integridad, disponibilidad y seguridad de los datos en su ciclo de vida',
        'Establecer arquitecturas de datos coherentes, escalables e interoperables',
        'Habilitar capacidades de analítica avanzada sobre datos confiables',
    ]),
    ('Operacional', AMBAR, [
        'Gestionar metadatos para trazabilidad y comprensión del dato en toda la organización',
        'Administrar datos maestros y de referencia para eliminar inconsistencias entre sistemas',
        'Definir estándares de almacenamiento, integración y acceso a los datos',
    ]),
]

for nivel, col, items in obj_dm:
    row = Table([[
        Paragraph(nivel, S('NL', fontSize=9, textColor=BLANCO, fontName='Helvetica-Bold',
                            alignment=TA_CENTER, leading=12)),
        [bullet(it, col) for it in items],
    ]], colWidths=[1.8*cm, usable_w - 1.8*cm])
    row.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), col),
        ('BACKGROUND', (1,0), (1,0), GRIS_L),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('VALIGN', (0,0), (0,0), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (1,0), (1,0), 10),
        ('RIGHTPADDING', (1,0), (1,0), 10),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ]))
    story.append(KeepTogether([row, Spacer(1, 0.15*cm)]))

story.append(Spacer(1, 0.25*cm))
story.append(Paragraph('<b>Las 11 Áreas de Conocimiento del DM-Book y su Aplicación en NeoBankX</b>', bold_body))
story.append(Spacer(1, 0.15*cm))

areas_dm = [
    ['Área de Conocimiento', 'Descripción', 'Aplicación en NeoBankX'],
    ['Gobernanza de Datos', 'Función central: roles, responsabilidades y decisiones sobre datos',
     'Oficina CDO, Data Owners y Stewards por cada dominio operativo'],
    ['Arquitectura de Datos', 'Estructura, diseño y flujo de datos en estado actual y objetivo',
     'Diseño cloud-native con microservicios y pipelines de datos'],
    ['Modelado y Diseño', 'Modelos conceptuales, lógicos y físicos de datos organizacionales',
     'Modelos de clientes, transacciones, fraude y scoring crediticio'],
    ['Almacenamiento y Operaciones', 'Gestión de bases de datos, respaldo y retención de datos',
     'Snowflake + Delta Lake para datos analíticos; bases operacionales'],
    ['Seguridad de Datos', 'Confidencialidad, integridad y disponibilidad de datos',
     'Zero Trust, cifrado, enmascaramiento de datos sensibles PCI-DSS'],
    ['Integración e Interoperabilidad', 'ETL/ELT, eventos en tiempo real, APIs internas y externas',
     'Open Banking APIs, Kafka para eventos, integración con terceros'],
    ['Gestión de Documentos', 'Datos no estructurados: contratos, formularios, contenido digital',
     'Gestión de KYC, contratos digitales y documentos regulatorios'],
    ['Datos Maestros y Referencia', 'Versión única y confiable de entidades de negocio clave',
     'MDM de clientes, productos financieros y códigos de referencia'],
    ['Data Warehousing & BI', 'Repositorios analíticos y plataformas de inteligencia de negocio',
     'Dashboards de fraude, fidelización y performance de crédito'],
    ['Gestión de Metadatos', 'Catálogo de datos: datos sobre los datos de la organización',
     'Catálogo centralizado para trazabilidad y data lineage'],
    ['Calidad de Datos', 'Completitud, precisión, consistencia, oportunidad, unicidad, validez',
     'Calidad de datos de entrada para modelos ML antifraude y scoring'],
]

areas_col_w = [usable_w*0.24, usable_w*0.38, usable_w*0.38]
areas_rows = []
for i, row in enumerate(areas_dm):
    if i == 0:
        areas_rows.append([Paragraph(c, S('AH', fontSize=8.5, textColor=BLANCO,
                           fontName='Helvetica-Bold', leading=12)) for c in row])
    else:
        areas_rows.append([Paragraph(c, S('AB', fontSize=7.8, textColor=GRIS_OSC,
                           fontName='Helvetica', leading=11)) for c in row])

areas_table = Table(areas_rows, colWidths=areas_col_w)
areas_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), VERDE),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [BLANCO, VERDE_L]),
    ('BACKGROUND', (0,1), (0,1), colors.HexColor('#D4EDBA')),
    ('GRID', (0,0), (-1,-1), 0.4, GRIS_BRD),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,1), (0,-1), 7.8),
]))
story.append(areas_table)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph('<b>Decisión Informada: ¿Por qué DM-Book es el marco principal?</b>', bold_body))
story.append(Spacer(1, 0.15*cm))

decision_rows = [
    ('Problema NeoBankX', 'Contribución DM-Book'),
    ('Fraude digital elevado', 'Mejora calidad e integridad del dato → mayor precisión de modelos ML antifraude'),
    ('Baja fidelización', 'Datos maestros consistentes → mejor personalización y analítica del cliente'),
    ('Escalabilidad limitada', 'Arquitectura de datos desacoplada → pipelines escalables y sin cuellos de botella'),
    ('Conflicto riesgo vs. data science', 'Gobierno del dato → roles claros, reduce ambigüedades entre equipos'),
    ('Cumplimiento regulatorio', 'Trazabilidad, control de acceso y auditoría de datos integrados'),
]
dec_col_w = [usable_w*0.35, usable_w*0.65]
dec_rows_para = []
for i, (prob, contrib) in enumerate(decision_rows):
    if i == 0:
        dec_rows_para.append([
            Paragraph(prob, S('DH', fontSize=8.5, textColor=BLANCO, fontName='Helvetica-Bold', leading=12)),
            Paragraph(contrib, S('DH', fontSize=8.5, textColor=BLANCO, fontName='Helvetica-Bold', leading=12)),
        ])
    else:
        dec_rows_para.append([
            Paragraph(f'\u26A0  {prob}', S('DP', fontSize=8, textColor=ROJO, fontName='Helvetica-Bold', leading=12)),
            Paragraph(f'\u2713  {contrib}', S('DC', fontSize=8, textColor=VERDE, fontName='Helvetica', leading=12)),
        ])
dec_table = Table(dec_rows_para, colWidths=dec_col_w)
dec_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), GRIS_MED),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [BLANCO, VERDE_L]),
    ('GRID', (0,0), (-1,-1), 0.4, GRIS_BRD),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
story.append(dec_table)
story.append(Spacer(1, 0.3*cm))

riesgos_box = Table([[
    [Paragraph('<b>Riesgos de NO implementar el DM-Book</b>', S('RBH', fontSize=9,
                textColor=ROJO, fontName='Helvetica-Bold', leading=13)),
     Spacer(1, 5)] + [bullet(r, ROJO, 9) for r in [
        'Datos inconsistentes reducen la efectividad de modelos antifraude',
        'Baja calidad de datos impacta negativamente el scoring crediticio',
        'Ausencia de arquitectura estructurada genera cuellos de botella de escalabilidad',
        'Conflictos organizacionales se agravan sin gobierno claro del dato',
        'Riesgos regulatorios por falta de trazabilidad y control de datos',
    ]],
]], colWidths=[usable_w])
riesgos_box.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), ROJO_L),
    ('BOX', (0,0), (-1,-1), 1, ROJO),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
]))
story.append(riesgos_box)
story.append(PageBreak())

# ── 9.2 COBIT ────────────────────────────────────────────────────────────────
story.append(Paragraph('9.2 COBIT 2019 — Marco Complementario de Gobierno de TI', sub_title))

cobit_intro = Table([[
    Paragraph(
        '<b>COBIT 2019</b> (Control Objectives for Information and Related Technologies), '
        'desarrollado por ISACA, es el marco internacional de referencia para el <b>gobierno '
        'y gestión de la información y la tecnología empresarial</b>. En NeoBankX, COBIT 2019 '
        'complementa al DM-Book actuando en la capa de <b>gobierno corporativo de TI</b>, '
        'mientras el DM-Book se enfoca en la gestión del dato como activo.',
        sec_body)
]], colWidths=[usable_w])
cobit_intro.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), MORADO_L),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ('BOX', (0,0), (-1,-1), 1, MORADO),
]))
story.append(cobit_intro)
story.append(Spacer(1, 0.3*cm))

cobit_areas = [
    ('EDM\nEvaluar, Orientar\ny Supervisar', MORADO,
     'Gobierno de TI a nivel de Junta/CTO. Alineación de la estrategia TI con el negocio. '
     'En NeoBankX: evaluación del portafolio de proyectos del PETI, supervisión del riesgo tecnológico.'),
    ('APO\nAlinear, Planificar\ny Organizar', AZUL,
     'Planificación estratégica y arquitectura TI. '
     'En NeoBankX: gestión del portafolio de proyectos, planificación de recursos y presupuesto TI.'),
    ('BAI\nConstruir, Adquirir\ne Implementar', VERDE,
     'Gestión de proyectos, desarrollo y adquisición de soluciones. '
     'En NeoBankX: implementación de motor antifraude, Open Banking y DevSecOps.'),
    ('DSS\nEntregar, Dar Servicio\ny Soporte', AMBAR,
     'Operación de servicios TI con disponibilidad y continuidad. '
     'En NeoBankX: SLA 99.9%, respuesta a incidentes <60min, soporte a plataforma.'),
    ('MEA\nMonitorear, Evaluar\ny Valorar', ROJO,
     'Monitoreo de desempeño y cumplimiento de TI. '
     'En NeoBankX: seguimiento de OKRs, auditorías regulatorias y evaluación del PETI.'),
]

for sigla, col, desc in cobit_areas:
    row = Table([[
        Paragraph(sigla, S('CS', fontSize=8.5, textColor=BLANCO, fontName='Helvetica-Bold',
                            alignment=TA_CENTER, leading=11)),
        Paragraph(desc, S('CD3', fontSize=8.3, textColor=GRIS_OSC, fontName='Helvetica',
                           leading=12, alignment=TA_JUSTIFY)),
    ]], colWidths=[2.5*cm, usable_w - 2.5*cm])
    row.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), col),
        ('BACKGROUND', (1,0), (1,0), GRIS_L),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (0,0), 5),
        ('LEFTPADDING', (1,0), (1,0), 10),
        ('RIGHTPADDING', (1,0), (1,0), 10),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ]))
    story.append(KeepTogether([row, Spacer(1, 0.12*cm)]))

story.append(Spacer(1, 0.3*cm))

# Tabla comparativa DM-Book vs COBIT
story.append(Paragraph('<b>DM-Book vs. COBIT 2019 — Complementariedad en NeoBankX</b>', bold_body))
story.append(Spacer(1, 0.15*cm))

comp_data = [
    ['Dimensión', 'DM-Book (Marco Principal)', 'COBIT 2019 (Marco Complementario)'],
    ['Foco', 'Gestión del dato como activo estratégico', 'Gobierno corporativo de TI'],
    ['Nivel', 'Operacional y táctico de datos', 'Estratégico y de gobierno TI'],
    ['Ámbito', 'Calidad, seguridad, arquitectura del dato', 'Portafolio TI, riesgos, cumplimiento'],
    ['Actor principal', 'CDO, Data Stewards, Data Owners', 'CTO, Junta Directiva, Auditores'],
    ['En NeoBankX', 'Gobierno del dato para fraude, crédito y personalización', 'Supervisión del PETI, OKRs y riesgo TI'],
    ['Resultado', 'Datos confiables para modelos ML e IA', 'TI alineada a objetivos del negocio'],
]
comp_col_w = [usable_w*0.20, usable_w*0.40, usable_w*0.40]
comp_rows = []
for i, row in enumerate(comp_data):
    if i == 0:
        comp_rows.append([Paragraph(c, S('CH2', fontSize=8.5, textColor=BLANCO,
                           fontName='Helvetica-Bold', leading=12)) for c in row])
    else:
        comp_rows.append([
            Paragraph(row[0], S('CB', fontSize=8, textColor=GRIS_OSC, fontName='Helvetica-Bold', leading=12)),
            Paragraph(row[1], S('CB', fontSize=8, textColor=GRIS_OSC, fontName='Helvetica', leading=12)),
            Paragraph(row[2], S('CB', fontSize=8, textColor=GRIS_OSC, fontName='Helvetica', leading=12)),
        ])
comp_table = Table(comp_rows, colWidths=comp_col_w)
comp_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,-1), GRIS_L),
    ('BACKGROUND', (0,0), (-1,0), GRIS_OSC),
    ('BACKGROUND', (1,1), (1,-1), VERDE_L),
    ('BACKGROUND', (2,1), (2,-1), MORADO_L),
    ('ROWBACKGROUNDS', (0,0), (0,-1), [GRIS_L]),
    ('GRID', (0,0), (-1,-1), 0.4, GRIS_BRD),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 7),
    ('RIGHTPADDING', (0,0), (-1,-1), 7),
]))
story.append(comp_table)
story.append(Spacer(1, 0.4*cm))

# ── 9.3 Justificación: Estructura, Procesos, Personas ────────────────────────
story.append(Paragraph('9.3 Justificación de Marcos: Estructura, Procesos y Personas', sub_title))

justif = [
    ('ESTRUCTURA', VERDE, VERDE_L, [
        ('DM-Book', 'Define la arquitectura de datos de NeoBankX: modelos de datos, '
         'catálogo de metadatos, arquitectura de integración cloud-native y '
         'la Oficina de Gobierno del Dato con CDO, Data Owners y Data Stewards.'),
        ('COBIT 2019', 'Establece la estructura de gobierno corporativo de TI: '
         'comités de dirección, responsabilidades del CTO y definición '
         'del portafolio estratégico de proyectos tecnológicos.'),
    ]),
    ('PROCESOS', AZUL, AZUL_L, [
        ('DM-Book', 'Normaliza los procesos de gestión del dato: ingesta, calidad, '
         'integración, seguridad, metadatos y gobierno en cada fase del ciclo de vida '
         'del dato. Aplica directamente en los pipelines de ML de fraude y scoring.'),
        ('COBIT 2019', 'Estructura los procesos de TI en cinco dominios (EDM, APO, BAI, DSS, MEA), '
         'cubriendo desde la planificación estratégica hasta el monitoreo de cumplimiento '
         'y la auditoría de las iniciativas del PETI.'),
    ]),
    ('PERSONAS', AMBAR, AMBAR_L, [
        ('DM-Book', 'Define roles especializados de gestión del dato que resuelven el '
         'conflicto entre equipos de riesgo y ciencia de datos: Data Owner (dueño del dato '
         'por dominio), Data Steward (custodia operativa) y CDO (liderazgo estratégico del dato).'),
        ('COBIT 2019', 'Establece responsabilidades de gobierno para CTO, Junta Directiva y '
         'auditores. Promueve la cultura de cumplimiento y responsabilidad tecnológica '
         'en todos los niveles organizacionales de NeoBankX.'),
    ]),
]

for dim, col, bg, marcos in justif:
    header = Table([[
        Paragraph(dim, S('JH', fontSize=10, textColor=BLANCO, fontName='Helvetica-Bold',
                          alignment=TA_CENTER, leading=14)),
    ]], colWidths=[usable_w])
    header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), col),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ]))
    story.append(header)

    marco_rows = []
    for marco_name, marco_desc in marcos:
        marco_rows.append([
            Paragraph(marco_name, S('MN', fontSize=8.5, textColor=col,
                       fontName='Helvetica-Bold', leading=12, alignment=TA_CENTER)),
            Paragraph(marco_desc, S('MD', fontSize=8.3, textColor=GRIS_OSC,
                       fontName='Helvetica', leading=12, alignment=TA_JUSTIFY)),
        ])
    marco_table = Table(marco_rows, colWidths=[2.0*cm, usable_w - 2.0*cm])
    marco_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('BACKGROUND', (0,0), (0,-1), bg),
        ('GRID', (0,0), (-1,-1), 0.4, GRIS_BRD),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('VALIGN', (0,0), (0,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (0,-1), 6),
        ('LEFTPADDING', (1,0), (1,-1), 10),
        ('RIGHTPADDING', (1,0), (1,-1), 10),
    ]))
    story.append(marco_table)
    story.append(Spacer(1, 0.2*cm))

story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 10: CONCLUSIONES Y RECOMENDACIONES
# ══════════════════════════════════════════════════════════════════════════════
section_header(story, '10', 'Conclusiones y Recomendaciones')

story.append(Paragraph(
    'El PETI de NeoBankX establece una hoja de ruta integral para transformar la organización '
    'en la fintech de mayor confianza y personalización en Latinoamérica, abordando sus tres '
    'problemas críticos desde una perspectiva técnica, organizacional y estratégica.',
    sec_body))
story.append(Spacer(1, 0.35*cm))

conclusiones = [
    ('Diagnóstico integral y contextualizado', VERDE,
     'El análisis DOFA permitió identificar los principales retos de NeoBankX '
     '(fraude, baja fidelización, escalabilidad) desde las dimensiones tecnológica, '
     'organizacional y competitiva. La Matriz CAME traduce estos hallazgos en estrategias '
     'concretas y las acciones estratégicas establecen la hoja de ruta ejecutable.'),
    ('El dato como activo estratégico', AZUL,
     'Los problemas de NeoBankX tienen raíz en la gestión deficiente del dato. '
     'El DM-Book, como marco principal, provee la estructura, los procesos y los roles '
     'necesarios para que NeoBankX trate el dato como activo crítico, mejorando '
     'directamente los modelos de fraude, crédito y personalización.'),
    ('Gobierno TI robusto con COBIT', MORADO,
     'COBIT 2019 complementa al DM-Book dotando a NeoBankX de un marco de gobierno '
     'corporativo de TI. Garantiza la alineación estratégica entre TI y el negocio, '
     'el monitoreo del portafolio del PETI y el cumplimiento regulatorio en el '
     'dinámico entorno fintech latinoamericano.'),
    ('Modelo de operación orientado a producto', AMBAR,
     'La adopción de squads por dominio con DevSecOps y la Oficina de Gobierno del Dato '
     'transversal resuelve el conflicto entre equipos de riesgo y científicos de datos, '
     'estableciendo estructuras claras de responsabilidad, colaboración y entrega continua.'),
    ('Inversión justificada y priorizada', ROJO,
     'La inversión estimada de USD 1.4M–2.0M en 36 meses se justifica por el retorno '
     'esperado: reducción del fraude en 35%, incremento del NPS en 25% y soporte al '
     'crecimiento de 2x en usuarios. La priorización en horizontes garantiza '
     'resultados tangibles desde los primeros 6 meses.'),
]

for title_c, col, body_c in conclusiones:
    box = Table([[
        Paragraph(title_c, S('CT', fontSize=9, textColor=col, fontName='Helvetica-Bold', leading=13)),
        Paragraph(body_c, S('CB2', fontSize=8.5, textColor=GRIS_OSC, fontName='Helvetica',
                              leading=13, alignment=TA_JUSTIFY)),
    ]], colWidths=[3.8*cm, usable_w - 3.8*cm])
    box.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,-1), 9),
        ('LEFTPADDING', (0,0), (0,0), 10),
        ('LEFTPADDING', (1,0), (1,0), 12),
        ('RIGHTPADDING', (1,0), (1,0), 10),
        ('BACKGROUND', (0,0), (0,0), colors.HexColor(
            '#EAF3DE' if col == VERDE else
            '#E6F1FB' if col == AZUL else
            '#F0E8F8' if col == MORADO else
            '#FAEEDA' if col == AMBAR else '#FAECE7')),
        ('BACKGROUND', (1,0), (1,0), GRIS_L),
        ('LINEAFTER', (0,0), (0,-1), 2, col),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
    ]))
    story.append(KeepTogether([box, Spacer(1, 0.2*cm)]))

story.append(Spacer(1, 0.35*cm))
story.append(Paragraph('<b>Recomendaciones para Sostenibilidad y Madurez Digital Futura</b>', bold_body))
story.append(Spacer(1, 0.2*cm))

recomendaciones = [
    ('Evolución del Modelo de Madurez', VERDE,
     'Adoptar el Modelo de Madurez de DAMA DMBOK para evaluar anualmente el nivel de '
     'gestión del dato en NeoBankX, estableciendo metas de madurez progresivas en cada '
     'uno de los 11 dominios del marco.'),
    ('Sostenibilidad del Gobierno del Dato', AZUL,
     'Institucionalizar la Oficina de Gobierno del Dato con presupuesto propio, OKRs '
     'específicos y reporte directo al CTO. Garantizar que el CDO participe en las '
     'decisiones estratégicas del negocio, no solo de TI.'),
    ('Innovación Continua con IA Responsable', AMBAR,
     'Establecer un Centro de Excelencia en IA que garantice el desarrollo de modelos '
     'explicables, auditables y justos, alineados con las regulaciones de IA emergentes '
     'en LATAM y los principios de ética de datos del DM-Book.'),
    ('Ecosistema de Partners y Open Banking', MORADO,
     'Desarrollar una estrategia de ecosistema que convierta a NeoBankX en plataforma '
     'de Open Banking líder en LATAM, aprovechando las APIs como canal de nuevos '
     'ingresos y de expansión a nuevos segmentos y geografías.'),
]

for title_r, col, body_r in recomendaciones:
    row = Table([[
        Paragraph(f'\u25B6  {title_r}', S('RT', fontSize=9, textColor=col,
                   fontName='Helvetica-Bold', leading=13)),
        Paragraph(body_r, S('RB2', fontSize=8.5, textColor=GRIS_OSC, fontName='Helvetica',
                              leading=13, alignment=TA_JUSTIFY)),
    ]], colWidths=[3.5*cm, usable_w - 3.5*cm])
    row.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (0,0), 8),
        ('LEFTPADDING', (1,0), (1,0), 10),
        ('RIGHTPADDING', (1,0), (1,0), 10),
        ('BACKGROUND', (0,0), (0,0), GRIS_L),
        ('BACKGROUND', (1,0), (1,0), BLANCO),
        ('BOX', (0,0), (-1,-1), 0.5, GRIS_BRD),
        ('LINEAFTER', (0,0), (0,-1), 1.5, col),
    ]))
    story.append(KeepTogether([row, Spacer(1, 0.12*cm)]))

story.append(Spacer(1, 0.5*cm))

# Cierre final
cierre = Table([[
    Paragraph(
        'El PETI de NeoBankX no es solo un plan tecnológico: es la hoja de ruta para que '
        'la organización eleve su madurez digital, trate el dato como su activo más valioso '
        'y se posicione como referente de confianza e innovación en el sector fintech de '
        'Latinoamérica. La combinación del <b>DM-Book como gobierno del dato</b> y '
        '<b>COBIT 2019 como gobierno de TI</b> garantiza una ejecución coherente, '
        'medible y sostenible en el tiempo.',
        sec_body),
]], colWidths=[usable_w])
cierre.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), VERDE_L),
    ('TOPPADDING', (0,0), (-1,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 14),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
    ('BOX', (0,0), (-1,-1), 1.5, VERDE),
]))
story.append(cierre)

# ══════════════════════════════════════════════════════════════════════════════
# REFERENCIAS BIBLIOGRÁFICAS
# ══════════════════════════════════════════════════════════════════════════════
story.append(PageBreak())
section_header(story, '', 'Referencias Bibliográficas')

refs = [
    'DAMA International. (2017). <i>DAMA-DMBOK: Data Management Body of Knowledge</i> (2nd ed.). Technics Publications.',
    'ISACA. (2019). <i>COBIT 2019 Framework: Introduction and Methodology</i>. ISACA.',
    'Porter, M. E., &amp; Heppelmann, J. E. (2015). How smart, connected products are transforming companies. <i>Harvard Business Review, 93</i>(10), 96–114.',
    'McKinsey &amp; Company. (2021). <i>Global banking annual review 2021: The great divergence</i>. McKinsey &amp; Company. https://www.mckinsey.com/',
    'Nubank. (2024). <i>Our Mission and Values</i>. https://canvasbusinessmodel.com/blogs/mission/nubank-mission',
    'PayPal. (2024). <i>Mission, Vision and Values</i>. https://www.paypalobjects.com/digitalassets/',
    'FasterCapital. (2024). <i>Fintech startup vision and mission: Crafting a vision</i>. https://fastercapital.com/',
    'OpenAI. (2024). ChatGPT [Large language model]. https://chat.openai.com/',
]
for r in refs:
    story.append(Paragraph(r, S('REF', fontSize=8.2, textColor=GRIS_MED, fontName='Helvetica',
                                  leading=13, leftIndent=12, firstLineIndent=-12, spaceAfter=5)))

# ══════════════════════════════════════════════════════════════════════════════
# BUILD
# ══════════════════════════════════════════════════════════════════════════════
doc.build(story,
          onFirstPage=lambda c, d: on_cover(c, d),
          onLaterPages=lambda c, d: on_page(c, d))

print(f'PDF generado exitosamente: {OUTPUT}')
