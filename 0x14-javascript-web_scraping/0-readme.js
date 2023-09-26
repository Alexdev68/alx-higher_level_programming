#!/usr/bin/node

const fs = require('fs');
const process = require('process')
const argv = process.argv

fs.readFile(argv[2], 'utf-8', (err, data) => {
	if (err) {
		console.log(err);
		return
	}
	console.log(data);
});
