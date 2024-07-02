import json
import pickle
import pandas as pd
import numpy as np

_data_columns = None
_model = None
_poly = None
_scaler = None

def artifacts():
    global _data_columns
    global _model
    global _poly
    global _scaler

    with open('columns.json','r') as f:
        _data_columns = json.load(f)['features']

    with open('model.pkl' , 'rb') as f:
        _model = pickle.load(f)

    with open('poly.pkl' , 'rb') as f:
        _poly = pickle.load(f)

    with open('scaler.pkl' , 'rb') as f:
        _scaler = pickle.load(f)


def make_predictions(item_id,item_id_num,item_weight,item_fat_content,item_vis,item_type,item_mrp,outlet_ide,outlet_est_year,outlet_size,outlet_location_type,outlet_type):
    item_id = item_id
    item_id_num = item_id_num
    item_weight = item_weight
    item_fat_content = item_fat_content
    item_vis = item_vis
    item_type = item_type
    item_mrp = item_mrp
    outlet_ide = outlet_ide
    outlet_est_year = outlet_est_year
    outlet_size = outlet_size
    outlet_location_type = outlet_location_type
    outlet_type = outlet_type

    ifc = lambda item_fat_content : 0 if item_fat_content == 'Low Fat' else 1
    os = lambda outlet_size : 0 if outlet_size == 'Small' else 1 if outlet_size == 'Medium' else 2
    olt = lambda outlet_location_type : 0 if outlet_location_type == 'Tier 1' else 1 if outlet_location_type == 'Tier 2' else 2
    ot = lambda outlet_type : 0 if outlet_type == 'Grocery Store' else 1 if outlet_type == 'Supermarket Type1' else 2 if outlet_type == 'Supermarket Type2' else 3


    input = np.zeros(len(_data_columns))

    input[0] = item_id_num
    input[1] = item_weight
    input[2] = ifc(item_fat_content)
    input[3] = item_vis
    input[4] = item_mrp
    input[5] = outlet_ide
    input[6] = outlet_est_year
    input[7] = os(outlet_size)
    input[8] = olt(outlet_location_type)
    input[9] = ot(outlet_type)

    input[_data_columns.index('Item_ide_' + item_id)] = 1
    input[_data_columns.index('Item_Type_' + item_type)] = 1

    input = pd.DataFrame([input], columns = _data_columns)

    #print(np.exp(_model.predict(_scaler.transform(_poly.transform(input)))))
    return np.round(np.exp(_model.predict(_scaler.transform(_poly.transform(input))))[0],2)

def show_data_columns():
    return _data_columns


artifacts()
#make_predictions()
#print(show_data_columns())