# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'F', 'L', 'R']
NF_moves = ['L', 'L', 'R']
LF_moves = ['L', 'F', 'F']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():

    request.get_data()
    data = request.json
    logger.info(data)

    map_x = data['arena']['dims'][0]
    map_y = data['arena']['dims'][1]
    logger.info(data['arena']['state']['https://cloud-run-hackathon-python-pe4heri35a-uc.a.run.app'])
    my_x = data['arena']['state']['https://cloud-run-hackathon-python-pe4heri35a-uc.a.run.app']['x']
    my_y = data['arena']['state']['https://cloud-run-hackathon-python-pe4heri35a-uc.a.run.app']['y']
    my_d = data['arena']['state']['https://cloud-run-hackathon-python-pe4heri35a-uc.a.run.app']['direction']
    wasHit = data['arena']['state']['https://cloud-run-hackathon-python-pe4heri35a-uc.a.run.app']['wasHit']

    state=data['arena']['state']

        
    if wasHit:
        return LF_moves[random.randrange(len(LF_moves))]

    for player in state:

        if player == 'https://cloud-run-hackathon-python-pe4heri35a-uc.a.run.app':
            continue

        if  0 <= my_x - state[player]['x'] <=3 and my_y == state[player]['y'] and my_d == 'W':
            logger.info(1)
            logger.info('kill: ' + str(state[player]))
            return "T"

        if  0 <= my_y - state[player]['y'] <=3 and my_x == state[player]['x'] and my_d == 'N':
            logger.info(2)
            logger.info('kill: ' + str(state[player]))
            return "T"

        if  0 <= state[player]['y'] - my_y <=3 and my_x == state[player]['x'] and my_d == 'S':
            logger.info(3)
            logger.info('kill: ' + str(state[player]))
            return "T"

        if  0 <= state[player]['x'] - my_x <=3 and my_y == state[player]['y'] and my_d == 'E':
            logger.info(4)
            logger.info('kill: ' + str(state[player]))
            return "T"


    if (0 < map_x - my_x <= 2 and my_d == 'E') or (0 < map_y - my_y <= 2 and my_d == 'S') or (0 < my_y - map_y <= 2 and my_d == 'N') or (0< my_y - map_y <= 2 and my_d == 'W'):
        logger.info(5)
        return NF_moves[random.randrange(len(NF_moves))]


    logger.info(6)

    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
