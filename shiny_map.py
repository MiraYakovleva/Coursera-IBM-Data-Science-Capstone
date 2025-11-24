from shiny import App, ui, render
import folium
from htmltools import HTML

# ---------- UI ----------
app_ui = ui.page_sidebar(
    ui.sidebar(
        #ui.h5("Filtros"),

        ui.h6("Tipos dispositivos"),
        ui.input_radio_buttons(
            "tipo", None,
            ["Traveller", "Wooden", "Coconut", "Ranger"],
            inline=False
        ),

        ui.h6("Información oceanográfica"),
        ui.input_radio_buttons(
            "info", None,
            ["Oleaje", "Corrientes", "Viento"],
            inline=False
        ),

        ui.h6("Estado dispositivos"),
        ui.input_radio_buttons(
            "estado", None,
            ["En el agua", "Recogidos"],
            inline=False
        ),
        width=300
    ),

    # вместо output_plot теперь html-контейнер для карты
    ui.output_ui("map", height="100vh", width="100%"),

    ui.head_content(
        ui.tags.style("""
            html, body { height: 100%; margin: 0; padding: 0; }
            .bslib-page-sidebar .main,
            .bslib-page-sidebar .content,
            .container-fluid {
                padding: 0 !important;
                margin: 0 !important;
            }
            .bslib-page-sidebar .sidebar h4,
            .bslib-page-sidebar .sidebar h5,
            .bslib-page-sidebar .sidebar h6 {
                font-weight: 600 !important;
                letter-spacing: 0.2px;
            }
            #map, .shiny-html-output { margin: 0 !important; height: 100vh !important; }
        """)
    ),

    title=ui.tags.div(
        ui.tags.img(
            src="www/ulysses_logo.png",
            height="40px",
            style="margin-right:12px; vertical-align:middle;"
        ),
        ui.tags.span("ULYSSES DATA FOR SCIENCE",
            style="font-weight:600; font-size:20px; vertical-align:middle;"
        ),
        style="display:flex; align-items:center;"
    ),

)

# ---------- Server ----------
def server(input, output, session):

    @output
    @render.ui
    def map():
        # создаём карту
        m = folium.Map(
            location=[0, 0],  # центр (экватор)
            zoom_start=2,
            tiles="CartoDB positron"  # нейтральная цветовая схема
        )

        # пример: добавим маркеры
        # folium.Marker([40.4168, -3.7038], popup="Madrid", tooltip="Madrid").add_to(m)
        # folium.Marker([48.8566, 2.3522], popup="Paris", tooltip="Paris").add_to(m)
        # folium.Marker([35.6895, 139.6917], popup="Tokyo", tooltip="Tokyo").add_to(m)

        # преобразуем карту в HTML
        return HTML(m._repr_html_())

app = App(app_ui, server)
