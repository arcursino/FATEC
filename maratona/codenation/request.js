const request = require ('request')

const fs = require('fs')

request('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=43cee38a24b531ad1080b933cfa52ba9bce731ff').pipe(fs.createWriteStream('answer.json'))


curl -v \
    -F "answer=@answer.json" \
    'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=43cee38a24b531ad1080b933cfa52ba9bce731ff'

