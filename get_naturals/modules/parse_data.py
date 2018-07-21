import json

def get_data_from_string(input_string):
    input_string = str(input_string)
    input_string = input_string[2:-1]
    input_string = input_string.split(";")
    return input_string

def dict_from_data(input_data):
    res = {}
    total_data_dict = {}
    channel_dict = {}
    channels_dict = {}
    mp_dict = {}
    channel_offset = 0
    inside_offset = 0
    mp_channel_offset = 0
    for data_offset in range(len(input_data)):
        if data_offset == 0:
            total_data_dict["budget"] = float(input_data[data_offset])
        if data_offset == 1:
            total_data_dict["spot_duration"] = float(input_data[data_offset])
        if data_offset == 2:
            total_data_dict["days_on_air"] = float(input_data[data_offset])
        if data_offset == 3:
            total_data_dict["spots_per_day"] = float(input_data[data_offset])
        if data_offset == 4:
            total_data_dict["orbita"] = float(input_data[data_offset])
            res["total_data"] = total_data_dict
        if data_offset > 4 and data_offset < 165:
            if inside_offset == 0:
                channel_dict["tvr"] = float(input_data[data_offset])
                inside_offset = inside_offset + 1
            elif inside_offset == 1:
                channel_dict["affinity"] = float(input_data[data_offset])
                inside_offset = inside_offset + 1
            elif inside_offset == 2:
                channel_dict["tcpp"] = float(input_data[data_offset])
                inside_offset = inside_offset + 1
            elif inside_offset == 3:
                channel_dict["prime"] = float(input_data[data_offset])
                channels_dict[channel_offset] = channel_dict
                channel_dict = {}
                inside_offset = 0
                channel_offset = channel_offset + 1
        if data_offset == 164:
            res["channels_data"] = channels_dict
        if data_offset > 164:
            mp_dict[mp_channel_offset] = input_data[data_offset]
            mp_channel_offset = mp_channel_offset + 1
    res["mp"] = mp_dict
    return res
        
def parse(input_data):
    return(dict_from_data(get_data_from_string(input_data)))
    #return dict_from_data(get_data_from_string(input_data)) 
        

