#!/usr/bin/node
'user strict'

const num = Number(process.argv[2])
Number.isInteger(num) ? console.log(`My number: ${num}`) : console.log('Not a number')
// const num = process.argv[2]
// num.isNaN ? console.log('Not a number') : console.log(`My number: ${num}`)
//not working
