#!/usr/local/bin/node
arr = [1,2,3,4,5]
console.log(Date.now())
Promise.all(
  arr.map(value=>{
    return new Promise(function(resolve, reject) {
      console.log('value = ' + value)
      if(value > 3) {
        console.log(value + " is processed")
        resolve(value)
      } else {
        console.log(value + " is rejected")
        reject(value)
      }
    }).catch(err => {
      console.log(value + " is caught")
      return err})
  })
).then(value => {
  console.log("we got in then: " + value)
  console.log(Date.now() + 'finish!')
}).catch(err => {
  console.log("something wrong: " + err)
})
