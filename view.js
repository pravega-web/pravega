// This is for routing all the front end  folders and the data required to bind them.

module.exports = (app)=>{

  app.get('/api/event',(req, res)=>{
    console.log(req.query.name)
    event.findOne({name:req.query.name},(e,d)=>{
      if(e) throw e;
      if(!d){
        res.send('204')
      } else {
        res.send(d);
      }
    })
  })

  app.post('/api/event',(req, res)=>{
    console.log(req.body);
    event.updateOne({ _id: req.body._id},req.body,(err,data)=>{
      if(err)throw err;
      console.log(data.nModified);
      res.send(data)
    })
  })

}