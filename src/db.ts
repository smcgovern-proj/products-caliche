import mongoose from 'mongoose'

mongoose.connect('mongodb://localhost:27017/calicheProducts', { useUnifiedTopology: true, useNewUrlParser: true }).catch(err => console.log('err on connect', err))

const db = mongoose.connection

db.on('error', console.error.bind(console, 'connection error:'))
db.once('open', () => {
  console.log('successfully opened connection to mongoDB')

  const productSchema = new mongoose.Schema({
    id: {type: Number, required: true},
    name: String,
    slogan: String,
    description: String,
    category: String,
    default_price: String,
    related: [ {product_id: Number} ],
    features: [ {feature: String, value: String} ],
  })

  const styleSchema = new mongoose.Schema({
    style_id: {type: Number, required: true},
    product_id: {type: Number, required: true},
    name: String,
    original_price: String,
    sale_price: String,
    default: Boolean,
    photos: [ {url: String, thumnail_url: String} ],
    skus: [ {quantity: Number, size: String} ],
  })

  const Product = mongoose.model('Product', productSchema);
  const Style = mongoose.model('Style', styleSchema);

})

export default db
