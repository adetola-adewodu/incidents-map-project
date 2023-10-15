import os
import json

from geojson import Feature, Point, FeatureCollection, dumps


path = "./data/"
dir_list = os.listdir(path)

features = []
for file in dir_list:
    file = path +file
    json_file = open(file)

    data = json.load(json_file)

    for i in data:
        if i == 'address':
            full_address = data[i].get("common_place_name") + " "
            full_address += data[i].get("address_line1") +" " +data[i].get("city")
            print(full_address)
            longitude = data[i].get('longitude')
            latitude = data[i].get('latitude')
            my_point = Point((longitude, latitude))
            temp_feature = Feature(geometry=my_point, properties={"address": full_address})
            features.append(temp_feature)
        
        if i == 'apparatus':

            
            status = data[i][0]['unit_status']
            if status.get('acknowledged'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " acknowledged"
                longitude = data[i][0]['unit_status']['acknowledged'].get('longitude')
                latitude = data[i][0]['unit_status']['acknowledged'].get('latitude')
                my_point = Point((longitude, latitude))
                temp_feature = Feature(geometry=my_point, properties={"address": full_address})
                features.append(temp_feature)

            if status.get('arrived'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " arrived"
                longitude = data[i][0]['unit_status']['arrived'].get('longitude')
                latitude = data[i][0]['unit_status']['arrived'].get('latitude')
                my_point = Point((longitude, latitude))
                temp_feature = Feature(geometry=my_point, properties={"address": full_address})
                features.append(temp_feature)
            
            if status.get('available'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " available"
                longitude = data[i][0]['unit_status']['arrived'].get('longitude')
                latitude = data[i][0]['unit_status']['arrived'].get('latitude')
                my_point = Point((longitude, latitude))
                temp_feature = Feature(geometry=my_point, properties={"address": full_address})
                features.append(temp_feature)

            if status.get('cleared'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " cleared"
                longitude = data[i][0]['unit_status']['cleared'].get('longitude')
                latitude = data[i][0]['unit_status']['cleared'].get('latitude')
                my_point = Point((longitude, latitude))
                temp_feature = Feature(geometry=my_point, properties={"address": full_address})
                features.append(temp_feature)
            
            if status.get('dispatched'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " dispatched"
                longitude = data[i][0]['unit_status']['dispatched'].get('longitude')
                latitude = data[i][0]['unit_status']['dispatched'].get('latitude')
                my_point = Point((longitude, latitude))
                temp_feature = Feature(geometry=my_point, properties={"address": full_address})
                features.append(temp_feature)

            if status.get('enroute'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " enroute"
                longitude = data[i][0]['unit_status']['enroute'].get('longitude')
                latitude = data[i][0]['unit_status']['enroute'].get('latitude')
                my_point = Point((longitude, latitude))
                temp_feature = Feature(geometry=my_point, properties={"address": full_address})
                features.append(temp_feature)
            
            if status.get('~'):
                full_address = data[i][0]["station"] + " " + data[i][0]["unit_id"] 
                full_address += " ~"
                longitude = data[i][0]['unit_status']['~'].get('longitude')
                latitude = data[i][0]['unit_status']['~'].get('latitude')
                my_point = Point((longitude, latitude))
                temp_feature = Feature(geometry=my_point, properties={"address": full_address})
                features.append(temp_feature)

number_of_features = len(features)

feature_collection = FeatureCollection(features)
geo_json_output = dumps(feature_collection, sort_keys=True)

output_file = open("data.geojson", "w")
output_file.write(geo_json_output)
output_file.close()