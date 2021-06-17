import os
import re
import json

action_type_pattern = re.compile('[\w]+ = \'(.+)\',')
actions_by_file = {}
repeated_actions = {}

for root, dirs, files in os.walk('./src'):
    for file in files:
        if 'actions.ts' in file:
            file_full_path = os.path.join(root, file)
            
            with open(file_full_path, 'r') as f:
                actions_by_file[file_full_path] = []
                for line in f:
                    for match in action_type_pattern.findall(line):
                        for already_checked_file_path in actions_by_file:
                            for action in actions_by_file[already_checked_file_path]:
                                if action == match:
                                    if repeated_actions.get(action) is None:
                                        repeated_actions[action] = [already_checked_file_path, file_full_path]
                                    else:
                                        repeated_actions[action].append(file_full_path)
                        actions_by_file[file_full_path].append(match)

with open('duplicate_actions.json', 'w') as fp:
    json.dump(repeated_actions, fp)
