import mongoose from 'mongoose'

mongoose.connect('mongodb://localhost:27107/calicheProducts', { useUnifiedTopology: true, useNewUrlParser: true })

const db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
  //define schema here
});
