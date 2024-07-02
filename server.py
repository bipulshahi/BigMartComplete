import util

from  flask import Flask,request

app = Flask(__name__)

@app.route('/data_features')
def data_features():
    return util.show_data_columns()


@app.route('/predict' , methods = ['POST'])
def predict():
    item_id = request.form['it_id']
    item_id_num = float(request.form['it_id_num'])
    item_weight = float(request.form['it_wt'])
    item_fat_content = request.form['it_fat_ct']
    item_vis = float(request.form['it_vis'])
    item_type = request.form['it_type']
    item_mrp = float(request.form['it_mrp'])
    outlet_ide = float(request.form['out_id'])
    outlet_est_year = float(request.form['out_est'])
    outlet_size = request.form['out_size']
    outlet_location_type = request.form['out_loc_type']
    outlet_type = request.form['out_type']

    result = {'Predicted Sales' : str(util.make_predictions(item_id,item_id_num,item_weight,item_fat_content,item_vis,item_type,item_mrp,outlet_ide,outlet_est_year,outlet_size,outlet_location_type,outlet_type))}
    #result = str(util.make_predictions())
    return result

app.run()