import dash_leaflet as dl
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_leaflet.express as dlx
from dash_extensions.javascript import arrow_function
import geopandas as gpd


keys = {
    "One": {
        "url": "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png",
        "name": "Terrain"
    },
    "Two": {
        "url": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        "name": "Open Street Map"
    },
    "Three": {
        "url": "http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}",
        "name": "Google Satellite Imagery"
    }
}


attribution = '&copy; <a href="http://www.khrw.ir/">Khorasan Regional Water Company</a> '


# -----------------------------------------------------------------------------
# SHAPEFILES LOCATION
# -----------------------------------------------------------------------------
AQUIFERS = "./assets/Aquifers.geojson"
MAHDOUDE = "./assets/Mahdoude.geojson"
HOZEH6 = "./assets/Hozeh6.geojson"
HOZEH30 = "./assets/Hozeh30.geojson"
OSTAN = "./assets/Ostan.geojson"
SHAHRESTAN = "./assets/Shahrestan.geojson"



info = html.Div(
    id="info",
    className="info",
    style={
        "position": "absolute",
        "bottom": "10px",
        "left": "10px",
        "zIndex": "1000"
    },
    dir="rtl"
)


search_bar = html.Div(
    children=[
        dcc.Input(
            id="search_lat_lng",
            type="search",
            placeholder="Lat: 36.30 Lon: 59.60",
            debounce=True,
            className="form-control"
        )
    ],
    style={
        "position": "absolute",
        "top": "10px",
        "left": "50px",
        "zIndex": "1000"
    },
    dir="ltr"
)

model = html.Div(
    children=[
        dbc.Modal(
            id="modal",
            centered=True,
            is_open=False,
            children=[
                dbc.ModalHeader(
                    id="modal_header"
                ),
                dbc.ModalBody(
                    id="modal_body"
                )
            ]
        )
    ]
)

model2 = html.Div(
    children=[
        dbc.Modal(
            id="modal2",
            centered=True,
            is_open=False,
            children=[
                dbc.ModalHeader(
                    id="modal2_header"
                ),
                dbc.ModalBody(
                    id="modal2_body"
                )
            ]
        )
    ]
)


model3 = html.Div(
    children=[
        dbc.Modal(
            # size="xl",
            id="modal3",
            centered=True,
            is_open=False,
            children=[
                dbc.ModalHeader(
                    id="modal3_header"
                ),
                dbc.ModalBody(
                    id="modal3_body"
                )
            ]
        )
    ]
)


# -------------------------------------------------------------------------------------------------
# TAB HOME - BODY
# -------------------------------------------------------------------------------------------------


TAB_HOME_BODY = html.Div([
    
    html.Div(
        children=[
            
            dl.Map(
                id="map",
#                 center=[36.30, 59.60],
                zoom=5,
                children=[
                    dl.LayersControl(
                        children=[
                            dl.BaseLayer(
                                children=[
                                    dl.TileLayer(
                                        url=key["url"],
                                        attribution=attribution
                                    ),
                                ],
                                name=key["name"],
                                checked=key["name"] == "Open Street Map"  
                            ) for key in keys.values()                            
                        ] + [
                            dl.Overlay(
                                children=[
                                    dl.LayerGroup(
                                        id="layer"
                                    )                                    
                                ],
                                name="click+search",
                                checked=True
                            )                            
                        ] + [
                            dl.Overlay(
                                children=[
                                    dl.GeoJSON(
                                        id="ostan",
                                        url=OSTAN,
#                                         zoomToBounds=True,
#                                         zoomToBoundsOnClick=True,
                                        hoverStyle=arrow_function(
                                            dict(
                                                weight=5,
                                                color='#222',
                                                dashArray=''
                                            )
                                        ),
                                        options={
                                            "style": {
                                                "color": "blue"
                                            }
                                        }                                       
                                    )                                    
                                ],
                                name="استان",
                                checked=False
                            )                            
                        ] + [
                            dl.Overlay(
                                children=[
                                    dl.GeoJSON(
                                        id="shahrestan",
                                        url=SHAHRESTAN,
#                                         zoomToBounds=True,
                                        zoomToBoundsOnClick=True,
                                        hoverStyle=arrow_function(
                                            dict(
                                                weight=5,
                                                color='#222',
                                                dashArray=''
                                            )
                                        ),
                                        options={
                                            "style": {
                                                "color": "#FD8D3C"
                                            }
                                        }                                       
                                    )                                    
                                ],
                                name="شهرستان",
                                checked=False
                            )                            
                        ] + [
                            dl.Overlay(
                                children=[
                                    dl.GeoJSON(
                                        id="hozeh6",
                                        url=HOZEH6,
#                                         zoomToBounds=True,
#                                         zoomToBoundsOnClick=True,
                                        hoverStyle=arrow_function(
                                            dict(
                                                weight=5,
                                                color='#222',
                                                dashArray=''
                                            )
                                        ),
                                        options={
                                            "style": {
                                                "color": "red"
                                            }
                                        },
                                    )                                    
                                ],
                                name="حوضه درجه یک",
                                checked=False
                            )                            
                        ] + [
                            dl.Overlay(
                                children=[
                                    dl.GeoJSON(
                                        id="hozeh30",
                                        url=HOZEH30,
#                                         zoomToBounds=True,
#                                         zoomToBoundsOnClick=True,
                                        hoverStyle=arrow_function(
                                            dict(
                                                weight=5,
                                                color='#222',
                                                dashArray=''
                                            )
                                        ),
                                        options={
                                            "style": {
                                                "color": "green"
                                            }
                                        }                                       
                                    )                                    
                                ],
                                name="حوضه درجه دو",
                                checked=False
                            )                            
                        ] + [
                            dl.Overlay(
                                children=[
                                    dl.GeoJSON(
                                        id="mahdoude",
                                        url=MAHDOUDE,
                                        zoomToBounds=True,
                                        zoomToBoundsOnClick=True,
                                        hoverStyle=arrow_function(
                                            dict(
                                                weight=5,
                                                color='#222',
                                                dashArray=''
                                            )
                                        ),
                                        options={
                                            "style": {
                                                "color": "tomato"
                                            }
                                        }                                       
                                    )                                    
                                ],
                                name="محدوده مطالعاتی",
                                checked=True
                            )                            
                        ]
                    ),
                    dl.LocateControl(
                        options={
                            'locateOptions': {
                                'enableHighAccuracy': True
                            }
                        }
                    ),
                    dl.MeasureControl(
                        position="topleft",
                        primaryLengthUnit="kilometers",
                        primaryAreaUnit="hectares",
                        activeColor="#214097",
                        completedColor="#972158"
                    ),
                    search_bar,
                    info,
                    model,
                    model2,
                    model3,
                ],
                style={
                    'height': '85vh'
                },
            ),
        ],
        dir="rtl"
    ),
    html.Div(
        children=[
            html.Div(
                id="out1",
                className="col-6"
            ),
            html.Div(
                id="out2",
                className="col-6"
            )
        ],
        className="row"
    )
])


