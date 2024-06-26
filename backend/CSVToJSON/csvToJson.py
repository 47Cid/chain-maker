import csv
import json
import secrets

index_protocol = 1
index_standard = 3
index_devices = 4
index_requ_hardware = 5
index_paper_name = 9
conference = 10
open_source_repo = 11
cve_number = 12
index_prior_state = 13
info_required = 14
index_post_state = 15
info_gained = 16

index = 0


with open('/Users/adithya/Documents/CIS Spring 2024/project/chain-maker/backend/CSVToJSON/entries1.csv') as file:
    #read in the attacks csv file
    csv_reader = csv.reader(file)


    #skip the heading line
    next(csv_reader)
    #convert all of the attacks into dictionaries and store them in a list
    attack_dict_list = []
    for attack in csv_reader:
        temp_dict = {}
        
        #keep a space open for an id to be saved since we want this to be the first val for asthetics
        index += 1
        temp_dict['id'] = index

        #save the attack name
        temp_dict['name'] = attack[index_paper_name]

        #save prior state 
        prior_state_dict = {}
        for state in attack[index_prior_state].split(','):
            state = state.strip()
            prior_state_dict[state] = state
        temp_dict['initState'] = prior_state_dict

        #save post state 
        post_state_dict = {}
        for state in attack[index_post_state].split(','):
            state = state.strip()
            post_state_dict[state] = state
        temp_dict['endState'] = post_state_dict

        temp_dict['conference'] = attack[conference].split(',')
        for(i, item) in enumerate(temp_dict['conference']):
            temp_dict['conference'][i] = item.strip()
        
        temp_dict['open_source_repo'] = attack[open_source_repo].split(',')
        for(i, item) in enumerate(temp_dict['open_source_repo']):
            temp_dict['open_source_repo'][i] = item.strip()
        
        temp_dict['cve_number'] = attack[cve_number].split(',')
        for(i, item) in enumerate(temp_dict['cve_number']):
            temp_dict['cve_number'][i] = item.strip()

        #save prior knowledge
        temp_dict['info_required'] = attack[info_required].split(',')
        for(i, item) in enumerate(temp_dict['info_required']):
            temp_dict['info_required'][i] = item.strip()

        #save post knowledge
        temp_dict['info_gained'] = attack[info_gained].split(',')
        for(i, item) in enumerate(temp_dict['info_gained']):
            temp_dict['info_gained'][i] = item.strip()
        #save hardware requirements
        temp_dict['hardwareRequirements'] = attack[index_requ_hardware].split(',')
        for(i, item) in enumerate(temp_dict['hardwareRequirements']):
            temp_dict['hardwareRequirements'][i] = item.strip()
            
        
        #update the id with a hash of temp_dict
        #dump it to a json first to ensure stability
        # temp_dict['_id'] = {'$oid': secrets.token_hex(12)}

        #save the temp dict in the list
        attack_dict_list.append(temp_dict)

with open('attackDB.json','w') as output_file:
    json.dump(attack_dict_list,fp=output_file,indent=4)
    