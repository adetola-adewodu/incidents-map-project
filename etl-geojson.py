import os
import json

from geojson import Feature, Point, FeatureCollection, dumps



def get_station_address_feature(features, data, index, coordinate_key):
    full_address = data[index][0]["station"] + " " + data[index][0]["unit_id"] 
    full_address += " " + coordinate_key
    longitude = data[index][0]['unit_status'][coordinate_key].get('longitude')
    latitude = data[index][0]['unit_status'][coordinate_key].get('latitude')
    my_point = Point((longitude, latitude))
    temp_feature = Feature(geometry=my_point, properties={"address": full_address})
    features.append(temp_feature)
    return features

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
                features = get_station_address_feature(features, data, i, 'acknowledged')

            if status.get('arrived'):
                features = get_station_address_feature(features, data, i, 'arrived')
            
            if status.get('available'):
                features = get_station_address_feature(features, data, i, 'available')

            if status.get('cleared'):
                features = get_station_address_feature(features, data, i, 'cleared')
            
            if status.get('dispatched'):
                features = get_station_address_feature(features, data, i, 'dispatched')

            if status.get('enroute'):
                features = get_station_address_feature(features, data, i, 'enroute')
            
            if status.get('~'):
                features = get_station_address_feature(features, data, i, '~')

number_of_features = len(features)
print(number_of_features)

feature_collection = FeatureCollection(features)
geo_json_output = dumps(feature_collection, sort_keys=True)

output_file = open("data.geojson", "w")
output_file.write(geo_json_output)
output_file.close()