#import numpy
import xlwt

inppp = {'total_data': {'budget': 50000000, 'spot_duration': 15.0, 'days_on_air': 28.0, 'spots_per_day': 10.0, 'orbita': 10.0}, 'channels_data': {0: {'tvr': 1.15, 'affinity': 0.82, 'tcpp': 199099.47, 'prime': 60.0}, 1: {'tvr': 0.87, 'affinity': 0.37, 'tcpp': 168601.23, 'prime': 65.0}, 2: {'tvr': 0.48, 'affinity': 0.29, 'tcpp': 197883.46, 'prime': 60.0}, 3: {'tvr': 1.56, 'affinity': 1.13, 'tcpp': 121192.4, 'prime': 60.0}, 4: {'tvr': 0.89, 'affinity': 0.97, 'tcpp': 133651.42, 'prime': 65.0}, 5: {'tvr': 0.53, 'affinity': 0.56, 'tcpp': 123271.74, 'prime': 65.0}, 6: {'tvr': 0.4, 'affinity': 0.48, 'tcpp': 159804.14, 'prime': 60.0}, 7: {'tvr': 0.36, 'affinity': 0.61, 'tcpp': 83219.06, 'prime': 45.0}, 8: {'tvr': 0.47, 'affinity': 1.07, 'tcpp': 111389.1, 'prime': 65.0}, 9: {'tvr': 0.47, 'affinity': 1.19, 'tcpp': 91025.76, 'prime': 55.0}, 10: {'tvr': 0.09, 'affinity': 0.7, 'tcpp': 106424.18, 'prime': 55.0}, 11: {'tvr': 0.23, 'affinity': 1.15, 'tcpp': 61204.02, 'prime': 55.0}, 12: {'tvr': 0.13, 'affinity': 0.25, 'tcpp': 159056.19, 'prime': 55.0}, 13: {'tvr': 0.58, 'affinity': 0.74, 'tcpp': 81861.5, 'prime': 45.0}, 14: {'tvr': 0.07, 'affinity': 0.2, 'tcpp': 159066.45, 'prime': 55.0}, 15: {'tvr': 0.11, 'affinity': 0.36, 'tcpp': 141885.06, 'prime': 55.0}, 16: {'tvr': 0.12, 'affinity': 0.31, 'tcpp': 175120.33, 'prime': 45.0}, 17: {'tvr': 0.22, 'affinity': 0.8, 'tcpp': 90704.02, 'prime': 45.0}, 18: {'tvr': 0.07, 'affinity': 0.86, 'tcpp': 56720.82, 'prime': 55.0}, 19: {'tvr': 0.1, 'affinity': 0.67, 'tcpp': 118522.06, 'prime': 55.0}, 20: {'tvr': 0.2, 'affinity': 1.28, 'tcpp': 65135.7, 'prime': 55.0}, 21: {'tvr': 0.06, 'affinity': 0.6, 'tcpp': 87701.08, 'prime': 45.0}, 22: {'tvr': 0.01, 'affinity': 1.13, 'tcpp': 39544.05, 'prime': 55.0}, 23: {'tvr': 0.08, 'affinity': 0.49, 'tcpp': 75378.38, 'prime': 55.0}, 24: {'tvr': 0.59, 'affinity': 0.85, 'tcpp': 58843.63, 'prime': 40.0}, 25: {'tvr': 0.36, 'affinity': 0.39, 'tcpp': 51485.61, 'prime': 55.0}, 26: {'tvr': 0.3, 'affinity': 0.31, 'tcpp': 57897.07, 'prime': 60.0}, 27: {'tvr': 0.66, 'affinity': 1.17, 'tcpp': 35375.4, 'prime': 55.0}, 28: {'tvr': 0.48, 'affinity': 0.91, 'tcpp': 45794.3, 'prime': 60.0}, 29: {'tvr': 0.33, 'affinity': 0.61, 'tcpp': 37923.06, 'prime': 60.0}, 30: {'tvr': 0.21, 'affinity': 0.53, 'tcpp': 43271.42, 'prime': 65.0}, 31: {'tvr': 0.19, 'affinity': 0.79, 'tcpp': 22630.2, 'prime': 55.0}, 32: {'tvr': 0.32, 'affinity': 1.09, 'tcpp': 28286.33, 'prime': 65.0}, 33: {'tvr': 0.29, 'affinity': 1.32, 'tcpp': 24095.45, 'prime': 55.0}, 34: {'tvr': 0.07, 'affinity': 0.3, 'tcpp': 63517.07, 'prime': 55.0}, 35: {'tvr': 0.06, 'affinity': 0.23, 'tcpp': 73990.24, 'prime': 55.0}, 36: {'tvr': 0.07, 'affinity': 0.35, 'tcpp': 48360.77, 'prime': 55.0}, 37: {'tvr': 0.05, 'affinity': 0.57, 'tcpp': 38475.68, 'prime': 50.0}, 38: {'tvr': 0.0, 'affinity': 0.0, 'tcpp': 0.0, 'prime': 0.0}, 39: {'tvr': 0.0, 'affinity': 0.0, 'tcpp': 0.0, 'prime': 0.0}}, 'mp': {0: 'Yes', 1: 'No', 2: 'Calculate', 3: 'Calculate', 4: 'Calculate', 5: 'Calculate', 6: 'Calculate', 7: 'Calculate', 8: 'Calculate', 9: 'Calculate', 10: 'Calculate', 11: 'Calculate', 12: 'Calculate', 13: 'Calculate', 14: 'Calculate', 15: 'Calculate', 16: 'Calculate', 17: 'Calculate', 18: 'Calculate', 19: 'Calculate', 20: 'Calculate', 21: 'Calculate', 22: 'Calculate', 23: 'Calculate', 24: 'Calculate', 25: 'Calculate', 26: 'Calculate', 27: 'Calculate', 28: 'Calculate', 29: 'Calculate', 30: 'Calculate', 31: 'Calculate', 32: 'Calculate', 33: 'Calculate', 34: 'Calculate', 35: 'Calculate', 36: 'Calculate', 37: 'Yes', 38: 'Calculate', 39: 'Calculate'}}
ccc = ['PERVY KANAL', 'ROSSIYA 1', 'NTV', 'TNT', 'STS', 'PYATY KANAL', 'REN TV', 'DOMASHNY', 'TV-3', 'FRIDAY', 'CHE', 'U', 'TV TSENTR', 'KARUSEL', 'ZVEZDA', 'ROSSIYA 24', 'MATCH TV', 'KANAL DISNEY', 'STS LOVE', 'TNT 4', 'MUZ TV', '2x2', 'SUPER', 'MIR', 'PERVY KANAL - O', 'ROSSIYA 1 - O', 'NTV - O', 'TNT - O', 'STS - O', 'PYATY KANAL - O', 'REN TV - O', 'DOMASHNY - O', 'TV-3 - O', 'FRIDAY - O', 'TV TSENTR - O', 'ZVEZDA - O', 'MATCH TV - O', 'TNT 4 - O', 'Reserve opt', 'Reserve opt']
ddd = ['National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'National', 'Orbital', 'Orbital', 'Orbital', 'Orbital', 'Orbital', 'Orbital', 'Orbital', 'Orbital', 'Orbital', 'Orbital', 'Orbital', 'Orbital', 'Orbital', 'Orbital', 'Reserve opt', 'Reserve opt']

def get_channels_params(input_dict):
	tvr = []
	affinity = []
	tcpp = []
	prime = []
	mp = []
	for keys in input_dict["channels_data"]:
		tvr.append(input_dict["channels_data"][keys]["tvr"])
		affinity.append(input_dict["channels_data"][keys]["affinity"])
		tcpp.append(input_dict["channels_data"][keys]["tcpp"])
		prime.append(input_dict["channels_data"][keys]["prime"])
		mp.append(input_dict["mp"][keys])
	return tvr, affinity, tcpp, prime, mp

#tvr, affinity, tcpp, prime, mp = get_channels_params(inppp)

def break_params_by_distr(param, distr):
    nat_param = []
    orb_param = []
    result = []
    for n in range(len(distr)):
        if distr[n] == "National":
            nat_param.append(param[n])
        else:
            orb_param.append(param[n])
    result.append(nat_param)
    result.append(orb_param)
    return result


def params_break(inpp_data, inpp_channels, inpp_distr):
    result = []
    tvr, affinity, tcpp, prime, mp = get_channels_params(inpp_data)
    for param in inpp_channels, tvr, affinity, tcpp, prime, mp:
        result.append(break_params_by_distr(param, inpp_distr))
    return result

#print(params_break(inppp,ccc,ddd))

def make_rank(input_list, inverse=False):
    if inverse == False:
        min_val = min(input_list)
        for n in range(len(input_list)):
            input_list[n] = input_list[n] - min_val
    if inverse == True:
        max_val = max(input_list)
        for n in range(len(input_list)):
            input_list[n] = max_val - input_list[n]
    max_val = max(input_list)
    for n in range(len(input_list)):
        input_list[n] = input_list[n]/max_val
    return input_list

def combinated_rank(input_list, proportion_list):
    result = []
    for n in range(len(input_list[0])):
        result.append(input_list[0][n] * proportion_list[0] + input_list[1][n] * proportion_list[1] + input_list[2][n] * proportion_list[2])
    min_val = min(result)
    for n in range(len(result)):
        result[n] = result[n] - min_val
    max_val = max(result)
    for n in range(len(result)):
        result[n] = result[n]/max_val
    return result
    
def make_ranks(input_list):
    pre_result = []
    for n in range(3):
        if n == 2:
            pre_result.append(make_rank(input_list[n+1][0], True))
        else:
            pre_result.append(make_rank(input_list[n+1][0], False))
    result = pre_result
    result.append(combinated_rank(pre_result, [0.333, 0.333, 0.333]))
    result.append(combinated_rank(pre_result, [0.5, 0.5, 0.0]))
    result.append(combinated_rank(pre_result, [0.5, 0.0, 0.5]))
    result.append(combinated_rank(pre_result, [0.0, 0.5, 0.5]))
    return result

def make_nat_mix_from_rank(rank):
	result = []
	inside_rank = rank
	for mix_iterator in range(len(rank)):
		current_mix = [0 for i in range(len(rank))]
		max_rank = max(inside_rank)
		for channel_iterator in range(len(rank)):
			if inside_rank[channel_iterator] == -1:
				current_mix[channel_iterator] = 1
		for channel_iterator in range(len(rank)):
			if inside_rank[channel_iterator] == max_rank:
				current_mix[channel_iterator] = 1
				inside_rank[channel_iterator] = -1
				break
		result.append(current_mix)
	return result

def make_nat_mixes_from_ranks(ranks):
	result = []
	for rank in ranks:
		result.extend(make_nat_mix_from_rank(rank))
	return result

def check_mixes_for_mandatory(mixes, mp_array):
	for channel_offset in range(len(mp_array)):
		if mp_array[channel_offset] == "Yes":
			for mix_offset in range(len(mixes)):
				mixes[mix_offset][channel_offset] = 1
		if mp_array[channel_offset] == "No":
			for mix_offset in range(len(mixes)):
				mixes[mix_offset][channel_offset] = 0
	return mixes

def check_for_doublets(mixes):
	result = []
	mixes_to_delete = []
	for mix in mixes:
		if mix not in result:
			result.append(mix)
	return result

#def generate_orbital_mix:

#params = params_break(inppp,ccc,ddd)
#ranks = make_ranks(params)
#params = params_break(inppp,ccc,ddd)
#mixes = make_nat_mixes_from_ranks(ranks)
#final_nat_mixes = check_mixes_for_mandatory(mixes, params[5][0])
#mixes = check_for_doublets(final_nat_mixes)
#print(params[5][0])

def get_orbital_offset(national_offset):
	orbital_offset = [0,1,2,3,4,5,6,7,8,9,"","",10,"",11,"",12,"","",13,"","","",""]
	return orbital_offset[national_offset]

#print(get_orbital_offset(23))

def generate_orbital_mix(national_mix, params_for_len):
	orbital_mix = [0 for i in range(len(params_for_len))]
	for channel_offset in range(len(national_mix)):
		if national_mix[channel_offset] == 1 and get_orbital_offset(channel_offset) != "":
			orbital_mix[get_orbital_offset(channel_offset)] = 1
	return orbital_mix

def generate_orbital_mixes(national_mixes, params_for_len):
	result = []
	for national_mix in national_mixes:
		mix_to_insert = []
		mix_to_insert = generate_orbital_mix(national_mix, params_for_len)
		if sum(mix_to_insert) == 0:
			mix_to_insert = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		result.append(mix_to_insert)
	return result

def merge_nat_orb_mix(national_mixes, orbital_mixes):
	result = []
	for mix_offset in range(len(national_mixes)):
		total_mix = []
		total_mix.append(national_mixes[mix_offset])
		total_mix.append(orbital_mixes[mix_offset])
		result.append(total_mix)
	return result

#print(params[1])

def insert_tvr_to_mix(mix, param):
	for distribution_offset in range(len(mix)):
		for channel_offset in range(len(mix[distribution_offset])):
			if mix[distribution_offset][channel_offset] == 1:
				mix[distribution_offset][channel_offset] = param[distribution_offset][channel_offset]
	return mix

def insert_tvrs_to_mixes(mixes, param):
	result = []
	for mix_offset in range(len(mixes)):
		result.append(insert_tvr_to_mix(mixes[mix_offset],param))
	return result

def make_percent_from_tvrs(mix):
	for distribution_offset in range(len(mix)):
		current_distribution_sum = sum(mix[distribution_offset])
		for channel_offset in range(len(mix[distribution_offset])):
			mix[distribution_offset][channel_offset] = mix[distribution_offset][channel_offset]/current_distribution_sum
	return mix

def insert_percents_to_mixes(mixes):
	result = []
	for mix_offset in range(len(mixes)):
		result.append(make_percent_from_tvrs(mixes[mix_offset]))
	return result

def make_mix_total(mix, orbital_percent):
	result = []
	for distribution_offset in range(len(mix)):
		for channel_offset in range(len(mix[distribution_offset])):
			if distribution_offset == 0:
				result.append(mix[distribution_offset][channel_offset] * (1 - (orbital_percent/100)))
			if distribution_offset == 1:
				result.append(mix[distribution_offset][channel_offset] * (orbital_percent/100))
	return result

def make_mixes_total(mixes, orbital_percent):
	result = []
	for mix in mixes:
		result.append(make_mix_total(mix, orbital_percent))
	return result

def get_tcpp_from_mix(mix, tcpp):
	result = [0 for i in range(len(mix))]
	for channel_offset in range(len(mix)):
		result[channel_offset] = mix[channel_offset] * tcpp[channel_offset]
	return sum(result)

def get_tcpp_for_mixes(mixes, tcpp):
	result = []
	tcpp_list = []
	for distribution_offset in range(len(tcpp)):
		tcpp_list.extend(tcpp[distribution_offset])
	for mix_offset in range(len(mixes)):
		result.append(get_tcpp_from_mix(mixes[mix_offset], tcpp_list))
	return result

def get_wtrps(budget, tcpp):
	result = []
	for mix_offset in range(len(tcpp)):
		result.append(budget/tcpp[mix_offset])
	return result

def get_trps(spot_duration, wtrp):
	result = []
	for mix_offset in range(len(wtrp)):
		result.append(wtrp[mix_offset]*30/spot_duration)
	return result 
	
def insert_trp_to_mix(mix, trp):
	result = [0 for i in range(len(mix))]
	for channel_offset in range(len(mix)):
		result[channel_offset] = mix[channel_offset]*trp	
	return result

def insert_trps_to_mixes(mixes, trps):
	result = []
	for mix_offset in range(len(mixes)):
		result.append(insert_trp_to_mix(mixes[mix_offset], trps[mix_offset]))
	return result

def make_spots_from_mix(mix, tvrs):
	result = []
	for channel_offset in range(len(mix)):
		result.append(mix[channel_offset]/tvrs[channel_offset])
	return result

def check_mix_for_overspot(mix, tvr, spots_limit):
	result = False
	for channel_offset in range(len(mix)):
		if tvr[channel_offset] > 0:
			if mix[channel_offset]/tvr[channel_offset] > spots_limit:
				result = True
	return result

def delete_overspot_mixes(mixes, tvr, spots_limit):
	tvr_list = []
	result = []
	for distribution_offset in range(len(tvr)):
		tvr_list.extend(tvr[distribution_offset])
	for mix_offset in range(len(mixes)):
		if check_mix_for_overspot(mixes[mix_offset], tvr_list, spots_limit) == False:
			result.append(mixes[mix_offset])
	return result

def break_by_prime(mix, prime):
	result = []
	for channel_offset in range(len(mix)):
		result.append(mix[channel_offset]*(prime[channel_offset]/100))
		result.append(mix[channel_offset]*(1 - (prime[channel_offset]/100)))
	return result

def break_mixes_by_prime(mixes, prime):
	prime_list = []
	result = []
	for distribution_offset in range(len(prime)):
		prime_list.extend(prime[distribution_offset])
	for mix_offset in range(len(mixes)):
		result.append(break_by_prime(mixes[mix_offset], prime_list))
	return result

def make_string_from_mixes(mixes):
	result = ""
	for channel_offset in range(len(mixes[0])):
		for mix_offset in range(len(mixes)):
			if mix_offset == 0:
				result = result + str(mixes[mix_offset][channel_offset])
			else:
				result = result + "\t" + str(mixes[mix_offset][channel_offset])
		result = result + "\n"
	return result

def make_txt_file_from_mixes(mixes):
	file = open("/root/split_combinator/get_naturals/templates/get_naturals/static/result.txt", "w")
	file.write(mixes)
	file.close()

#def make_xl_file_frddom_mi

def generate_mix(input_data, channels_data, distribution_data):
	params = params_break(input_data, channels_data, distribution_data)
	ranks = make_ranks(params)
	params = params_break(input_data, channels_data, distribution_data)
	nat_mixes = make_nat_mixes_from_ranks(ranks)
	nat_mixes = check_mixes_for_mandatory(nat_mixes, params[5][0])
	nat_mixes = check_for_doublets(nat_mixes)
	orb_mixes = generate_orbital_mixes(nat_mixes, params[0][1])
	orb_mixes = check_mixes_for_mandatory(orb_mixes, params[5][1])
	mixes = merge_nat_orb_mix(nat_mixes, orb_mixes)
	mixes = insert_tvrs_to_mixes(mixes, params[1])
	mixes = insert_percents_to_mixes(mixes)
	mixes = make_mixes_total(mixes, input_data['total_data']['orbita'])
	print(params[3])
	print(mixes[3])
	tcpps = get_tcpp_for_mixes(mixes, params[3])	
	print(tcpps[3])
	wtrps = get_wtrps(input_data['total_data']['budget'], tcpps)
	print(wtrps[3])
	trps = get_trps(input_data['total_data']['spot_duration'], wtrps)
	print(trps[3])
	print(input_data['total_data']['budget'])
	print(input_data['total_data']['spot_duration'])
	mixes = insert_trps_to_mixes(mixes, trps)
	#print(len(mixes))	
	mixes = delete_overspot_mixes(mixes, params[1], input_data['total_data']['days_on_air'] * input_data['total_data']['spots_per_day'])
	#print(len(mixes))
	#print(len(tcpp))
	#print(len(mixes))
	#print(wtrp)
	#print(trp)
	#print(insert_trps_to_mixes(mixes[0],trp[0]))	
	#print(mixes)
	mixes = break_mixes_by_prime(mixes, params[4])
	print(mixes[3])
	mixes = make_string_from_mixes(mixes)
	#make_txt_file_from_mixes(mixes)
	return mixes

#print(generate_mix(inppp, ccc, ddd))
#priinnt(make_mixes_total(insert_percents_to_mixes(insert_tvrs_to_mixes(merge_nat_orb_mix(mixes, generate_orbital_mixes(mixes, params[5][1])), params[1])), 10))
