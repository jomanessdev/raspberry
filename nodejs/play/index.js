var express = require('express');
var app =  express();

app.use(function(err,req,res,next){
console.error(err.stack);
res.status(500).send('Error for some reason');
});

app.get('/hello',(request,response) => {

    console.log(request);
    response.send('Hello world');

});

app.listen(8080, () => console.log('Listening on port 8080'));
