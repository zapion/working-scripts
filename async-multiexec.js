#!/usr/local/bin/node
exec = require('child_process').exec
promisify = require('util').promisify

pexec = promisify(exec)


arr = [1,2,3,4,5]
console.log(Date.now())
Promise.all(
  arr.map(value=>{
    return pexec('sleep 3').then(out => {
      console.log('value = ' + value)
      console.log(JSON.stringify(out))
    }
  )})
).then(function(value) {
  console.log(Date.now() + 'finish!')
})
