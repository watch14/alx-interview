#!/usr/bin/node

const express = require('express')
const app = express()

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`

app.get(url, (err, resp, body) =>{
    if (err) {
        console.error(err);
    } else {
        const data = JSON.parse(body);
        console.log(data);
    }
});