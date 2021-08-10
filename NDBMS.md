const productSchema = new Schema({
  id: Number,
  name: String,
  slogan: String,
  description: String,
  category: String,
  default_price: String,
  related: [ {product_id: Number} ],
  features: [ {feature: String, value: String} ],
});

const styleSchema = new Schema({
  style_id: Number,
  product_id: Number,
  name: String,
  original_price: String,
  sale_price: String,
  default?: Boolean,
  photos: [ {url: String, thumnail_url: String} ],
  skus: [ {quantity: Number, size: String} ],
});

