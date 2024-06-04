#!/usr/bin/node

const request = require('request')

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`

request.get(url, (err, resp, body) =>{
    if (err) {
        console.error(err);
    } else {
        const data = JSON.parse(body);
        const characters = data.characters;

        const charNames = []
        
        for (let i = 0 ; i < characters.length ; i++) {
            request.get(characters[i], (err, resp, body) =>{
                if (err) {
                    console.log(err)
                } else {
                    let data_name = JSON.parse(body);
                    console.log(data_name.name)
                    charNames.push(data_name.name);
                }
            });
        }
    }
});